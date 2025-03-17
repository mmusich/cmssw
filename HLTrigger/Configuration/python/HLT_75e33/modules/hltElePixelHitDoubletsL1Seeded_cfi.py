import FWCore.ParameterSet.Config as cms

from RecoTracker.TkHitPairs.HitPairEDProducer import HitPairEDProducer as _HitPairEDProducer

hltElePixelHitDoubletsL1Seeded = _HitPairEDProducer(
    clusterCheck = (""),
    layerPairs = [0],
    maxElement = 0,
    maxElementTotal = 50000000,
    produceIntermediateHitDoublets = True,
    produceSeedingHitSets = True,
    seedingLayers = ("hltPixelLayerPairsL1Seeded"),
    trackingRegions = ("hltEleSeedsTrackingRegionsL1Seeded"),
    trackingRegionsSeedingLayers = ("")
)
