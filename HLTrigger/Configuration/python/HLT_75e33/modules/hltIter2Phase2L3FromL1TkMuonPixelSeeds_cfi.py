import FWCore.ParameterSet.Config as cms

from RecoTracker.TkSeedGenerator.SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer import SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer as _SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer

hltIter2Phase2L3FromL1TkMuonPixelSeeds = _SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer(
    MinOneOverPtError = 1.0,
    OriginTransverseErrorMultiplier = 1.0,
    SeedComparitorPSet = dict(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = 5.0,
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = False,
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = ("hltIter2Phase2L3FromL1TkMuonPixelHitTriplets")
)
