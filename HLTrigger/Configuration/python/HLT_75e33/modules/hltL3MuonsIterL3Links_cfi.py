import FWCore.ParameterSet.Config as cms

hltL3MuonsIterL3Links = cms.EDProducer( "MuonLinksProducer",
    inputCollection = cms.InputTag( "hltPhase2L3Muons" )
)
