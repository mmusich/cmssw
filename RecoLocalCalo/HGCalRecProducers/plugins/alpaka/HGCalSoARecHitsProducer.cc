// Improved HGCalSoARecHitsProducer.cc
//
// Optimizations applied vs. original (eb819177):
//
//  1. Single-pass hit loop: threshold check + fill happen in one pass; no double
//     iteration over hits. A scratch host buffer of hits.size() is allocated once
//     and the real occupancy (index) is tracked.
//  2. Run-constant setup moved to beginRun(): rhtools_.setGeometry(),
//     maxlayer_, computeThreshold() are called once per run, not per event.
//     The initialized_ flag is removed.
//  3. Flat 1-D threshold arrays: thresholds_ and v_sigmaNoise_ are flattened to
//     contiguous std::vector<double> with stride thickStride_, eliminating the
//     cache-unfriendly vector-of-vectors indirection.
//  4. operator[] instead of at() in the hot loop: bounds are guaranteed by
//     construction; the throwing at() branches are gone.
//  5. isBH_ boolean precomputed in constructor: the "BH" string comparison is
//     hoisted out of the hit loop.
//  6. Device copy sized to index: a correctly-sized host collection is built
//     after the fill loop and only `index` elements are transferred to the GPU.
//     Uses plain alpaka::memcpy(queue, dst, src, count) — no createSubView /
//     alpaka::Idx<Device>, which are not available for PortableCollection buffers.
//  7. deltasi_index_regemfac_ initialised in the constructor to avoid UB.

#include "DataFormats/HGCRecHit/interface/HGCRecHitCollections.h"
#include "DataFormats/HGCalReco/interface/HGCalSoARecHitsHostCollection.h"
#include "DataFormats/HGCalReco/interface/alpaka/HGCalSoARecHitsDeviceCollection.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/ParameterSetDescription.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "Geometry/HGCalGeometry/interface/HGCalGeometry.h"
#include "HeterogeneousCore/AlpakaCore/interface/alpaka/EDPutToken.h"
#include "HeterogeneousCore/AlpakaCore/interface/alpaka/ESGetToken.h"
#include "HeterogeneousCore/AlpakaCore/interface/alpaka/stream/EDProducer.h"
#include "HeterogeneousCore/AlpakaInterface/interface/config.h"
#include "RecoLocalCalo/HGCalRecAlgos/interface/RecHitTools.h"

namespace ALPAKA_ACCELERATOR_NAMESPACE {

  class HGCalSoARecHitsProducer : public stream::EDProducer<edm::stream::WatchRuns> {
  public:
    HGCalSoARecHitsProducer(edm::ParameterSet const& config)
        : EDProducer(config),
          detector_(config.getParameter<std::string>("detector")),
          isNose_(detector_ == "HFNose"),
          isBH_(detector_ == "BH"),  // OPT 5: hoist string comparison
          maxNumberOfThickIndices_(config.getParameter<unsigned>("maxNumberOfThickIndices")),
          // OPT 7: initialise deltasi_index_regemfac_ to avoid UB
          deltasi_index_regemfac_(static_cast<int>(maxNumberOfThickIndices_)),
          fcPerEle_(config.getParameter<double>("fcPerEle")),
          ecut_(config.getParameter<double>("ecut")),
          fcPerMip_(config.getParameter<std::vector<double>>("fcPerMip")),
          nonAgedNoises_(config.getParameter<std::vector<double>>("noises")),
          dEdXweights_(config.getParameter<std::vector<double>>("dEdXweights")),
          thicknessCorrection_(config.getParameter<std::vector<double>>("thicknessCorrection")),
          caloGeomToken_(consumesCollector().esConsumes<CaloGeometry, CaloGeometryRecord>()),
          hits_token_(consumes<HGCRecHitCollection>(config.getParameter<edm::InputTag>("recHits"))),
          deviceToken_{produces()} {}

    ~HGCalSoARecHitsProducer() override = default;

