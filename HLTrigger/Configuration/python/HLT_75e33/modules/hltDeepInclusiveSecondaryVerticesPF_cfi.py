import FWCore.ParameterSet.Config as cms

from RecoVertex.AdaptiveVertexFinder.CandidateVertexMerger import CandidateVertexMerger as _CandidateVertexMerger

hltDeepInclusiveSecondaryVerticesPF = _CandidateVertexMerger(
    maxFraction = 0.7,
    minSignificance = 2,
    secondaryVertices = ("hltDeepInclusiveVertexFinderPF")
)
