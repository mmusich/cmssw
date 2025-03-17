import FWCore.ParameterSet.Config as cms

from RecoTracker.TkHitPairs.HitPairEDProducer import HitPairEDProducer as _HitPairEDProducer

hltPhase2L3FromL1TkMuonPixelTracksHitDoublets = _HitPairEDProducer(
    clusterCheck = (""),
    layerPairs = [0, 1, 2],
    maxElement = 0,
    produceIntermediateHitDoublets = True,
    produceSeedingHitSets = False,
    seedingLayers = ("hltPhase2L3FromL1TkMuonPixelLayerQuadruplets"),
    trackingRegions = ("hltPhase2L3FromL1TkMuonPixelTracksTrackingRegions"),
    trackingRegionsSeedingLayers = ("")
)
