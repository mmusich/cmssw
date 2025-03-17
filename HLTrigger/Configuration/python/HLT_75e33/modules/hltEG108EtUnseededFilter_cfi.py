import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaEtFilter import HLTEgammaEtFilter as _HLTEgammaEtFilter

hltEG108EtUnseededFilter = _HLTEgammaEtFilter(
    etcutEB = 108.0,
    etcutEE = 9999999.0,
    inputTag = ("hltEgammaCandidatesWrapperUnseeded"),
    l1EGCand = ("hltEgammaCandidatesUnseeded"),
    ncandcut = 1,
    saveTags = True
)
