import FWCore.ParameterSet.Config as cms

from RecoHGCal.TICL.TICLLayerTileProducer import TICLLayerTileProducer as _TICLLayerTileProducer

hltTiclLayerTileProducer = _TICLLayerTileProducer(
    detector = cms.string('HGCAL'),
    layer_HFNose_clusters = ("hgcalLayerClustersHFNose"),
    layer_clusters = ("hltHgcalMergeLayerClusters"),
    mightGet = cms.optional.untracked.vstring
)
