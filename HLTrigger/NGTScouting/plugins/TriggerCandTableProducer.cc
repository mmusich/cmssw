// TriggerCandTableProducer.cc
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
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"

class TriggerCandTableProducer : public edm::stream::EDProducer<> {
public:
  explicit TriggerCandTableProducer(const edm::ParameterSet& cfg);
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void produce(edm::Event&, const edm::EventSetup&) override;

  const edm::InputTag triggerSummaryTag_;
  const std::string processName_;
  const std::string trigCandsName_;
  const bool keepAllFilters_;  // if true, try all modules in a path; if false, take last filter-like module

  // consumes tokens
  const edm::EDGetTokenT<trigger::TriggerEvent> triggerSummaryToken_;

  // HLT config
  mutable HLTConfigProvider hltConfig_;
};

TriggerCandTableProducer::TriggerCandTableProducer(const edm::ParameterSet& cfg)
    : triggerSummaryTag_(cfg.getParameter<edm::InputTag>("triggerSummary")),
      processName_(cfg.getParameter<std::string>("processName")),
      trigCandsName_(cfg.getParameter<std::string>("trigCandsName")),
      keepAllFilters_(cfg.getUntrackedParameter<bool>("keepAllFilters", false)),
      triggerSummaryToken_(consumes<trigger::TriggerEvent>(triggerSummaryTag_)) {
  produces<nanoaod::FlatTable>();
}

void TriggerCandTableProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;
  using namespace trigger;

  bool changed = true;
  if (!hltConfig_.init(iEvent.getRun(), iSetup, processName_, changed)) {
    edm::LogWarning("TriggerCandTableProducer")
        << "HLTConfigProvider initialization failed for process '" << processName_ << "'";
    return;
  }

  if (changed) {
    edm::LogInfo("TriggerCandTableProducer")
        << "HLT menu for process '" << processName_ << "' changed: " << hltConfig_.size() << " paths available.";
  }

  // Get TriggerEvent (contains filter->keys and objects)
  Handle<TriggerEvent> triggerObj;
  iEvent.getByToken(triggerSummaryToken_, triggerObj);
  if (!triggerObj.isValid()) {
    edm::LogInfo("TriggerCandTableProducer") << "TriggerEvent not present in event; producing empty table.";
    auto empty = std::make_unique<nanoaod::FlatTable>(0, "hltTriggerCands", true);
    iEvent.put(std::move(empty));
    return;
  }

  const TriggerObjectCollection& toc = triggerObj->getObjects();

  // Prepare vectors for table columns (one row per trigger candidate)
  const size_t nFilts = 100;
  static constexpr float default_value = std::numeric_limits<float>::quiet_NaN();

  std::vector<float> col_pt(nFilts, default_value);
  std::vector<float> col_eta(nFilts, default_value);
  std::vector<float> col_phi(nFilts, default_value);
  std::vector<float> col_mass(nFilts, default_value);

  // iterate over HLT paths from the HLT config
  const std::vector<std::string>& paths = hltConfig_.triggerNames();

  //std::cout << " LIST OF ALL PATHS " << std::endl;
  //for (const auto& path : paths) {
  //  if (!path.starts_with("HLT_"))
  //    continue;
  //  std::cout << "path name: " << path << std::endl;
  // }
  //std::cout << "===================" << std::endl;

  unsigned int countFilters{0};
  for (size_t ip = 0; ip < paths.size(); ++ip) {
    const std::string& pathName = paths[ip];
    if (!pathName.starts_with("HLT_"))
      continue;

    //std::cout << "path name: " << pathName << std::endl;

    // find a module label to query in TriggerEvent:
    // try the last module of the path that looks like a filter, falling back to the last module.
    std::string chosenFilterLabel;
    const std::vector<std::string>& modules = hltConfig_.moduleLabels(pathName);
    if (!modules.empty()) {
      if (keepAllFilters_) {
        // when keepAllFilters_ we will iterate over all modules; here choose last as fallback for consistency
        chosenFilterLabel = modules.front();
      } else {
        // pick the last module whose type contains "Filter" (common for filters producing trigger::TriggerEvent entries)
        for (int im = static_cast<int>(modules.size()) - 1; im >= 0; --im) {
          const std::string& mod = modules[im];
          std::string mtype = hltConfig_.moduleType(mod);
          std::string mEDMtype = hltConfig_.moduleEDMType(mod);
          bool isSaveTags = hltConfig_.saveTags(mod);

          //std::cout << "module: " << mod << " (moduleType= " << mtype << " , moduleEDMtype= " << mEDMtype
          //          << " , saveTags=" << isSaveTags << "  ) " << std::endl;

          if (mEDMtype.find("EDFilter") != std::string::npos && isSaveTags) {
            chosenFilterLabel = mod;
            break;
          }
        }
        if (chosenFilterLabel.empty())
          chosenFilterLabel = modules.back();
      }
    }
    //std::cout << "===================" << std::endl;

    // TriggerEvent filterTag expects encoded "module:instance:process" or at least the module label.
    // We must search for a filter with that label in triggerObj.
    // The filterTag stored in TriggerEvent is of type edm::InputTag (module:instance:process); TriggerEvent::filterTag(index).label() returns module label.
    int filterIndex = -1;
    for (size_t ifilt = 0; ifilt < triggerObj->sizeFilters(); ++ifilt) {
      std::string fullname = triggerObj->filterTag(ifilt).label();  // just label part
      //std::cout << "fullname: " << fullname << " chosenFilterLabel: " << chosenFilterLabel << std::endl;
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
      edm::LogWarning("TriggerCandTableProducer") << "No filter found in TriggerEvent for path " << pathName
                                                           << " (chosen module '" << chosenFilterLabel << "').";
      continue;
    }

    // get keys (indices into toc) for this filter and fill table rows
    const Keys& keys = triggerObj->filterKeys(filterIndex);
    for (const auto& ki : keys) {
      const TriggerObject& to = toc[ki];

      std::cout << "ki = " << ki << ", pt = " << to.pt() << ", eta = " << to.eta() << ", phi = " << to.phi()
                << ", mass = " << to.mass() << ", id = " << to.id() << ", path = " << pathName << std::endl;

      col_pt[countFilters] = to.pt();
      col_eta[countFilters] = to.eta();
      col_phi[countFilters] = to.phi();
      col_mass[countFilters] = to.mass();
    }
    countFilters++;
  }  // end path loop

  // Create flat table: rows = number of candidates
  const int nRows = static_cast<int>(col_pt.size());
  std::cout << "countedFilters: " << countFilters << " nRows: " << nRows << std::endl;

  assert(size_t(nRows) <= nFilts);

  auto trigTable = std::make_unique<nanoaod::FlatTable>(nFilts, trigCandsName_, true, false);
  trigTable->addColumn<float>("pt", col_pt, "candidate p_{T}", 10);
  trigTable->addColumn<float>("eta", col_eta, "candidate eta", 10);
  trigTable->addColumn<float>("phi", col_phi, "candidate phi", 10);
  trigTable->addColumn<float>("mass", col_mass, "candidate mass", 10);

  std::cout << "just before the put!" << std::endl;
    
  // put product into event
  iEvent.put(std::move(trigTable));

  std::cout << "just after the put!" << std::endl;
  
}

void TriggerCandTableProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<edm::InputTag>("triggerSummary");
  desc.add<std::string>("processName");
  desc.add<std::string>("trigCandsName")->setComment("name of the flat table ouput");
  desc.addUntracked<bool>("keepAllFilters", false);
  descriptions.addWithDefaultLabel(desc);
}

// plugin registration
#include "FWCore/Framework/interface/ModuleFactory.h"
DEFINE_FWK_MODULE(TriggerCandTableProducer);
