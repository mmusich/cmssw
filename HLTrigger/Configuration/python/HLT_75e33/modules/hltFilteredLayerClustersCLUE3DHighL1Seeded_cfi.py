import FWCore.ParameterSet.Config as cms

from RecoHGCal.TICL.FilteredLayerClustersProducer import FilteredLayerClustersProducer as _FilteredLayerClustersProducer

hltFilteredLayerClustersCLUE3DHighL1Seeded = _FilteredLayerClustersProducer(
    LayerClusters = ("hltHgcalMergeLayerClustersL1Seeded"),
    LayerClustersInputMask = ("hltHgcalMergeLayerClustersL1Seeded","InitialLayerClustersMask"),
    clusterFilter = cms.string('ClusterFilterByAlgoAndSize'),
    iteration_label = cms.string('CLUE3DHigh'),
    max_cluster_size = 9999,
    max_layerId = 9999,
    mightGet = cms.optional.untracked.vstring,
    min_cluster_size = 2,
    min_layerId = 0
)
