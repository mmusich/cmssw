import FWCore.ParameterSet.Config as cms

from RecoVertex.AdaptiveVertexFinder.CandidateVertexArbitrator import CandidateVertexArbitrator as _CandidateVertexArbitrator

hltDeepTrackVertexArbitratorPF = _CandidateVertexArbitrator(
    beamSpot = ("hltOnlineBeamSpot"),
    dLenFraction = 0.333,
    dRCut = 0.4,
    distCut = 0.04,
    fitterRatio = 0.25,
    fitterSigmacut = 3,
    fitterTini = 256,
    maxTimeSignificance = 3.5,
    mightGet = cms.optional.untracked.vstring,
    primaryVertices = ("hltOfflinePrimaryVertices"),
    secondaryVertices = ("hltDeepInclusiveSecondaryVerticesPF"),
    sigCut = 5,
    trackMinLayers = 4,
    trackMinPixels = 1,
    trackMinPt = 1.4,
    tracks = ("hltParticleFlowTmp")
)
