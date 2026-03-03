import FWCore.ParameterSet.Config as cms

hltTriggerCandsOldTable = cms.EDProducer("TriggerCandTableProducer",
                                      triggerSummary = cms.InputTag("hltTriggerSummaryAOD"),
                                      processName = cms.string("HLT"),
                                      trigCandsName = cms.string("hltP4s"),
                                      keepAllFilters = cms.untracked.bool(False))

hltTriggerCandsTable = cms.EDProducer("HLTriggerCandidateTableProducer",
                                      triggerSummary = cms.InputTag("hltTriggerSummaryAOD"),
                                      processName = cms.string("HLT"),
                                      trigCandsName = cms.string("hltTriggerCandidates"),
                                      # Configuration of specific paths and filters
                                      selection = cms.VPSet(
                                          cms.PSet(
                                              path = cms.string("HLT_IsoMu24_FromL1TkMuon"),
                                              filter = cms.untracked.string("hltL3crIsoL1TkSingleMu22L3f24QL3trkIsoRegionalNewFiltered0p07EcalHcalHgcalTrk ")
                                          ),
                                          cms.PSet(
                                              path = cms.string("HLT_Ele32_WPTight_Unseeded"),
                                              # If you leave 'filter' out, the C++ code will find the last filter automatically
                                          ),
                                          cms.PSet(
                                              path = cms.string("HLT_DoubleMediumDeepTauPFTauHPS35_eta2p1")
                                          ))
                                      )
