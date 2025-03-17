import FWCore.ParameterSet.Config as cms

from RecoTracker.TkSeedGenerator.SeedCreatorFromRegionConsecutiveHitsEDProducer import SeedCreatorFromRegionConsecutiveHitsEDProducer as _SeedCreatorFromRegionConsecutiveHitsEDProducer

hltElePixelSeedsTripletsL1Seeded = _SeedCreatorFromRegionConsecutiveHitsEDProducer(
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
    seedingHitSets = ("hltElePixelHitTripletsL1Seeded")
)
