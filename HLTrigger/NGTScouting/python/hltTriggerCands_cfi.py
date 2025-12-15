import FWCore.ParameterSet.Config as cms

hltTriggerCandsTable = cms.EDProducer("TriggerCandTableProducer",
                                      triggerSummary = cms.InputTag("hltTriggerSummaryAOD","", "HLT"),
                                      processName = cms.string("HLT"),
                                      trigCandsName = cms.string("hltP4s"),
                                      keepAllFilters = cms.untracked.bool(False)
                                      )
