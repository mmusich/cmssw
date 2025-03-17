import FWCore.ParameterSet.Config as cms

from RecoBTag.Combined.DeepFlavourJetTagsProducer import DeepFlavourJetTagsProducer as _DeepFlavourJetTagsProducer

hltDeepCombinedSecondaryVertexBJetTagsPFPuppiModEta2p4 = _DeepFlavourJetTagsProducer(
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepCSV_PhaseII.json'),
    checkSVForDefaults = True,
    meanPadding = True,
    src = ("hltDeepCombinedSecondaryVertexBJetTagsInfosPuppiModEta2p4"),
    toAdd = dict(
        probbb = cms.string('probb')
    )
)
