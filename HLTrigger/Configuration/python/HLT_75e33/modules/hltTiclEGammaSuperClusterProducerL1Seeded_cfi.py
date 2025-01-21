import FWCore.ParameterSet.Config as cms

hltTiclEGammaSuperClusterProducerL1Seeded = cms.EDProducer("EGammaSuperclusterProducer",
    enableRegression = cms.bool(True),
    layerClusters = cms.InputTag("hltHgcalMergeLayerClustersL1Seeded"),
    regressionModelPath = cms.FileInPath('RecoHGCal/TICL/data/superclustering/regression_v1.onnx'),
    superclusterEtThreshold = cms.double(4),
    ticlSuperClusters = cms.InputTag("hltTiclTracksterLinksSuperclusteringDNNL1Seeded"),
    ticlTrackstersEM = cms.InputTag("hltTiclTrackstersCLUE3DHighL1Seeded"),
)
