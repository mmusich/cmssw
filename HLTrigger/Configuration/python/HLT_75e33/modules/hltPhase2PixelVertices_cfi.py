import FWCore.ParameterSet.Config as cms

from RecoVertex.PixelVertexFinding.PixelVertexProducer import PixelVertexProducer as _PixelVertexProducer

hltPhase2PixelVertices = _PixelVertexProducer(
    Finder = cms.string('DivisiveVertexFinder'),
    Method2 = True,
    NTrkMin = 2,
    PVcomparer = dict(
        refToPSet_ = cms.string('pSetPvClusterComparerForIT')
    ),
    PtMin = 1.0,
    TrackCollection = ("hltPhase2PixelTracks"),
    UseError = True,
    Verbosity = 0,
    WtAverage = True,
    ZOffset = 5.0,
    ZSeparation = 0.005,
    beamSpot = ("hltOnlineBeamSpot")
)
