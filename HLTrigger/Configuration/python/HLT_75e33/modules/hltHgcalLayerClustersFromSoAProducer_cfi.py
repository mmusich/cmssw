import FWCore.ParameterSet.Config as cms

from RecoLocalCalo.HGCalRecProducers.HGCalLayerClustersFromSoAProducer import HGCalLayerClustersFromSoAProducer as _HGCalLayerClustersFromSoAProducer

hltHgcalLayerClustersFromSoAProducer = _HGCalLayerClustersFromSoAProducer(
    detector = cms.string('EE'),
    hgcalRecHitsLayerClustersSoA = ("hltHgcalSoARecHitsLayerClustersProducer"),
    hgcalRecHitsSoA = ("hltHgcalSoARecHitsProducer"),
    nHitsTime = 3,
    src = ("hltHgcalSoALayerClustersProducer"),
    timeClname = cms.string('timeLayerCluster')
)


