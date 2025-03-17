import FWCore.ParameterSet.Config as cms

from RecoHGCal.TICL.FilteredLayerClustersProducer import FilteredLayerClustersProducer as _FilteredLayerClustersProducer

hltFilteredLayerClustersRecovery = _FilteredLayerClustersProducer(
    LayerClusters = ("hltHgcalMergeLayerClusters"),
    LayerClustersInputMask = ("hltTiclTrackstersCLUE3DHigh"),
    algo_number = [6, 7, 8],
    clusterFilter = cms.string('ClusterFilterBySize'),
    iteration_label = cms.string('Recovery'),
    max_cluster_size = 9999,
    max_layerId = 9999,
    mightGet = cms.optional.untracked.vstring,
    min_cluster_size = 2,
    min_layerId = 0
)
