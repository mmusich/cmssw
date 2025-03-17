import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.HLT2L1P2GTCandL1P2GTCandDZ import HLT2L1P2GTCandL1P2GTCandDZ as _HLT2L1P2GTCandL1P2GTCandDZ

hltTripleMuon3DR0 = _HLT2L1P2GTCandL1P2GTCandDZ(
    MaxDZ = -1,
    MinDR = 0,
    MinN = 3,
    l1GTAlgoBlockTag = ("l1tGTAlgoBlockProducer"),
    l1GTAlgoName1 = "pTripleTkMuon5_3_3",
    l1GTAlgoName2 = "pTripleTkMuon5_3_3",
    originTag1 = cms.VInputTag(("l1tGTProducer", "GMTTkMuons")),
    originTag2 = cms.VInputTag(("l1tGTProducer", "GMTTkMuons")),
    saveTags = True,
    triggerType1 = -114,
    triggerType2 = -114
)
