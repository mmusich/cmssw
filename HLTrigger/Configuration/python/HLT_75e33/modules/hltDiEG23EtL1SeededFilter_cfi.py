import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaEtFilter import HLTEgammaEtFilter as _HLTEgammaEtFilter

hltDiEG23EtL1SeededFilter = _HLTEgammaEtFilter(
    etcutEB = 23.0,
    etcutEE = 23.0,
    inputTag = ("hltEgammaCandidatesWrapperL1Seeded"),
    l1EGCand = ("hltEgammaCandidatesL1Seeded"),
    ncandcut = 2,
    saveTags = True
)
