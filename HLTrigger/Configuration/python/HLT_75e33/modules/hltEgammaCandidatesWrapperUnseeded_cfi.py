import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaTriggerFilterObjectWrapper import HLTEgammaTriggerFilterObjectWrapper as _HLTEgammaTriggerFilterObjectWrapper

hltEgammaCandidatesWrapperUnseeded = _HLTEgammaTriggerFilterObjectWrapper(
    candIsolatedTag = ("hltEgammaCandidatesUnseeded"),
    candNonIsolatedTag = (""),
    doIsolated = True,
    saveTags = True
)
