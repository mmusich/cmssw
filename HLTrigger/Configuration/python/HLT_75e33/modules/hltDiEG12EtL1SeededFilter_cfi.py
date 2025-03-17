import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaEtFilter import HLTEgammaEtFilter as _HLTEgammaEtFilter

hltDiEG12EtL1SeededFilter = _HLTEgammaEtFilter(
    etcutEB = 12.0,
    etcutEE = 12.0,
    inputTag = ("hltEgammaCandidatesWrapperL1Seeded"),
    l1EGCand = ("hltEgammaCandidatesL1Seeded"),
    ncandcut = 2,
    saveTags = True
)
