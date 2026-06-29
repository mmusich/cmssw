// Generalised Phase-2 GT filter, modelled after HLTL1TSeed.
// Replaces the tau-only HLTP2GTTauFilter with support for all
// l1t::P2GTCandidate::ObjectType values.

#include "HLTrigger/HLTcore/interface/HLTFilter.h"
#include "DataFormats/L1Trigger/interface/P2GTCandidate.h"
#include "DataFormats/L1Trigger/interface/P2GTAlgoBlock.h"
#include "DataFormats/HLTReco/interface/TriggerFilterObjectWithRefs.h"
#include "DataFormats/HLTReco/interface/TriggerTypeDefs.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/ParameterSet/interface/ParameterSetDescription.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include <map>
#include <string>
#include <vector>

// ---------------------------------------------------------------------------
// Helper: map every P2GTCandidate ObjectType to the corresponding HLT
// trigger-object type used when storing refs in TriggerFilterObjectWithRefs.
// ---------------------------------------------------------------------------
namespace {
  trigger::TriggerObjectType triggerTypeForP2GT(l1t::P2GTCandidate::ObjectType ot) {
    using OT = l1t::P2GTCandidate::ObjectType;
    switch (ot) {
      // GCT objects
      case OT::GCTNonIsoEg:
        return trigger::TriggerL1NoIsoEG;
      case OT::GCTIsoEg:
        return trigger::TriggerL1IsoEG;
      case OT::GCTJets:
        return trigger::TriggerL1Jet;
      case OT::GCTTaus:
        return trigger::TriggerTau;
      case OT::GCTHtSum:
        return trigger::TriggerL1HTT;
      case OT::GCTEtSum:
        return trigger::TriggerL1ETT;
      // GMT muon objects
      case OT::GMTSaPromptMuons:
        return trigger::TriggerL1Mu;
      case OT::GMTSaDisplacedMuons:
        return trigger::TriggerL1Mu;
      case OT::GMTTkMuons:
        return trigger::TriggerL1Mu;
      case OT::GMTTopo:
        return trigger::TriggerL1Mu;
      // GTT objects
      case OT::GTTPromptJets:
        return trigger::TriggerL1Jet;
      case OT::GTTDisplacedJets:
        return trigger::TriggerL1Jet;
      case OT::GTTPhiCandidates:
        return trigger::TriggerL1Jet;
      case OT::GTTRhoCandidates:
        return trigger::TriggerL1Jet;
      case OT::GTTBsCandidates:
        return trigger::TriggerL1Jet;
      case OT::GTTHadronicTaus:
        return trigger::TriggerTau;
      case OT::GTTPromptTracks:
        return trigger::TriggerTrack;
      case OT::GTTDisplacedTracks:
        return trigger::TriggerTrack;
      case OT::GTTPrimaryVert:
        return trigger::TriggerL1Vertex;
      case OT::GTTPromptHtSum:
        return trigger::TriggerL1HTT;
      case OT::GTTDisplacedHtSum:
        return trigger::TriggerL1HTT;
      case OT::GTTEtSum:
        return trigger::TriggerL1ETT;
      // CL2 objects
      case OT::CL2JetsSC4:
        return trigger::TriggerL1CenJet;
      case OT::CL2JetsSC8:
        return trigger::TriggerL1CenJet;
      case OT::CL2Taus:
        return trigger::TriggerL1Tau;
      case OT::CL2Electrons:
        return trigger::TriggerL1EG;
      case OT::CL2Photons:
        return trigger::TriggerL1EG;
      case OT::CL2HtSum:
        return trigger::TriggerL1HTT;
      case OT::CL2EtSum:
        return trigger::TriggerL1ETT;
      default:
        return trigger::TriggerCluster;
    }
  }

