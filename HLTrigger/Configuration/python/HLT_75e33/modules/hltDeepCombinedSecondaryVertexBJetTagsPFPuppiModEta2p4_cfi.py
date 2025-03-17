import FWCore.ParameterSet.Config as cms

from RecoBTag.Combined.DeepFlavourJetTagsProducer import DeepFlavourJetTagsProducer as _DeepFlavourJetTagsProducer

hltDeepCombinedSecondaryVertexBJetTagsPFPuppiModEta2p4 = _DeepFlavourJetTagsProducer(
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepCSV_PhaseII.json'),
    checkSVForDefaults = cms.bool(True),
    meanPadding = cms.bool(True),
    src = cms.InputTag("hltDeepCombinedSecondaryVertexBJetTagsInfosPuppiModEta2p4"),
    toAdd = cms.PSet(
        probbb = cms.string('probb')
    )
)
