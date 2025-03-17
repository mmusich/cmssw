import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaEtFilter import HLTEgammaEtFilter as _HLTEgammaEtFilter

hltEG26EtUnseededFilter = _HLTEgammaEtFilter(
    etcutEB = 26.0,
    etcutEE = 26.0,
    inputTag = ("hltEgammaCandidatesWrapperUnseeded"),
    l1EGCand = ("hltEgammaCandidatesUnseeded"),
    ncandcut = 1,
    saveTags = True
)
