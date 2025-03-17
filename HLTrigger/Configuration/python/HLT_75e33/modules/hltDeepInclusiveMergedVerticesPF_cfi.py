import FWCore.ParameterSet.Config as cms

from RecoVertex.AdaptiveVertexFinder.CandidateVertexMerger import CandidateVertexMerger as _CandidateVertexMerger

hltDeepInclusiveMergedVerticesPF = _CandidateVertexMerger(
    maxFraction = 0.2,
    minSignificance = 10.0,
    secondaryVertices = ("hltDeepTrackVertexArbitratorPF")
)
