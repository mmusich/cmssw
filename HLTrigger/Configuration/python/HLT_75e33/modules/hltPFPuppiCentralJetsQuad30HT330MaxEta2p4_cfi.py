import FWCore.ParameterSet.Config as cms

from HLTrigger.JetMET.HLTHtMhtFilter import HLTHtMhtFilter as _HLTHtMhtFilter

hltPFPuppiCentralJetsQuad30HT330MaxEta2p4 = _HLTHtMhtFilter(
    htLabels = cms.VInputTag("hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4"),
    meffSlope = [1.0],
    mhtLabels = cms.VInputTag("hltHtMhtPFPuppiCentralJetsQuadC30MaxEta2p4"),
    minHt = [330.0],
    minMeff = [0.0],
    minMht = [0.0],
    saveTags = True
)
