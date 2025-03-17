import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaEtFilter import HLTEgammaEtFilter as _HLTEgammaEtFilter

hltEG32EtUnseededFilter = _HLTEgammaEtFilter(
    etcutEB = 32.0,
    etcutEE = 32.0,
    inputTag = ("hltEgammaCandidatesWrapperUnseeded"),
    l1EGCand = ("hltEgammaCandidatesUnseeded"),
    ncandcut = 1,
    saveTags = True
)
