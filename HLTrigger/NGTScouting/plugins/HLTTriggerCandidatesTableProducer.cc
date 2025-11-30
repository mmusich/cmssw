// HLTTriggerCandidatesTableProducer.cc
// Stores HLT trigger candidate four-momenta (pt,eta,phi,mass) in a nanoaod::FlatTable.
// One row per trigger candidate; column "path" indicates the HLT path that produced it.

// system includes
#include <vector>
#include <string>

// user includes
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/HLTReco/interface/TriggerObject.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/NanoAOD/interface/FlatTable.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"

class HLTTriggerCandidatesTableProducer : public edm::global::EDProducer<edm::BeginRunProducer> {
public:
  explicit HLTTriggerCandidatesTableProducer(const edm::ParameterSet& cfg);
  ~HLTTriggerCandidatesTableProducer() override = default;

  void globalBeginRunProduce(edm::Run& iRun, edm::EventSetup const& iSetup) const override;
  void produce(edm::StreamID, edm::Event& evt, const edm::EventSetup& es) const override;


private:
  const edm::InputTag triggerSummaryTag_;
  const edm::InputTag triggerResultsTag_;
  const std::string processName_;
  const bool keepAllFilters_;  // if true, try all modules in a path; if false, take last filter-like module

  // consumes tokens
  const edm::EDGetTokenT<trigger::TriggerEvent> triggerSummaryToken_;
  const edm::EDGetTokenT<edm::TriggerResults> triggerResultsToken_;

  // HLT config
  mutable HLTConfigProvider hltConfig_;
};

HLTTriggerCandidatesTableProducer::HLTTriggerCandidatesTableProducer(const edm::ParameterSet& cfg)
    : triggerSummaryTag_(cfg.getParameter<edm::InputTag>("triggerSummary")),
      triggerResultsTag_(cfg.getParameter<edm::InputTag>("triggerResults")),
      processName_(cfg.getParameter<std::string>("processName")),
      keepAllFilters_(cfg.getUntrackedParameter<bool>("keepAllFilters", false)),
      triggerSummaryToken_(consumes<trigger::TriggerEvent>(triggerSummaryTag_)),
      triggerResultsToken_(consumes<edm::TriggerResults>(triggerResultsTag_)) {
  produces<nanoaod::FlatTable>();
}

void HLTTriggerCandidatesTableProducer::globalBeginRunProduce(edm::Run& iRun, edm::EventSetup const& es) const {
  bool changed = true;

  if (!hltConfig_.init(iRun, es, processName_, changed)) {
    edm::LogWarning("HLTTriggerCandidatesTableProducer")
      << "HLTConfigProvider initialization failed for process '"
      << processName_ << "'";
    return;
  }
  
  if (changed) {
    edm::LogInfo("HLTTriggerCandidatesTableProducer")
      << "HLT menu for process '" << processName_
      << "' changed: " << hltConfig_.size() << " paths available.";
  }
}

