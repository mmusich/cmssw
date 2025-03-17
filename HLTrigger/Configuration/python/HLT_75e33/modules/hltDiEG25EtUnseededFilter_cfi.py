import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaEtFilter import HLTEgammaEtFilter as _HLTEgammaEtFilter

hltDiEG25EtUnseededFilter = _HLTEgammaEtFilter(
    etcutEB = 25.0,
    etcutEE = 25.0,
    inputTag = ("hltEgammaCandidatesWrapperUnseeded"),
    l1EGCand = ("hltEgammaCandidatesUnseeded"),
    ncandcut = 2,
    saveTags = True
)
