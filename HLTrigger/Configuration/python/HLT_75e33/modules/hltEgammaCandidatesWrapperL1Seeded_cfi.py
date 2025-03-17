import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaTriggerFilterObjectWrapper import HLTEgammaTriggerFilterObjectWrapper as _HLTEgammaTriggerFilterObjectWrapper

hltEgammaCandidatesWrapperL1Seeded = _HLTEgammaTriggerFilterObjectWrapper(
    candIsolatedTag = cms.InputTag("hltEgammaCandidatesL1Seeded"),
    candNonIsolatedTag = cms.InputTag(""),
    doIsolated = cms.bool(True),
    saveTags = cms.bool(True)
)
