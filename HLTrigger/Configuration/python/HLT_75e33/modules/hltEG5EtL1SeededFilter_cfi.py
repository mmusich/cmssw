import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaEtFilter import HLTEgammaEtFilter as _HLTEgammaEtFilter

hltEG5EtL1SeededFilter = _HLTEgammaEtFilter(
    etcutEB = cms.double(5.0),
    etcutEE = cms.double(5.0),
    inputTag = cms.InputTag("hltEgammaCandidatesWrapperL1Seeded"),
    l1EGCand = cms.InputTag("hltEgammaCandidatesL1Seeded"),
    ncandcut = cms.int32(1),
    saveTags = cms.bool(True)
)
