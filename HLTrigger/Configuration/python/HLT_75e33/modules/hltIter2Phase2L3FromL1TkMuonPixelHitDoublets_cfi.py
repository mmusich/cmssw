import FWCore.ParameterSet.Config as cms

from RecoTracker.TkHitPairs.HitPairEDProducer import HitPairEDProducer as _HitPairEDProducer

hltIter2Phase2L3FromL1TkMuonPixelHitDoublets = _HitPairEDProducer(
    clusterCheck = ("hltIter2Phase2L3FromL1TkMuonPixelClusterCheck"),
    layerPairs = [0, 1],
    maxElement = 0,
    produceIntermediateHitDoublets = True,
    produceSeedingHitSets = False,
    seedingLayers = ("hltIter2Phase2L3FromL1TkMuonPixelLayerTriplets"),
    trackingRegions = ("hltPhase2L3FromL1TkMuonPixelTracksTrackingRegions"),
    trackingRegionsSeedingLayers = ("")
)
