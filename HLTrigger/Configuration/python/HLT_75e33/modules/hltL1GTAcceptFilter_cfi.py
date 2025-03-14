import FWCore.ParameterSet.Config as cms

from L1Trigger.Phase2L1GT.L1GTAcceptFilter import L1GTAcceptFilter as _L1GTAcceptFilter

hltL1GTAcceptFilter = _L1GTAcceptFilter(
                                   algoBlocksTag = cms.InputTag("l1tGTAlgoBlockProducer"),
                                   decision = cms.string("final")                                    
                                   )
