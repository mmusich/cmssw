import FWCore.ParameterSet.Config as cms

from RecoTracker.TkSeedGenerator.SeedCreatorFromRegionConsecutiveHitsEDProducer import SeedCreatorFromRegionConsecutiveHitsEDProducer as _SeedCreatorFromRegionConsecutiveHitsEDProducer

hltElePixelSeedsTripletsL1Seeded = _SeedCreatorFromRegionConsecutiveHitsEDProducer(
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("hltElePixelHitTripletsL1Seeded")
)
