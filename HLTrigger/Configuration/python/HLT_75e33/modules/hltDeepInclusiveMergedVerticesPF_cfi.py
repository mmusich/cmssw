import FWCore.ParameterSet.Config as cms

from RecoVertex.AdaptiveVertexFinder.CandidateVertexMerger import CandidateVertexMerger as _CandidateVertexMerger

hltDeepInclusiveMergedVerticesPF = _CandidateVertexMerger(
    maxFraction = cms.double(0.2),
    minSignificance = cms.double(10.0),
    secondaryVertices = cms.InputTag("hltDeepTrackVertexArbitratorPF")
)
