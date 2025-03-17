import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaEtFilter import HLTEgammaEtFilter as _HLTEgammaEtFilter

hltEG30EtUnseededFilter = _HLTEgammaEtFilter(
    etcutEB = 30.0,
    etcutEE = 30.0,
    inputTag = ("hltEgammaCandidatesWrapperUnseeded"),
    l1EGCand = ("hltEgammaCandidatesUnseeded"),
    ncandcut = 1,
    saveTags = True
)
