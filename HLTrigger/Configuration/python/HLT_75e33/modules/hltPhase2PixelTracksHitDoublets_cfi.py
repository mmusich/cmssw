import FWCore.ParameterSet.Config as cms

from RecoTracker.TkHitPairs.HitPairEDProducer import HitPairEDProducer as _HitPairEDProducer

hltPhase2PixelTracksHitDoublets = _HitPairEDProducer(
    clusterCheck = (""),
    layerPairs = [0, 1, 2],
    maxElement = 50000000,
    maxElementTotal = 50000000,
    produceIntermediateHitDoublets = True,
    produceSeedingHitSets = False,
    seedingLayers = ("hltPhase2PixelTracksSeedLayers"),
    trackingRegions = ("hltPhase2PixelTracksAndHighPtStepTrackingRegions"),
    trackingRegionsSeedingLayers = ("")
)
