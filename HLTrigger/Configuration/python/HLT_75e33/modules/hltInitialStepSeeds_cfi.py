import FWCore.ParameterSet.Config as cms

from RecoTracker.TkSeedGenerator.SeedGeneratorFromProtoTracksEDProducer import SeedGeneratorFromProtoTracksEDProducer as _SeedGeneratorFromProtoTracksEDProducer

hltInitialStepSeeds = _SeedGeneratorFromProtoTracksEDProducer(
    InputCollection = ("hltPhase2PixelTracks"),
    InputVertexCollection = (""),
    SeedCreatorPSet = dict(
        refToPSet_ = cms.string('seedFromProtoTracks')
    ),
    TTRHBuilder = cms.string('WithTrackAngle'),
    originHalfLength = 0.3,
    originRadius = 0.1,
    useEventsWithNoVertex = True,
    usePV = False,
    useProtoTrackKinematics = False,
    includeFourthHit = False
)

from Configuration.ProcessModifiers.trackingLST_cff import trackingLST
trackingLST.toModify(hltInitialStepSeeds, includeFourthHit = True)
