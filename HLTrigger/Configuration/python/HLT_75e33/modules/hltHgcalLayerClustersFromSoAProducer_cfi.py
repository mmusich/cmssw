import FWCore.ParameterSet.Config as cms

from RecoLocalCalo.HGCalRecProducers.HGCalLayerClustersFromSoAProducer import HGCalLayerClustersFromSoAProducer as _HGCalLayerClustersFromSoAProducer

hltHgcalLayerClustersFromSoAProducer = _HGCalLayerClustersFromSoAProducer(
    detector = cms.string('EE'),
    hgcalRecHitsLayerClustersSoA = cms.InputTag("hltHgcalSoARecHitsLayerClustersProducer"),
    hgcalRecHitsSoA = cms.InputTag("hltHgcalSoARecHitsProducer"),
    nHitsTime = cms.uint32(3),
    src = cms.InputTag("hltHgcalSoALayerClustersProducer"),
    timeClname = cms.string('timeLayerCluster')
)


