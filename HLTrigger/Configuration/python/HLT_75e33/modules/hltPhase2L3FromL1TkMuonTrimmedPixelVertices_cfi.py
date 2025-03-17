import FWCore.ParameterSet.Config as cms

from RecoVertex.PixelVertexFinding.PixelVertexCollectionTrimmer import PixelVertexCollectionTrimmer as _PixelVertexCollectionTrimmer

hltPhase2L3FromL1TkMuonTrimmedPixelVertices = _PixelVertexCollectionTrimmer(
    PVcomparer = cms.PSet(
        refToPSet_ = cms.string('hltPhase2PSetPvClusterComparerForIT')
    ),
    fractionSumPt2 = cms.double(0.3),
    maxVtx = cms.uint32(100),
    minSumPt2 = cms.double(0.0),
    src = cms.InputTag("hltPhase2L3FromL1TkMuonPixelVertices")
)
