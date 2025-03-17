import FWCore.ParameterSet.Config as cms

from RecoLocalCalo.HGCalRecProducers.MergeClusterProducer import MergeClusterProducer as _MergeClusterProducer

hltHgcalMergeLayerClustersL1Seeded = _MergeClusterProducer(
    layerClustersEE = ("hltHgcalLayerClustersEEL1Seeded"),
    layerClustersHSci = ("hltHgcalLayerClustersHSciL1Seeded"),
    layerClustersHSi = ("hltHgcalLayerClustersHSiL1Seeded"),
    mightGet = cms.optional.untracked.vstring,
    timeClname = cms.string('timeLayerCluster'),
    time_layerclustersEE = ("hltHgcalLayerClustersEEL1Seeded","timeLayerCluster"),
    time_layerclustersHSci = ("hltHgcalLayerClustersHSciL1Seeded","timeLayerCluster"),
    time_layerclustersHSi = ("hltHgcalLayerClustersHSiL1Seeded","timeLayerCluster")
)
