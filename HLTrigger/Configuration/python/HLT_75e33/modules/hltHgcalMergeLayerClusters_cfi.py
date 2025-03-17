import FWCore.ParameterSet.Config as cms

from RecoLocalCalo.HGCalRecProducers.MergeClusterProducer import MergeClusterProducer as _MergeClusterProducer

hltHgcalMergeLayerClusters = _MergeClusterProducer(
    layerClustersEE = ("hltHgcalLayerClustersEE"),
    layerClustersHSci = ("hltHgcalLayerClustersHSci"),
    layerClustersHSi = ("hltHgcalLayerClustersHSi"),
    mightGet = cms.optional.untracked.vstring,
    timeClname = cms.string('timeLayerCluster'),
    time_layerclustersEE = ("hltHgcalLayerClustersEE","timeLayerCluster"),
    time_layerclustersHSci = ("hltHgcalLayerClustersHSci","timeLayerCluster"),
    time_layerclustersHSi = ("hltHgcalLayerClustersHSi","timeLayerCluster")
)