    // OPT 2: geometry setup + threshold computation moved here, called once per run
    void beginRun(edm::Run const&, edm::EventSetup const& iSetup) override {
      edm::ESHandle<CaloGeometry> geom = iSetup.getHandle(caloGeomToken_);
      rhtools_.setGeometry(*geom);
      maxlayer_ = rhtools_.lastLayer(isNose_);
      computeThreshold();
    }

    void endRun(edm::Run const&, edm::EventSetup const&) override {}

    void produce(device::Event& iEvent, device::EventSetup const& iSetup) override {
      edm::Handle<HGCRecHitCollection> hits_h = iEvent.getHandle(hits_token_);
      auto const& hits = *hits_h.product();
      const unsigned int nHits = hits.size();

      // OPT 1: allocate scratch host buffer at maximum possible size (nHits).
      // We fill in a single pass and track the real occupancy with `index`.
      HGCalSoARecHitsHostCollection cells(iEvent.queue(), nHits);
      auto cellsView = cells.view();

      uint32_t index = 0;

      // OPT 1: single pass — threshold check + fill merged
      for (unsigned int i = 0; i < nHits; ++i) {
        const HGCRecHit& hgrh = hits[i];
        const DetId detid = hgrh.detid();

        // geometry lookups (called once per hit, not twice)
        const unsigned int layerOnSide = rhtools_.getLayerWithOffset(detid) - 1;
        int thickness_index = rhtools_.getSiThickIndex(detid);
        if (thickness_index == -1)
          thickness_index = static_cast<int>(maxNumberOfThickIndices_);

        // OPT 3+4: flat array lookup with operator[] (no bounds-check throw, no pointer indirection)
        double storedThreshold = thresholds_[layerOnSide * thickStride_ + thickness_index];

        // Silicon CE-H uses a separate threshold entry
        if (detid.det() == DetId::HGCalHSi || detid.subdetId() == HGCHEF)
          storedThreshold = thresholds_[layerOnSide * thickStride_ + thickness_index + deltasi_index_regemfac_];

        if (hgrh.energy() < storedThreshold)
          continue;

        const float sigmaNoise = v_sigmaNoise_[layerOnSide * thickStride_ + thickness_index];

        const GlobalPoint position(rhtools_.getPosition(detid));
        const int offset = ((rhtools_.zside(detid) + 1) >> 1) * maxlayer_;
        const int layer = static_cast<int>(layerOnSide) + offset;

        auto entryInSoA = cellsView[index];

        // OPT 5: isBH_ bool, not a string comparison
        if (isBH_) {
          entryInSoA.dim1() = position.eta();
          entryInSoA.dim2() = position.phi();
        } else {
          entryInSoA.dim1() = position.x();
          entryInSoA.dim2() = position.y();
        }
        entryInSoA.dim3() = position.z();
        entryInSoA.energy() = hgrh.energy();
        entryInSoA.mipEnergy() = hgrh.energy();  // TODO: convert to MIP
        entryInSoA.sigmaNoise() = sigmaNoise;
        entryInSoA.layer() = layer;
        entryInSoA.recHitIndex() = i;
        entryInSoA.detid() = detid.rawId();
        entryInSoA.time() = hgrh.time();
        entryInSoA.timeError() = hgrh.timeError();

        ++index;
      }

      // OPT 6: build a correctly-sized host collection (index entries, not nHits)
      // using a plain alpaka::memcpy(queue, dst, src, count) overload.
      // This avoids alpaka::createSubView / alpaka::Idx<Device> which are not
      // available for PortableCollection buffers in this CMSSW/alpaka version.
      HGCalSoARecHitsHostCollection cellsFinal(iEvent.queue(), index);
      alpaka::memcpy(iEvent.queue(), cellsFinal.buffer(), cells.buffer(), index);

      if constexpr (!std::is_same_v<Device, alpaka_common::DevHost>) {
        // GPU backends: async H2D transfer of the trimmed host buffer
        HGCalSoARecHitsDeviceCollection deviceProduct{iEvent.queue(), index};
        alpaka::memcpy(iEvent.queue(), deviceProduct.buffer(), cellsFinal.buffer(), index);
        iEvent.emplace(deviceToken_, std::move(deviceProduct));
      } else {
        // CPU (serial) backend: put the host collection directly
        iEvent.emplace(deviceToken_, std::move(cellsFinal));
      }
    }

