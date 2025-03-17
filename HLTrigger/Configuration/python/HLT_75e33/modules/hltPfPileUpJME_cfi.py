import FWCore.ParameterSet.Config as cms

from CommonTools.ParticleFlow.PFPileUp import PFPileUp as _PFPileUp

hltPfPileUpJME = _PFPileUp(
    PFCandidates = ("hltParticleFlowPtrs"),
    Vertices = ("hltGoodOfflinePrimaryVertices"),
    checkClosestZVertex = False,
    enable = True,
    useVertexAssociation = False,
    verbose = cms.untracked.bool(False),
    vertexAssociation = (""),
    vertexAssociationQuality = 7
)
