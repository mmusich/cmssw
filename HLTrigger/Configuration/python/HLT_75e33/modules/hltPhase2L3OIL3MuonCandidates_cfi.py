import FWCore.ParameterSet.Config as cms

from RecoMuon.L3MuonProducer.L3MuonCandidateProducer import L3MuonCandidateProducer as _L3MuonCandidateProducer

hltPhase2L3OIL3MuonCandidates = _L3MuonCandidateProducer(
    InputLinksObjects = ("hltPhase2L3OIL3MuonsLinksCombination"),
    InputObjects = ("hltPhase2L3OIL3Muons"),
    MuonPtOption = cms.string('Tracker')
)
