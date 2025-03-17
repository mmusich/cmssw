import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaEtFilter import HLTEgammaEtFilter as _HLTEgammaEtFilter

hltDiEG25EtL1SeededFilter = _HLTEgammaEtFilter(
    etcutEB = 25.0,
    etcutEE = 25.0,
    inputTag = ("hltEgammaCandidatesWrapperL1Seeded"),
    l1EGCand = ("hltEgammaCandidatesL1Seeded"),
    ncandcut = 2,
    saveTags = True
)
