import FWCore.ParameterSet.Config as cms

from RecoHGCal.TICL.TICLLayerTileProducer import TICLLayerTileProducer as _TICLLayerTileProducer

hltTiclLayerTileProducer = _TICLLayerTileProducer(
    detector = cms.string('HGCAL'),
    layer_HFNose_clusters = cms.InputTag("hgcalLayerClustersHFNose"),
    layer_clusters = cms.InputTag("hltHgcalMergeLayerClusters"),
    mightGet = cms.optional.untracked.vstring
)
