import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaEtFilter import HLTEgammaEtFilter as _HLTEgammaEtFilter

hltDiEG23EtUnseededFilter = _HLTEgammaEtFilter(
    etcutEB = 23.0,
    etcutEE = 23.0,
    inputTag = ("hltEgammaCandidatesWrapperUnseeded"),
    l1EGCand = ("hltEgammaCandidatesUnseeded"),
    ncandcut = 2,
    saveTags = True
)
