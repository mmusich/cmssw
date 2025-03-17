import FWCore.ParameterSet.Config as cms

from HLTrigger.btau.HLTPFJetCollectionProducer import HLTPFJetCollectionProducer as _HLTPFJetCollectionProducer

hltPFPuppiJetForBtagEta2p4 = _HLTPFJetCollectionProducer(
    HLTObject = cms.InputTag("hltPFPuppiJetForBtagSelectorEta2p4"),
    TriggerTypes = cms.vint32(86)
)
