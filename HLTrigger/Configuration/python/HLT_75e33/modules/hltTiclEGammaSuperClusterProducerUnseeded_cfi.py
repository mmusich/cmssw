import FWCore.ParameterSet.Config as cms

hltTiclEGammaSuperClusterProducerUnseeded = cms.EDProducer("EGammaSuperclusterProducer",
    enableRegression = cms.bool(True),
    layerClusters = cms.InputTag("hltHgcalMergeLayerClusters"),
    regressionModelPath = cms.FileInPath('RecoHGCal/TICL/data/superclustering/regression_v1.onnx'),
    superclusterEtThreshold = cms.double(4),
    ticlSuperClusters = cms.InputTag("hltTiclTracksterLinksSuperclusteringDNNUnseeded"),
    ticlTrackstersEM = cms.InputTag("hltTiclTrackstersCLUE3DHigh")
)