  // Human-readable name for log messages.
  const char* objectTypeName(l1t::P2GTCandidate::ObjectType ot) {
    using OT = l1t::P2GTCandidate::ObjectType;
    switch (ot) {
      case OT::GCTNonIsoEg:
        return "GCTNonIsoEg";
      case OT::GCTIsoEg:
        return "GCTIsoEg";
      case OT::GCTJets:
        return "GCTJets";
      case OT::GCTTaus:
        return "GCTTaus";
      case OT::GCTHtSum:
        return "GCTHtSum";
      case OT::GCTEtSum:
        return "GCTEtSum";
      case OT::GMTSaPromptMuons:
        return "GMTSaPromptMuons";
      case OT::GMTSaDisplacedMuons:
        return "GMTSaDisplacedMuons";
      case OT::GMTTkMuons:
        return "GMTTkMuons";
      case OT::GMTTopo:
        return "GMTTopo";
      case OT::GTTPromptJets:
        return "GTTPromptJets";
      case OT::GTTDisplacedJets:
        return "GTTDisplacedJets";
      case OT::GTTPhiCandidates:
        return "GTTPhiCandidates";
      case OT::GTTRhoCandidates:
        return "GTTRhoCandidates";
      case OT::GTTBsCandidates:
        return "GTTBsCandidates";
      case OT::GTTHadronicTaus:
        return "GTTHadronicTaus";
      case OT::GTTPromptTracks:
        return "GTTPromptTracks";
      case OT::GTTDisplacedTracks:
        return "GTTDisplacedTracks";
      case OT::GTTPrimaryVert:
        return "GTTPrimaryVert";
      case OT::GTTPromptHtSum:
        return "GTTPromptHtSum";
      case OT::GTTDisplacedHtSum:
        return "GTTDisplacedHtSum";
      case OT::GTTEtSum:
        return "GTTEtSum";
      case OT::CL2JetsSC4:
        return "CL2JetsSC4";
      case OT::CL2JetsSC8:
        return "CL2JetsSC8";
      case OT::CL2Taus:
        return "CL2Taus";
      case OT::CL2Electrons:
        return "CL2Electrons";
      case OT::CL2Photons:
        return "CL2Photons";
      case OT::CL2HtSum:
        return "CL2HtSum";
      case OT::CL2EtSum:
        return "CL2EtSum";
      default:
        return "Unknown";
    }
  }

  // Parse a string like "CL2Taus" into the enum value.
  // Throws cms::Exception on unknown names.
  l1t::P2GTCandidate::ObjectType parseObjectType(const std::string& name) {
    using OT = l1t::P2GTCandidate::ObjectType;
    static const std::map<std::string, OT> table = {
        {"GCTNonIsoEg", OT::GCTNonIsoEg},
        {"GCTIsoEg", OT::GCTIsoEg},
        {"GCTJets", OT::GCTJets},
        {"GCTTaus", OT::GCTTaus},
        {"GCTHtSum", OT::GCTHtSum},
        {"GCTEtSum", OT::GCTEtSum},
        {"GMTSaPromptMuons", OT::GMTSaPromptMuons},
        {"GMTSaDisplacedMuons", OT::GMTSaDisplacedMuons},
        {"GMTTkMuons", OT::GMTTkMuons},
        {"GMTTopo", OT::GMTTopo},
        {"GTTPromptJets", OT::GTTPromptJets},
        {"GTTDisplacedJets", OT::GTTDisplacedJets},
        {"GTTPhiCandidates", OT::GTTPhiCandidates},
        {"GTTRhoCandidates", OT::GTTRhoCandidates},
        {"GTTBsCandidates", OT::GTTBsCandidates},
        {"GTTHadronicTaus", OT::GTTHadronicTaus},
        {"GTTPromptTracks", OT::GTTPromptTracks},
        {"GTTDisplacedTracks", OT::GTTDisplacedTracks},
        {"GTTPrimaryVert", OT::GTTPrimaryVert},
        {"GTTPromptHtSum", OT::GTTPromptHtSum},
        {"GTTDisplacedHtSum", OT::GTTDisplacedHtSum},
        {"GTTEtSum", OT::GTTEtSum},
        {"CL2JetsSC4", OT::CL2JetsSC4},
        {"CL2JetsSC8", OT::CL2JetsSC8},
        {"CL2Taus", OT::CL2Taus},
        {"CL2Electrons", OT::CL2Electrons},
        {"CL2Photons", OT::CL2Photons},
        {"CL2HtSum", OT::CL2HtSum},
        {"CL2EtSum", OT::CL2EtSum},
    };
    auto it = table.find(name);
    if (it == table.end())
      throw cms::Exception("Configuration") << "HLTP2GTFilter: unknown P2GT object type \"" << name << "\"";
    return it->second;
  }
}  // namespace

// ---------------------------------------------------------------------------
// Filter class
// ---------------------------------------------------------------------------
class HLTP2GTFilter : public HLTFilter {
public:
  explicit HLTP2GTFilter(const edm::ParameterSet&);
  static void fillDescriptions(edm::ConfigurationDescriptions&);
  bool hltFilter(edm::Event&, const edm::EventSetup&, trigger::TriggerFilterObjectWithRefs&) const override;

private:
  const edm::InputTag m_l1GTAlgoBlockTag;
  const edm::EDGetTokenT<l1t::P2GTAlgoBlockMap> m_algoBlockToken;

  // Per-algo configuration: which algo names to seed from, which object
  // type(s) to accept, and optional kinematic cuts.
  struct AlgoConfig {
    std::string algoName;
    l1t::P2GTCandidate::ObjectType objectType;
    double minPt;
    double maxAbsEta;
  };

