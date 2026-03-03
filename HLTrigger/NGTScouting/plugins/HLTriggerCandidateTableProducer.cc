// HLTriggerCandidateTableProducer.cc (Filtered Version)
#include <vector>
#include <string>
#include <map>

#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/NanoAOD/interface/FlatTable.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"

class HLTriggerCandidateTableProducer : public edm::stream::EDProducer<> {
public:
  explicit HLTriggerCandidateTableProducer(const edm::ParameterSet& cfg);
private:
  void produce(edm::Event&, const edm::EventSetup&) override;

  const edm::EDGetTokenT<trigger::TriggerEvent> triggerSummaryToken_;
  const std::string processName_;
  const std::string trigCandsName_;

  // Structure to hold user configuration
  struct PathSelector {
    std::string pathName;
    std::string filterLabel; // If empty, we will find the last filter automatically
  };
  std::vector<PathSelector> selectors_;

  mutable HLTConfigProvider hltConfig_;
};

HLTriggerCandidateTableProducer::HLTriggerCandidateTableProducer(const edm::ParameterSet& cfg)
    : triggerSummaryToken_(consumes<trigger::TriggerEvent>(cfg.getParameter<edm::InputTag>("triggerSummary"))),
      processName_(cfg.getParameter<std::string>("processName")),
      trigCandsName_(cfg.getParameter<std::string>("trigCandsName")) {
  
  auto selPSets = cfg.getParameter<std::vector<edm::ParameterSet>>("selection");
  for (const auto& pset : selPSets) {
    selectors_.push_back({
        pset.getParameter<std::string>("path"),
        pset.getUntrackedParameter<std::string>("filter", "")
    });
  }
  produces<nanoaod::FlatTable>();
}

void HLTriggerCandidateTableProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {
  bool changed = true;
  if (!hltConfig_.init(iEvent.getRun(), iSetup, processName_, changed)){
    edm::LogWarning("HLTriggerCandidateTableProducer") << "HLT configuration changed";
    return;
  }

  edm::Handle<trigger::TriggerEvent> triggerObj;
  iEvent.getByToken(triggerSummaryToken_, triggerObj);
  if (!triggerObj.isValid()){
    edm::LogWarning("HLTriggerCandidateTableProducer") << "Trigger object handle is not valid!";
    return;
  }

  std::vector<float> pt, eta, phi, mass;
  std::vector<int> pathIdx;

  const trigger::TriggerObjectCollection& toc = triggerObj->getObjects();

  for (size_t i = 0; i < selectors_.size(); ++i) {
    const auto& sel = selectors_[i];
    std::string targetFilter = sel.filterLabel;

    // If no filter specified, find the last filter in the path
    if (targetFilter.empty()) {
      const auto& modules = hltConfig_.moduleLabels(sel.pathName);
      for (int im = modules.size() - 1; im >= 0; --im) {
        if (hltConfig_.moduleEDMType(modules[im]) == "EDFilter" && hltConfig_.saveTags(modules[im])) {
          targetFilter = modules[im];
          break;
        }
      }
    }

    int fIdx = triggerObj->filterIndex(edm::InputTag(targetFilter, "", processName_).encode());
    if (fIdx < triggerObj->sizeFilters()) {
      const trigger::Keys& keys = triggerObj->filterKeys(fIdx);
      for (const auto& k : keys) {
        pt.push_back(toc[k].pt());
        eta.push_back(toc[k].eta());
        phi.push_back(toc[k].phi());
        mass.push_back(toc[k].mass());
        pathIdx.push_back(i); // Save the index of the path in your config list
      }
    } else {
      edm::LogWarning("HLTriggerCandidateTableProducer") << "fIdx: " << fIdx << " < triggerObj->sizeFilters(): " << triggerObj->sizeFilters();
    }
  }

  auto table = std::make_unique<nanoaod::FlatTable>(pt.size(), trigCandsName_, true);
  table->addColumn<float>("pt", pt, "pt", 10);
  table->addColumn<float>("eta", eta, "eta", 10);
  table->addColumn<float>("phi", phi, "phi", 10);
  table->addColumn<float>("mass", mass, "mass", 10);
  table->addColumn<int>("selIdx", pathIdx, "Index in the selection list");
  iEvent.put(std::move(table));
}

DEFINE_FWK_MODULE(HLTriggerCandidateTableProducer);