void HLTTriggerCandidatesTableProducer::produce(edm::StreamID, edm::Event& evt, const edm::EventSetup& /*es*/) const {
  using namespace edm;
  using namespace trigger;

  // Get TriggerEvent (contains filter->keys and objects)
  Handle<TriggerEvent> triggerObj;
  evt.getByToken(triggerSummaryToken_, triggerObj);
  if (!triggerObj.isValid()) {
    edm::LogInfo("HLTTriggerCandidatesTableProducer") << "TriggerEvent not present in event; producing empty table.";
    auto empty = std::make_unique<nanoaod::FlatTable>(0, "hltTriggerCands", true);
    evt.put(std::move(empty));
    return;
  }
  const TriggerObjectCollection& toc = triggerObj->getObjects();

  // Get TriggerResults to know which paths fired
  Handle<TriggerResults> triggerResults;
  evt.getByToken(triggerResultsToken_, triggerResults);
  if (!triggerResults.isValid()) {
    edm::LogWarning("HLTTriggerCandidatesTableProducer") << "TriggerResults not found; producing empty table.";
    auto empty = std::make_unique<nanoaod::FlatTable>(0, "hltTriggerCands", true);
    evt.put(std::move(empty));
    return;
  }

  // Prepare vectors for table columns (one row per trigger candidate)
  std::vector<float> col_pt;
  std::vector<float> col_eta;
  std::vector<float> col_phi;
  std::vector<float> col_mass;
  std::vector<std::string> col_path;

  // iterate over HLT paths from the HLT config
  const std::vector<std::string>& paths = hltConfig_.triggerNames();
  for (size_t ip = 0; ip < paths.size(); ++ip) {
    // skip if path index out of range
    if (ip >= (size_t)triggerResults->size())
      continue;

    const bool accepted = triggerResults->accept(static_cast<int>(ip));
    if (!accepted)
      continue;  // only consider fired paths

    const std::string& pathName = paths[ip];
    // find a module label to query in TriggerEvent:
    // try the last module of the path that looks like a filter, falling back to the last module.
    std::string chosenFilterLabel;
    const std::vector<std::string>& modules = hltConfig_.moduleLabels(pathName);
    if (!modules.empty()) {
      if (keepAllFilters_) {
        // when keepAllFilters_ we will iterate over all modules; here choose last as fallback for consistency
        chosenFilterLabel = modules.back();
      } else {
        // pick the last module whose type contains "Filter" (common for filters producing trigger::TriggerEvent entries)
        for (int im = static_cast<int>(modules.size()) - 1; im >= 0; --im) {
          const std::string& mod = modules[im];
          std::string mtype = hltConfig_.moduleType(mod);
          if (mtype.find("Filter") != std::string::npos || mtype.find("Producer") != std::string::npos) {
            chosenFilterLabel = mod;
            break;
          }
        }
        if (chosenFilterLabel.empty())
          chosenFilterLabel = modules.back();
      }
    }

    // TriggerEvent filterTag expects encoded "module:instance:process" or at least the module label.
    // We must search for a filter with that label in triggerObj.
    // The filterTag stored in TriggerEvent is of type edm::InputTag (module:instance:process); TriggerEvent::filterTag(index).label() returns module label.
    int filterIndex = -1;
    for (size_t ifilt = 0; ifilt < triggerObj->sizeFilters(); ++ifilt) {
      std::string fullname = triggerObj->filterTag(ifilt).label();  // just label part
      if (fullname == chosenFilterLabel) {
        filterIndex = static_cast<int>(ifilt);
        break;
      }
    }

    if (filterIndex < 0) {
      // fallback: try using chosenFilterLabel encoded (module:instance:process)
      edm::InputTag guessed(chosenFilterLabel);
      int idx = triggerObj->filterIndex(guessed.encode());
      if (idx >= 0 && idx < static_cast<int>(triggerObj->sizeFilters()))
        filterIndex = idx;
    }

    if (filterIndex < 0) {
      // nothing found for this path; skip but log debug
      edm::LogWarning("HLTTriggerCandidatesTableProducer")
	<< "No filter found in TriggerEvent for path " << pathName << " (chosen module '" << chosenFilterLabel << "').";
      continue;
    }

    // get keys (indices into toc) for this filter and fill table rows
    const Keys& keys = triggerObj->filterKeys(filterIndex);
    for (const auto& ki : keys) {
      const TriggerObject& to = toc[ki];
      col_pt.push_back(to.pt());
      col_eta.push_back(to.eta());
      col_phi.push_back(to.phi());
      col_mass.push_back(to.mass());
      col_path.push_back(pathName);
    }
  }  // end path loop

  // Create flat table: rows = number of candidates
  const int nRows = static_cast<int>(col_pt.size());
  auto table = std::make_unique<nanoaod::FlatTable>(nRows, "hltTriggerCands", true);
  table->addColumn<float>("pt", col_pt, "candidate p_{T}", 10);
  table->addColumn<float>("eta", col_eta, "candidate eta", 10);
  table->addColumn<float>("phi", col_phi, "candidate phi", 10);
  table->addColumn<float>("mass", col_mass, "candidate mass", 10);
  //table->addColumn<std::string>("path", col_path, "HLT path name that produced the candidate");

  // put product into event
  evt.put(std::move(table));
}

// plugin registration
#include "FWCore/Framework/interface/ModuleFactory.h"
DEFINE_FWK_MODULE(HLTTriggerCandidatesTableProducer);
