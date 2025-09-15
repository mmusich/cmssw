import FWCore.ParameterSet.Config as cms

from ..modules.hltPhase2PixelVertices_cfi import *

HLTPhase2PixelVertexingSequence = cms.Sequence(
    hltPhase2PixelVertices
)

from ..modules.hltPhase2PixelVerticesSoA_cfi import *

_HLTPhase2PixelVerticesSequence = cms.Sequence(
    hltPhase2PixelVerticesSoA+
    hltPhase2PixelVertices
)

from Configuration.ProcessModifiers.alpaka_cff import alpaka
alpaka.toReplaceWith(HLTPhase2PixelVertexingSequence, _HLTPhase2PixelVerticesSequence)
