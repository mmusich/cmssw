import FWCore.ParameterSet.Config as cms

from RecoVertex.AdaptiveVertexFinder.CandidateVertexMerger import CandidateVertexMerger as _CandidateVertexMerger

hltDeepInclusiveSecondaryVerticesPF = _CandidateVertexMerger(
    maxFraction = cms.double(0.7),
    minSignificance = cms.double(2),
    secondaryVertices = cms.InputTag("hltDeepInclusiveVertexFinderPF")
)
