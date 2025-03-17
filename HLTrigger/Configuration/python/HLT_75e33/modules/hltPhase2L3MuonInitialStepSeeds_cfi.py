import FWCore.ParameterSet.Config as cms

from RecoTracker.TkSeedGenerator.SeedGeneratorFromProtoTracksEDProducer import SeedGeneratorFromProtoTracksEDProducer as _SeedGeneratorFromProtoTracksEDProducer

hltPhase2L3MuonInitialStepSeeds = _SeedGeneratorFromProtoTracksEDProducer(
    InputCollection = cms.InputTag("hltPhase2L3MuonPixelTracks"),
    InputVertexCollection = cms.InputTag(""),
    SeedCreatorPSet = cms.PSet(
        refToPSet_ = cms.string('hltPhase2L3MuonSeedFromProtoTracks')
    ),
    TTRHBuilder = cms.string('WithTrackAngle'),
    originHalfLength = cms.double(0.3),
    originRadius = cms.double(0.1),
    useEventsWithNoVertex = cms.bool(True),
    usePV = cms.bool(True),
    useProtoTrackKinematics = cms.bool(False)
)
