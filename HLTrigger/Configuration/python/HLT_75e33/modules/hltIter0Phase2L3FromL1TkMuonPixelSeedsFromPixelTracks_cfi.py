import FWCore.ParameterSet.Config as cms

from RecoTracker.TkSeedGenerator.SeedGeneratorFromProtoTracksEDProducer import SeedGeneratorFromProtoTracksEDProducer as _SeedGeneratorFromProtoTracksEDProducer

hltIter0Phase2L3FromL1TkMuonPixelSeedsFromPixelTracks = _SeedGeneratorFromProtoTracksEDProducer(
    InputCollection = ("hltPhase2L3FromL1TkMuonPixelTracks"),
    InputVertexCollection = ("hltPhase2L3FromL1TkMuonTrimmedPixelVertices"),
    SeedCreatorPSet = dict(
        refToPSet_ = cms.string('hltPhase2SeedFromProtoTracks')
    ),
    TTRHBuilder = cms.string('WithTrackAngle'),
    originHalfLength = 0.3,
    originRadius = 0.1,
    useEventsWithNoVertex = True,
    usePV = False,
    useProtoTrackKinematics = False
)
