import FWCore.ParameterSet.Config as cms

from RecoMuon.L2MuonProducer.L2MuonCandidateProducer import L2MuonCandidateProducer as _L2MuonCandidateProducer

hltL2MuonFromL1TkMuonCandidates = _L2MuonCandidateProducer(
    InputObjects = cms.InputTag("hltL2MuonsFromL1TkMuon","UpdatedAtVtx")
)
