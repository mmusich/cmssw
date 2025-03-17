import FWCore.ParameterSet.Config as cms

from RecoMuon.L3MuonProducer.L3MuonCandidateProducerFromMuons import L3MuonCandidateProducerFromMuons as _L3MuonCandidateProducerFromMuons

hltPhase2L3MuonCandidates = _L3MuonCandidateProducerFromMuons(
    InputObjects = ("hltPhase2L3Muons")
)
