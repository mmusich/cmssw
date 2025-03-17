import FWCore.ParameterSet.Config as cms

from RecoBTag.ImpactParameter.CandIPProducer import CandIPProducer as _CandIPProducer

hltDeepBLifetimeTagInfosPFPuppi = _CandIPProducer(
    candidates = ("hltParticleFlowTmp"),
    computeGhostTrack = True,
    computeProbabilities = True,
    ghostTrackPriorDeltaR = 0.03,
    jetDirectionUsingGhostTrack = False,
    jetDirectionUsingTracks = False,
    jets = ("hltAK4PFPuppiJets"),
    maxDeltaR = 0.4,
    maximumChiSquared = 5.0,
    maximumLongitudinalImpactParameter = 17.0,
    maximumTransverseImpactParameter = 0.2,
    minimumNumberOfHits = 3,
    minimumNumberOfPixelHits = 2,
    minimumTransverseMomentum = 1.0,
    primaryVertex = ("hltOfflinePrimaryVertices"),
    useTrackQuality = False
)
