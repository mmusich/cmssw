import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFTracking.PFTrackProducer import PFTrackProducer as _PFTrackProducer

hltPfTrack = _PFTrackProducer(
    GsfTrackModuleLabel = ("electronGsfTracks"),
    GsfTracksInEvents = False,
    MuColl = ("hltPhase2L3Muons"),
    PrimaryVertexLabel = ("hltOfflinePrimaryVertices"),
    TkColList = cms.VInputTag(("hltGeneralTracks")),
    TrackQuality = cms.string('highPurity'),
    TrajInEvents = False,
    UseQuality = True
)
