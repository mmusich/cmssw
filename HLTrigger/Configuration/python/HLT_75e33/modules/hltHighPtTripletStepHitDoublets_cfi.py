import FWCore.ParameterSet.Config as cms

from RecoTracker.TkHitPairs.HitPairEDProducer import HitPairEDProducer as _HitPairEDProducer

hltHighPtTripletStepHitDoublets = _HitPairEDProducer(
    clusterCheck = ("hltTrackerClusterCheck"),
    layerPairs = [0, 1],
    maxElement = 50000000,
    maxElementTotal = 50000000,
    mightGet = cms.optional.untracked.vstring,
    produceIntermediateHitDoublets = True,
    produceSeedingHitSets = False,
    seedingLayers = ("hltHighPtTripletStepSeedLayers"),
    trackingRegions = ("hltPhase2PixelTracksAndHighPtStepTrackingRegions"),
    trackingRegionsSeedingLayers = ("")
)
