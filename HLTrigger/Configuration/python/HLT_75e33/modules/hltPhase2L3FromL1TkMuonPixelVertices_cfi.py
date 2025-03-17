import FWCore.ParameterSet.Config as cms

from RecoVertex.PixelVertexFinding.PixelVertexProducer import PixelVertexProducer as _PixelVertexProducer

hltPhase2L3FromL1TkMuonPixelVertices = _PixelVertexProducer(
    Finder = cms.string('DivisiveVertexFinder'),
    Method2 = True,
    NTrkMin = 2,
    PVcomparer = dict(
        refToPSet_ = cms.string('hltPhase2PSetPvClusterComparerForIT')
    ),
    PtMin = 1.0,
    TrackCollection = ("hltPhase2L3FromL1TkMuonPixelTracks"),
    UseError = True,
    Verbosity = 0,
    WtAverage = True,
    ZOffset = 5.0,
    ZSeparation = 0.05,
    beamSpot = ("hltOnlineBeamSpot")
)
