import FWCore.ParameterSet.Config as cms

from HLTrigger.JetMET.HLTMhtFilter import HLTMhtFilter as _HLTMhtFilter

hltPFPuppiMHT140 = _HLTMhtFilter(
    mhtLabels = cms.VInputTag("hltPFPuppiMHT"),
    minMht = cms.vdouble(140.0),
    saveTags = cms.bool(True)
)
