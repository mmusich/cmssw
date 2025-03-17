import FWCore.ParameterSet.Config as cms

from HLTrigger.btau.HLTPFJetTag import HLTPFJetTag as _HLTPFJetTag

hltBTagPFPuppiDeepFlavour0p935DoubleEta2p4 = _HLTPFJetTag(
    JetTags = ("hltPfDeepFlavourJetTagsModEta2p4","probb"),
    Jets = ("hltPFPuppiJetForBtagEta2p4"),
    MatchJetsByDeltaR = True,
    MaxJetDeltaR = 0.1,
    MaxTag = 999999.0,
    MinJets = 2,
    MinTag = 0.935,
    TriggerType = 86,
    saveTags = True
)
