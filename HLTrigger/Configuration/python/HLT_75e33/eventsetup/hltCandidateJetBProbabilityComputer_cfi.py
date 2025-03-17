import FWCore.ParameterSet.Config as cms

from RecoBTag.ImpactParameter.CandidateJetBProbabilityESProducer import CandidateJetBProbabilityESProducer as _CandidateJetBProbabilityESProducer

hltCandidateJetBProbabilityComputer = _CandidateJetBProbabilityESProducer(
    a_dR = -0.001053,
    a_pT = 0.005263,
    b_dR = 0.6263,
    b_pT = 0.3684,
    deltaR = -1.0,
    impactParameterType = 0,
    max_pT = 500,
    max_pT_dRcut = 0.1,
    max_pT_trackPTcut = 3,
    maximumDecayLength = 5.0,
    maximumDistanceToJetAxis = 0.07,
    min_pT = 120,
    min_pT_dRcut = 0.5,
    minimumProbability = 0.005,
    numberOfBTracks = 4,
    trackIpSign = 1,
    trackQualityClass = cms.string('any'),
    useVariableJTA = False
)
