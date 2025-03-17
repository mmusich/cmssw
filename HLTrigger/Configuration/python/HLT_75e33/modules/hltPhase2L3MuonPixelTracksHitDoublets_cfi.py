import FWCore.ParameterSet.Config as cms

from RecoTracker.TkHitPairs.HitPairEDProducer import HitPairEDProducer as _HitPairEDProducer

hltPhase2L3MuonPixelTracksHitDoublets = _HitPairEDProducer(
    clusterCheck = ("hltTrackerClusterCheck"),
    layerPairs = [0, 1, 2],
    maxElement = 5000000,
    maxElementTotal = 50000000,
    mightGet = cms.optional.untracked.vstring,
    produceIntermediateHitDoublets = True,
    produceSeedingHitSets = False,
    seedingLayers = ("hltPhase2L3MuonPixelTracksSeedLayers"),
    trackingRegions = ("hltPhase2L3MuonPixelTracksAndHighPtTripletTrackingRegions"),
    trackingRegionsSeedingLayers = ("")
)
