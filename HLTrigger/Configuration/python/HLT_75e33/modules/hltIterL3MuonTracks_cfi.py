import FWCore.ParameterSet.Config as cms

hltIterL3MuonTracks = cms.EDProducer( "HLTMuonTrackSelector",
    track = cms.InputTag( "hltPhase2L3MuonMerged" ),
    muon = cms.InputTag( "hltPhase2L3Muons" ),
    originalMVAVals = cms.InputTag( "none" ),
    copyMVA = cms.bool( False ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False )
)
