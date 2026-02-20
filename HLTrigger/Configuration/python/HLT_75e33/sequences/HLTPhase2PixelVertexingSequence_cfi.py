import FWCore.ParameterSet.Config as cms
from HeterogeneousCore.AlpakaCore.functions import makeSerialClone

from ..modules.hltPhase2PixelVertices_cfi import *

HLTPhase2PixelVertexingSequence = cms.Sequence(
    hltPhase2PixelVertices
)

# Serial sequence for CPU vs. GPU validation, to be kept in sync with default sequence
def _makeSerialPhase2PixelVertexingSequence(seq):
    _g = globals()
    _g["hltPhase2PixelVerticesSerialSync"] = hltPhase2PixelVertices.clone(
        TrackCollection = "hltPhase2PixelTracksCAExtensionSerialSync"
    )
    _newSeq = cms.Sequence(
        hltPhase2PixelVerticesSerialSync
    )
    seq._seq = _newSeq._seq

# Empty sequence as a placeholder to be filled when alpakaValidationHLT is active
HLTPhase2PixelVertexingSequenceSerialSync = cms.Sequence()

from Configuration.ProcessModifiers.alpakaValidationHLT_cff import alpakaValidationHLT
alpakaValidationHLT.toModify(HLTPhase2PixelVertexingSequenceSerialSync, _makeSerialPhase2PixelVertexingSequence)
