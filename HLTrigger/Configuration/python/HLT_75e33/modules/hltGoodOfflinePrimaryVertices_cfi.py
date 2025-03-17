import FWCore.ParameterSet.Config as cms

from CommonTools.RecoAlgos.VertexSelector import VertexSelector as _VertexSelector

hltGoodOfflinePrimaryVertices = _VertexSelector(
    cut = cms.string('!isFake && ndof >= 4.0 && abs(z) <= 24.0 && abs(position.Rho) <= 2.0'),
    filter = False,
    src = ("hltOfflinePrimaryVertices")
)
