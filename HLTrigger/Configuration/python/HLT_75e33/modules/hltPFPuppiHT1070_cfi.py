import FWCore.ParameterSet.Config as cms

from HLTrigger.JetMET.HLTHtMhtFilter import HLTHtMhtFilter as _HLTHtMhtFilter

hltPFPuppiHT1070 = _HLTHtMhtFilter(
    htLabels = cms.VInputTag("hltPFPuppiHT"),
    meffSlope = [1.0],
    mhtLabels = cms.VInputTag("hltPFPuppiHT"),
    minHt = [1070.0],
    minMeff = [0.0],
    minMht = [0.0],
    saveTags = True
)
