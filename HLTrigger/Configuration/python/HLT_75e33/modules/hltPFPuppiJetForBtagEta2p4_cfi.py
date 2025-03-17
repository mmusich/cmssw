import FWCore.ParameterSet.Config as cms

from HLTrigger.btau.HLTPFJetCollectionProducer import HLTPFJetCollectionProducer as _HLTPFJetCollectionProducer

hltPFPuppiJetForBtagEta2p4 = _HLTPFJetCollectionProducer(
    HLTObject = ("hltPFPuppiJetForBtagSelectorEta2p4"),
    TriggerTypes = [86]
)
