import FWCore.ParameterSet.Config as cms

from HLTrigger.JetMET.HLTHtMhtFilter import HLTHtMhtFilter as _HLTHtMhtFilter

hltPFPuppiHT1070 = _HLTHtMhtFilter(
    htLabels = cms.VInputTag("hltPFPuppiHT"),
    meffSlope = cms.vdouble(1.0),
    mhtLabels = cms.VInputTag("hltPFPuppiHT"),
    minHt = cms.vdouble(1070.0),
    minMeff = cms.vdouble(0.0),
    minMht = cms.vdouble(0.0),
    saveTags = cms.bool(True)
)
