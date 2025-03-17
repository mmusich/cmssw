import FWCore.ParameterSet.Config as cms

from RecoHGCal.TICL.TICLLayerTileProducer import TICLLayerTileProducer as _TICLLayerTileProducer

hltTiclLayerTileProducerL1Seeded = _TICLLayerTileProducer(
    detector = cms.string('HGCAL'),
    layer_HFNose_clusters = ("hgcalLayerClustersHFNose"),
    layer_clusters = ("hltHgcalMergeLayerClustersL1Seeded"),
    mightGet = cms.optional.untracked.vstring
)
