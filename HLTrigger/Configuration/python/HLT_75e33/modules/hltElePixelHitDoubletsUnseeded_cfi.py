import FWCore.ParameterSet.Config as cms

from RecoTracker.TkHitPairs.HitPairEDProducer import HitPairEDProducer as _HitPairEDProducer

hltElePixelHitDoubletsUnseeded = _HitPairEDProducer(
    clusterCheck = (""),
    layerPairs = [0],
    maxElement = 0,
    maxElementTotal = 50000000,
    produceIntermediateHitDoublets = True,
    produceSeedingHitSets = True,
    seedingLayers = ("hltPixelLayerPairsUnseeded"),
    trackingRegions = ("hltEleSeedsTrackingRegionsUnseeded"),
    trackingRegionsSeedingLayers = ("")
)
