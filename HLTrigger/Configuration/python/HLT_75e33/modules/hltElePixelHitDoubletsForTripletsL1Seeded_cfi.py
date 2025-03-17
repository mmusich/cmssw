import FWCore.ParameterSet.Config as cms

from RecoTracker.TkHitPairs.HitPairEDProducer import HitPairEDProducer as _HitPairEDProducer

hltElePixelHitDoubletsForTripletsL1Seeded = _HitPairEDProducer(
    clusterCheck = (""),
    layerPairs = [0, 1],
    maxElement = 0,
    maxElementTotal = 50000000,
    produceIntermediateHitDoublets = True,
    produceSeedingHitSets = True,
    seedingLayers = ("hltPixelLayerTriplets"),
    trackingRegions = ("hltEleSeedsTrackingRegionsL1Seeded"),
    trackingRegionsSeedingLayers = ("")
)
