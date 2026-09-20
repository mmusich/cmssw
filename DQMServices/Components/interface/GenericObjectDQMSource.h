#ifndef DQMServices_Components_interface_GenericObjectDQMSource_h
#define DQMServices_Components_interface_GenericObjectDQMSource_h

#include "DQMServices/Core/interface/DQMEDAnalyzer.h"
#include "DQMServices/Core/interface/DQMStore.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/ParameterSetDescription.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"
#include "DQMServices/Components/interface/DQMVariable.h"
#include "DQMServices/Components/interface/DQMVectorVariable.h"
#include "DQMServices/Components/interface/DQMEtaPhiMapVariable.h"

#include <cstddef>
#include <string>
#include <type_traits>
#include <vector>

// Trait template supplying the list of plottable variables for object type T.
// Must be specialized per type before GenericObjectDQMSource<T> is instantiated,
// e.g. see TrackDQMVariables.h for the reco::Track specialization.
//
// A specialization only needs `variables()` (scalar members). It may
// additionally define:
//  - `vectorVariables()` -> std::vector<DQMVectorVariable<T>> for
//    vector-valued members (e.g. Run3ScoutingElectron::trkpt())
//  - `etaPhiMapVariables()` -> std::vector<DQMEtaPhiMapVariable<T>> for a
//    detId-driven eta/phi occupancy map (e.g. calorimeter recHit types)
// Both are entirely optional and detected automatically, so existing
// specializations that don't need them are unaffected.
template <typename T>
struct DQMVariableTraits;

namespace dqmgeneric_detail {
  template <typename T, typename = void>
  struct has_vector_variables : std::false_type {};

  template <typename T>
  struct has_vector_variables<T, std::void_t<decltype(DQMVariableTraits<T>::vectorVariables())>> : std::true_type {};

  template <typename T, typename = void>
  struct has_etaphi_variables : std::false_type {};

  template <typename T>
  struct has_etaphi_variables<T, std::void_t<decltype(DQMVariableTraits<T>::etaPhiMapVariables())>> : std::true_type {};
}  // namespace dqmgeneric_detail

// Generic DQM source: books and fills one 1D histogram per DQMVariable<T>
// (as supplied by DQMVariableTraits<T>::variables()) for every object in an
// input collection of type Collection (default std::vector<T>, matching the
// usual reco::*Collection typedefs). If DQMVariableTraits<T> also defines
// vectorVariables(), one additional histogram per DQMVectorVariable<T> is
// booked and filled once per element on every event. If it defines
// etaPhiMapVariables(), one TH2F per DQMEtaPhiMapVariable<T> is booked and
// filled once per detId, using CaloGeometry to convert each detId to eta/phi.
//
// Adding a plot for a new member of T means adding one line to the trait
// specialization's variable list -- this class itself never changes.
template <typename T, typename Collection = std::vector<T>>
class GenericObjectDQMSource : public DQMEDAnalyzer {
public:
  explicit GenericObjectDQMSource(edm::ParameterSet const& iConfig)
      : token_(consumes<Collection>(iConfig.getParameter<edm::InputTag>("src"))),
        folder_(iConfig.getParameter<std::string>("folder")),
        variables_(DQMVariableTraits<T>::variables()) {
    if constexpr (dqmgeneric_detail::has_vector_variables<T>::value) {
      vectorVariables_ = DQMVariableTraits<T>::vectorVariables();
    }
    if constexpr (dqmgeneric_detail::has_etaphi_variables<T>::value) {
      etaPhiVariables_ = DQMVariableTraits<T>::etaPhiMapVariables();
      geomToken_ = esConsumes<CaloGeometry, CaloGeometryRecord>();
    }
  }

  ~GenericObjectDQMSource() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
    edm::ParameterSetDescription desc;
    desc.add<edm::InputTag>("src");
    desc.add<std::string>("folder");
    descriptions.addDefault(desc);
  }

  void bookHistograms(DQMStore::IBooker& ibooker, edm::Run const&, edm::EventSetup const&) override {
    ibooker.setCurrentFolder(folder_);

    histos_.clear();
    histos_.reserve(variables_.size());
    for (auto const& var : variables_) {
      histos_.push_back(
          ibooker.book1D(var.name, var.title + ";" + var.title + ";Entries", var.nbins, var.xmin, var.xmax));
    }

    vectorHistos_.clear();
    vectorHistos_.reserve(vectorVariables_.size());
    for (auto const& var : vectorVariables_) {
      vectorHistos_.push_back(
          ibooker.book1D(var.name, var.title + ";" + var.title + ";Entries", var.nbins, var.xmin, var.xmax));
    }

    etaPhiHistos_.clear();
    etaPhiHistos_.reserve(etaPhiVariables_.size());
    for (auto const& var : etaPhiVariables_) {
      etaPhiHistos_.push_back(ibooker.book2D(var.name,
                                             var.title + ";#eta;#phi",
                                             var.nbinsEta,
                                             var.etaMin,
                                             var.etaMax,
                                             var.nbinsPhi,
                                             var.phiMin,
                                             var.phiMax));
    }
  }

  void analyze(edm::Event const& iEvent, edm::EventSetup const& iSetup) override {
    edm::Handle<Collection> handle;
    iEvent.getByToken(token_, handle);
    if (!handle.isValid())
      return;

    CaloGeometry const* geometry = nullptr;
    if constexpr (dqmgeneric_detail::has_etaphi_variables<T>::value) {
      if (!etaPhiVariables_.empty()) {
        geometry = &iSetup.getData(geomToken_);
      }
    }

    for (auto const& obj : *handle) {
      for (std::size_t i = 0; i < variables_.size(); ++i) {
        histos_[i]->Fill(variables_[i].accessor(obj));
      }
      for (std::size_t i = 0; i < vectorVariables_.size(); ++i) {
        for (double value : vectorVariables_[i].accessor(obj)) {
          vectorHistos_[i]->Fill(value);
        }
      }
      if constexpr (dqmgeneric_detail::has_etaphi_variables<T>::value) {
        for (std::size_t i = 0; i < etaPhiVariables_.size(); ++i) {
          for (uint32_t rawId : etaPhiVariables_[i].detIdAccessor(obj)) {
            auto cellGeometry = geometry->getGeometry(DetId(rawId));
            if (cellGeometry) {
              auto const& pos = cellGeometry->getPosition();
              etaPhiHistos_[i]->Fill(pos.eta(), pos.phi());
            }
          }
        }
      }
    }
  }

private:
  edm::EDGetTokenT<Collection> token_;
  std::string folder_;
  std::vector<DQMVariable<T>> variables_;
  std::vector<MonitorElement*> histos_;
  std::vector<DQMVectorVariable<T>> vectorVariables_;
  std::vector<MonitorElement*> vectorHistos_;
  std::vector<DQMEtaPhiMapVariable<T>> etaPhiVariables_;
  std::vector<MonitorElement*> etaPhiHistos_;
  edm::ESGetToken<CaloGeometry, CaloGeometryRecord> geomToken_;
};

#endif