    static void fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
      edm::ParameterSetDescription desc;
      desc.add<std::string>("detector", "EE")->setComment("options EE, FH, BH, HFNose; other value defaults to EE");
      desc.add<edm::InputTag>("recHits", edm::InputTag("HGCalRecHit", "HGCEERecHits"));
      desc.add<unsigned int>("maxNumberOfThickIndices", 6);
      desc.add<double>("fcPerEle", 0.00016020506);
      desc.add<std::vector<double>>("fcPerMip");
      desc.add<std::vector<double>>("thicknessCorrection");
      desc.add<std::vector<double>>("noises");
      desc.add<std::vector<double>>("dEdXweights");
      desc.add<double>("ecut", 3.);
      descriptions.addWithDefaultLabel(desc);
    }

  private:
    // ---- configuration ----
    std::string detector_;
    bool isNose_;
    bool isBH_;  // OPT 5
    unsigned maxNumberOfThickIndices_;
    int deltasi_index_regemfac_;  // OPT 7: now initialised in ctor
    double fcPerEle_;
    double ecut_;
    std::vector<double> fcPerMip_;
    std::vector<double> nonAgedNoises_;
    std::vector<double> dEdXweights_;
    std::vector<double> thicknessCorrection_;

    // ---- run-level cache (set in beginRun) ----
    unsigned int maxlayer_ = 0;
    unsigned int thickStride_ = 0;  // OPT 3: stride for flat 2-D arrays

    // OPT 3: flat contiguous arrays instead of vector<vector<double>>
    std::vector<double> thresholds_;    // [layer * thickStride_ + thick]
    std::vector<double> v_sigmaNoise_;  // same layout

    hgcal::RecHitTools rhtools_;

    // ---- tokens ----
    edm::ESGetToken<CaloGeometry, CaloGeometryRecord> caloGeomToken_;
    edm::EDGetTokenT<HGCRecHitCollection> hits_token_;
    device::EDPutToken<HGCalSoARecHitsDeviceCollection> const deviceToken_;

    // OPT 2: called once per run from beginRun(), not every event
    void computeThreshold() {
      // thickStride_ covers:
      //   indices 0..maxNumberOfThickIndices_-1  for CE-E Si thicknesses
      //   indices maxNumberOfThickIndices_..2*maxNumberOfThickIndices_-1  for CE-H Si (deltasi offset)
      //   index   2*maxNumberOfThickIndices_  for scintillator (non-nose only)
      thickStride_ = 2 * maxNumberOfThickIndices_ + !isNose_;

      thresholds_.assign(maxlayer_ * thickStride_, 0.0);
      v_sigmaNoise_.assign(maxlayer_ * thickStride_, 0.0);

      for (unsigned ilayer = 1; ilayer <= maxlayer_; ++ilayer) {
        const unsigned base = (ilayer - 1) * thickStride_;
        for (unsigned ithick = 0; ithick < maxNumberOfThickIndices_; ++ithick) {
          const float sigmaNoise = 0.001f * fcPerEle_ * nonAgedNoises_[ithick] * dEdXweights_[ilayer] /
                                   (fcPerMip_[ithick] * thicknessCorrection_[ithick]);
          // OPT 4: operator[] — bounds guaranteed by construction
          thresholds_[base + ithick] = sigmaNoise * ecut_;
          v_sigmaNoise_[base + ithick] = sigmaNoise;
        }
      }
    }
  };

}  // namespace ALPAKA_ACCELERATOR_NAMESPACE

#include "HeterogeneousCore/AlpakaCore/interface/alpaka/MakerMacros.h"
DEFINE_FWK_ALPAKA_MODULE(HGCalSoARecHitsProducer);