  std::vector<AlgoConfig> m_algoConfigs;
  unsigned int m_minN;  // minimum total number of accepted objects
};

// ---------------------------------------------------------------------------
// Constructor
// ---------------------------------------------------------------------------
HLTP2GTFilter::HLTP2GTFilter(const edm::ParameterSet& iConfig)
    : HLTFilter(iConfig),
      m_l1GTAlgoBlockTag(iConfig.getParameter<edm::InputTag>("l1GTAlgoBlockTag")),
      m_algoBlockToken(consumes<l1t::P2GTAlgoBlockMap>(m_l1GTAlgoBlockTag)),
      m_minN(iConfig.getParameter<unsigned int>("minN")) {
  const auto& algos = iConfig.getParameter<std::vector<edm::ParameterSet>>("l1GTAlgos");
  m_algoConfigs.reserve(algos.size());
  for (const auto& ps : algos) {
    AlgoConfig cfg;
    cfg.algoName = ps.getParameter<std::string>("name");
    cfg.objectType = parseObjectType(ps.getParameter<std::string>("objectType"));
    cfg.minPt = ps.getParameter<double>("minPt");
    cfg.maxAbsEta = ps.getParameter<double>("maxAbsEta");
    m_algoConfigs.push_back(std::move(cfg));
  }
}

// ---------------------------------------------------------------------------
// fillDescriptions
// ---------------------------------------------------------------------------
void HLTP2GTFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  makeHLTFilterDescription(desc);

  desc.add<edm::InputTag>("l1GTAlgoBlockTag", edm::InputTag(""));
  desc.add<unsigned int>("minN", 1);

  // Each element of l1GTAlgos describes one (algo, objectType, cuts) triplet.
  edm::ParameterSetDescription algoDesc;
  algoDesc.add<std::string>("name", "");
  algoDesc.add<std::string>("objectType", "CL2Taus");
  algoDesc.add<double>("minPt", 0.0);
  algoDesc.add<double>("maxAbsEta", 1e99);
  desc.addVPSet("l1GTAlgos", algoDesc, {});

  descriptions.add("HLTP2GTFilter", desc);
}

// ---------------------------------------------------------------------------
// hltFilter
// ---------------------------------------------------------------------------
bool HLTP2GTFilter::hltFilter(edm::Event& iEvent,
                              const edm::EventSetup& /*iSetup*/,
                              trigger::TriggerFilterObjectWithRefs& filterproduct) const {
  if (saveTags())
    filterproduct.addCollectionTag(m_l1GTAlgoBlockTag);

  if (m_l1GTAlgoBlockTag.isUninitialized() || m_algoConfigs.empty())
    return false;

  const l1t::P2GTAlgoBlockMap& algos = iEvent.get(m_algoBlockToken);

  std::vector<l1t::P2GTCandidateRef> accepted;

  for (const auto& cfg : m_algoConfigs) {
    auto it = algos.find(cfg.algoName);
    if (it == algos.end())
      continue;
    if (!it->second.decisionBeforeBxMaskAndPrescale())
      continue;

    const l1t::P2GTCandidateVectorRef& objects = it->second.trigObjects();
    for (const l1t::P2GTCandidateRef& obj : objects) {
      if (obj->objectType() != cfg.objectType)
        continue;
      if (obj->pt() < cfg.minPt)
        continue;
      if (std::abs(obj->eta()) > cfg.maxAbsEta)
        continue;
      accepted.push_back(obj);
    }
  }

  // Register collection tags from accepted refs (same pattern as original).
  if (saveTags()) {
    edm::InputTag tagOld;
    for (const auto& cand : accepted) {
      const edm::ProductID pid(cand.id());
      const auto& prov = iEvent.getStableProvenance(pid);
      edm::InputTag tagNew(prov.moduleLabel(), prov.productInstanceName(), prov.processName());
      if (tagNew.encode() != tagOld.encode()) {
        filterproduct.addCollectionTag(tagNew);
        tagOld = tagNew;
      }
    }
  }

  // Store objects in the filter product with the appropriate trigger type.
  for (const auto& cand : accepted) {
    const trigger::TriggerObjectType ttype = triggerTypeForP2GT(cand->objectType());
    LogDebug("HLTP2GTFilter") << "Adding " << objectTypeName(cand->objectType()) << " pt=" << cand->pt()
                              << " eta=" << cand->eta() << " as trigger type " << ttype;
    filterproduct.addObject(ttype, cand);
  }

  return accepted.size() >= m_minN;
}

DEFINE_FWK_MODULE(HLTP2GTFilter);
