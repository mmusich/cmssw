import FWCore.ParameterSet.Config as cms

from RecoVertex.AdaptiveVertexFinder.InclusiveCandidateVertexFinder import InclusiveCandidateVertexFinder as _InclusiveCandidateVertexFinder

hltDeepInclusiveVertexFinderPF = _InclusiveCandidateVertexFinder(
    beamSpot = ("hltOnlineBeamSpot"),
    clusterizer = dict(
        clusterMaxDistance = 0.05,
        clusterMaxSignificance = 4.5,
        clusterMinAngleCosine = 0.5,
        distanceRatio = 20,
        maxTimeSignificance = 3.5,
        seedMax3DIPSignificance = 9999,
        seedMax3DIPValue = 9999,
        seedMin3DIPSignificance = 1.2,
        seedMin3DIPValue = 0.005
    ),
    fitterRatio = 0.25,
    fitterSigmacut = 3,
    fitterTini = 256,
    maxNTracks = 15,
    maximumLongitudinalImpactParameter = 0.2,
    maximumTimeSignificance = 3,
    mightGet = cms.optional.untracked.vstring,
    minHits = 8,
    minPt = 1.4,
    primaryVertices = ("hltOfflinePrimaryVertices"),
    tracks = ("hltParticleFlowTmp"),
    useDirectVertexFitter = True,
    useVertexReco = True,
    vertexMinAngleCosine = 0.95,
    vertexMinDLen2DSig = 2.5,
    vertexMinDLenSig = 0.5,
    vertexReco = dict(
        finder = cms.string('avr'),
        primcut = 1,
        seccut = 3,
        smoothing = True
    )
)
