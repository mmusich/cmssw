import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.HLT2L1P2GTCandL1P2GTCandDZ import HLT2L1P2GTCandL1P2GTCandDZ as _HLT2L1P2GTCandL1P2GTCandDZ

hltDoubleMuon7DZ1p0 = _HLT2L1P2GTCandL1P2GTCandDZ(
    MaxDZ = 1.0,
    MinDR = -1,
    MinN = 1,
    l1GTAlgoBlockTag = ("l1tGTAlgoBlockProducer"),
    l1GTAlgoName1 = "pDoubleTkMuon15_7",
    l1GTAlgoName2 = "pDoubleTkMuon15_7",
    originTag1 = cms.VInputTag(("l1tGTProducer", "GMTTkMuons")),
    originTag2 = cms.VInputTag(("l1tGTProducer", "GMTTkMuons")),
    saveTags = True,
    triggerType1 = -114,
    triggerType2 = -114
)
