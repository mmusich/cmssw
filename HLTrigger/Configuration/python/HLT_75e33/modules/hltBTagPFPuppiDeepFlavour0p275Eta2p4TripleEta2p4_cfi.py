import FWCore.ParameterSet.Config as cms

from HLTrigger.btau.HLTPFJetTag import HLTPFJetTag as _HLTPFJetTag

hltBTagPFPuppiDeepFlavour0p275Eta2p4TripleEta2p4 = _HLTPFJetTag(
    JetTags = ("hltPfDeepFlavourJetTagsModEta2p4","probb"),
    Jets = ("hltPFPuppiJetForBtagEta2p4"),
    MaxTag = 999999.0,
    MinJets = 3,
    MinTag = 0.275,
    TriggerType = 86,
    saveTags = True
)
