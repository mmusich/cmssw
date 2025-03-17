import FWCore.ParameterSet.Config as cms

from RecoTracker.TkSeedGenerator.SeedGeneratorFromProtoTracksEDProducer import SeedGeneratorFromProtoTracksEDProducer as _SeedGeneratorFromProtoTracksEDProducer

hltInitialStepSeeds = _SeedGeneratorFromProtoTracksEDProducer(
    InputCollection = cms.InputTag("hltPhase2PixelTracks"),
    InputVertexCollection = cms.InputTag(""),
    SeedCreatorPSet = cms.PSet(
        refToPSet_ = cms.string('seedFromProtoTracks')
    ),
    TTRHBuilder = cms.string('WithTrackAngle'),
    originHalfLength = cms.double(0.3),
    originRadius = cms.double(0.1),
    useEventsWithNoVertex = cms.bool(True),
    usePV = cms.bool(False),
    useProtoTrackKinematics = cms.bool(False),
    includeFourthHit = cms.bool(False)
)

from Configuration.ProcessModifiers.trackingLST_cff import trackingLST
trackingLST.toModify(hltInitialStepSeeds, includeFourthHit = True)
