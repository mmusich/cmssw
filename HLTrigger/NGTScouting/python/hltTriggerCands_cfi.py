import FWCore.ParameterSet.Config as cms

hltTriggerCands = cms.EDProducer("HLTTriggerCandidatesTableProducer",
    triggerSummary = cms.InputTag("hltTriggerSummaryAOD","", "HLT"),
    triggerResults = cms.InputTag("TriggerResults", "", "HLT"),
    processName = cms.string("HLT"),
    keepAllFilters = cms.untracked.bool(False)
)
