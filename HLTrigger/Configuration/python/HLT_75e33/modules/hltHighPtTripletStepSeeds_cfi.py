import FWCore.ParameterSet.Config as cms

from RecoTracker.TkSeedGenerator.SeedCreatorFromRegionConsecutiveHitsEDProducer import SeedCreatorFromRegionConsecutiveHitsEDProducer as _SeedCreatorFromRegionConsecutiveHitsEDProducer

hltHighPtTripletStepSeeds = _SeedCreatorFromRegionConsecutiveHitsEDProducer(
    MinOneOverPtError = 1,
    OriginTransverseErrorMultiplier = 1,
    SeedComparitorPSet = dict(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = 5,
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = False,
    magneticField = cms.string(''),
    mightGet = cms.optional.untracked.vstring,
    propagator = cms.string('PropagatorWithMaterial'),
    seedingHitSets = ("hltHighPtTripletStepHitTriplets")
)
