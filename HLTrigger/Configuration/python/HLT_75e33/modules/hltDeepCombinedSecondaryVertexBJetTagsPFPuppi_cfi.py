import FWCore.ParameterSet.Config as cms

from RecoBTag.Combined.DeepFlavourJetTagsProducer import DeepFlavourJetTagsProducer as _DeepFlavourJetTagsProducer

hltDeepCombinedSecondaryVertexBJetTagsPFPuppi = _DeepFlavourJetTagsProducer(
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepCSV_PhaseII.json'),
    checkSVForDefaults = cms.bool(True),
    meanPadding = cms.bool(True),
    src = cms.InputTag("hltDeepCombinedSecondaryVertexBJetTagsInfosPuppi"),
    toAdd = cms.PSet(
        probbb = cms.string('probb')
    )
)
