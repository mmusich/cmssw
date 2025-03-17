import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaEtFilter import HLTEgammaEtFilter as _HLTEgammaEtFilter

hltEG115EtL1SeededFilter = _HLTEgammaEtFilter(
    etcutEB = 115.0,
    etcutEE = 115.0,
    inputTag = ("hltEgammaCandidatesWrapperL1Seeded"),
    l1EGCand = ("hltEgammaCandidatesL1Seeded"),
    ncandcut = 1,
    saveTags = True
)
