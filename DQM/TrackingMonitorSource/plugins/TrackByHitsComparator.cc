// system includes
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cmath>

// user includes
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DQMServices/Core/interface/DQMEDAnalyzer.h"
#include "DQMServices/Core/interface/DQMStore.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackingRecHit/interface/TrackingRecHit.h"

class TrackByHitsComparator : public DQMEDAnalyzer {

public:
  explicit TrackByHitsComparator(const edm::ParameterSet&);
  ~TrackByHitsComparator() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions&);

protected:
  void bookHistograms(DQMStore::IBooker&,
                      edm::Run const&,
                      edm::EventSetup const&) override;

  void analyze(edm::Event const&,
               edm::EventSetup const&) override;

private:
  void extractDetIds(const reco::Track&, std::vector<uint32_t>&);

  edm::EDGetTokenT<reco::TrackCollection> tracksAToken_;
  edm::EDGetTokenT<reco::TrackCollection> tracksBToken_;

  double minSharedFraction_;
  std::string folder_;

  MonitorElement* h_dpt_;
  MonitorElement* h_sharedFraction_;

  // ---- Reused per stream
  std::vector<uint32_t> detidsA_;
  std::vector<std::vector<uint32_t>> detidsB_;

  std::unordered_map<uint32_t, std::vector<unsigned int>> detIdToB_;

  std::vector<uint16_t> matchCounts_;
  std::vector<unsigned int> touched_;
};

TrackByHitsComparator::TrackByHitsComparator(
    const edm::ParameterSet& iConfig)
    : tracksAToken_(consumes<reco::TrackCollection>(
          iConfig.getParameter<edm::InputTag>("tracksA"))),
      tracksBToken_(consumes<reco::TrackCollection>(
          iConfig.getParameter<edm::InputTag>("tracksB"))),
      minSharedFraction_(iConfig.getParameter<double>("minSharedFraction")),
      folder_(iConfig.getParameter<std::string>("folder")),
      h_dpt_(nullptr),
      h_sharedFraction_(nullptr) {}

void TrackByHitsComparator::bookHistograms(
    DQMStore::IBooker& ibooker,
    edm::Run const&,
    edm::EventSetup const&) {

  ibooker.setCurrentFolder(folder_);
  h_dpt_ = ibooker.book1D("dpt", "(pT_A - pT_B)/pT_B", 100, -0.5, 0.5);
  h_sharedFraction_ =
      ibooker.book1D("sharedFraction", "Shared hit fraction", 100, 0., 1.1);
}

void TrackByHitsComparator::extractDetIds(
    const reco::Track& trk,
    std::vector<uint32_t>& buffer) {

  buffer.clear();
  buffer.reserve(trk.recHitsSize());

  for (auto const& hit : trk.recHits()) {
    if (!hit->isValid()) continue;
    buffer.push_back(hit->geographicalId().rawId());
  }

  std::sort(buffer.begin(), buffer.end());
  buffer.erase(std::unique(buffer.begin(), buffer.end()), buffer.end());
}

void TrackByHitsComparator::analyze(
    edm::Event const& iEvent,
    edm::EventSetup const&) {

  auto const& tracksA = iEvent.get(tracksAToken_);
  auto const& tracksB = iEvent.get(tracksBToken_);

  const unsigned int nB = tracksB.size();
  if (tracksA.empty() || nB == 0) return;

  // ---- Resize per event buffers once
  detidsB_.resize(nB);
  matchCounts_.assign(nB, 0);
  touched_.clear();
  detIdToB_.clear();
  detIdToB_.reserve(nB * 8);  // good heuristic for PU200

  // ---- Precompute B detids + index
  for (unsigned int iB = 0; iB < nB; ++iB) {
    extractDetIds(tracksB[iB], detidsB_[iB]);

    for (auto detid : detidsB_[iB]) {
      detIdToB_[detid].push_back(iB);
    }
  }

  // ---- Loop over A tracks
  for (unsigned int iA = 0; iA < tracksA.size(); ++iA) {

    extractDetIds(tracksA[iA], detidsA_);
    if (detidsA_.empty()) continue;

    const unsigned int required =
        std::ceil(minSharedFraction_ * detidsA_.size());

    // Count matches via DetId index
    for (auto detid : detidsA_) {

      auto it = detIdToB_.find(detid);
      if (it == detIdToB_.end()) continue;

      for (auto idxB : it->second) {

        if (matchCounts_[idxB] == 0)
          touched_.push_back(idxB);

        ++matchCounts_[idxB];
      }
    }

    // Find best match among touched only
    unsigned int bestIdx = nB;
    uint16_t bestCount = 0;

    for (auto idxB : touched_) {
      if (matchCounts_[idxB] > bestCount) {
        bestCount = matchCounts_[idxB];
        bestIdx = idxB;
      }
    }

    if (bestIdx < nB && bestCount >= required) {

      double frac =
          double(bestCount) /
          std::min(detidsA_.size(),
                   detidsB_[bestIdx].size());

      h_sharedFraction_->Fill(frac);

      double dpt =
          (tracksA[iA].pt() - tracksB[bestIdx].pt()) /
          tracksB[bestIdx].pt();

      h_dpt_->Fill(dpt);
    }

    // Reset only touched indices
    for (auto idxB : touched_)
      matchCounts_[idxB] = 0;

    touched_.clear();
  }
}

void TrackByHitsComparator::fillDescriptions(
    edm::ConfigurationDescriptions& descriptions) {

  edm::ParameterSetDescription desc;
  desc.add<edm::InputTag>("tracksA");
  desc.add<edm::InputTag>("tracksB");
  desc.add<double>("minSharedFraction", 0.75);
  desc.add<std::string>("folder", "Tracking/TrackComparisonPU200");
  descriptions.addWithDefaultLabel(desc);
}

DEFINE_FWK_MODULE(TrackByHitsComparator);
