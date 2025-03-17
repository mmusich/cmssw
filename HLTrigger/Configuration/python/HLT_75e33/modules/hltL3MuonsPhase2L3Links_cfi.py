import FWCore.ParameterSet.Config as cms

from RecoMuon.MuonIdentification.MuonLinksProducer import MuonLinksProducer as _MuonLinksProducer

hltL3MuonsPhase2L3Links = _MuonLinksProducer(
    inputCollection = cms.InputTag("hltPhase2L3Muons")
)
