import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaTriggerFilterObjectWrapper import HLTEgammaTriggerFilterObjectWrapper as _HLTEgammaTriggerFilterObjectWrapper

hltEgammaCandidatesWrapperUnseeded = _HLTEgammaTriggerFilterObjectWrapper(
    candIsolatedTag = cms.InputTag("hltEgammaCandidatesUnseeded"),
    candNonIsolatedTag = cms.InputTag(""),
    doIsolated = cms.bool(True),
    saveTags = cms.bool(True)
)
