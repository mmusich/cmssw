import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaEtFilter import HLTEgammaEtFilter as _HLTEgammaEtFilter

hltEG32EtL1SeededFilter = _HLTEgammaEtFilter(
    etcutEB = 32.0,
    etcutEE = 32.0,
    inputTag = ("hltEgammaCandidatesWrapperL1Seeded"),
    l1EGCand = ("hltEgammaCandidatesL1Seeded"),
    ncandcut = 1,
    saveTags = True
)
