import FWCore.ParameterSet.Config as cms

from RecoBTag.Combined.DeepFlavourJetTagsProducer import DeepFlavourJetTagsProducer as _DeepFlavourJetTagsProducer

hltDeepCombinedSecondaryVertexBJetTagsPFPuppi = _DeepFlavourJetTagsProducer(
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepCSV_PhaseII.json'),
    checkSVForDefaults = True,
    meanPadding = True,
    src = ("hltDeepCombinedSecondaryVertexBJetTagsInfosPuppi"),
    toAdd = dict(
        probbb = cms.string('probb')
    )
)
