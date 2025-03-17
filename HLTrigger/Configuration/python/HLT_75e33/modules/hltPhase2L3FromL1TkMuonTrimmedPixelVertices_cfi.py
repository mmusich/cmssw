import FWCore.ParameterSet.Config as cms

from RecoVertex.PixelVertexFinding.PixelVertexCollectionTrimmer import PixelVertexCollectionTrimmer as _PixelVertexCollectionTrimmer

hltPhase2L3FromL1TkMuonTrimmedPixelVertices = _PixelVertexCollectionTrimmer(
    PVcomparer = dict(
        refToPSet_ = cms.string('hltPhase2PSetPvClusterComparerForIT')
    ),
    fractionSumPt2 = 0.3,
    maxVtx = 100,
    minSumPt2 = 0.0,
    src = ("hltPhase2L3FromL1TkMuonPixelVertices")
)
