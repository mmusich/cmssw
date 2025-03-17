import FWCore.ParameterSet.Config as cms

from RecoTracker.TkSeedGenerator.SeedGeneratorFromProtoTracksEDProducer import SeedGeneratorFromProtoTracksEDProducer as _SeedGeneratorFromProtoTracksEDProducer

hltPhase2L3MuonInitialStepSeeds = _SeedGeneratorFromProtoTracksEDProducer(
    InputCollection = ("hltPhase2L3MuonPixelTracks"),
    InputVertexCollection = (""),
    SeedCreatorPSet = dict(
        refToPSet_ = cms.string('hltPhase2L3MuonSeedFromProtoTracks')
    ),
    TTRHBuilder = cms.string('WithTrackAngle'),
    originHalfLength = 0.3,
    originRadius = 0.1,
    useEventsWithNoVertex = True,
    usePV = True,
    useProtoTrackKinematics = False
)
