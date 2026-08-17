import FWCore.ParameterSet.Config as cms

hltScoutingMuonPacker = cms.EDProducer( "HLTScoutingMuonProducer",
    ChargedCandidates = cms.InputTag( "hltPhase2L3MuonCandidates" ),
    displacedvertexCollection = cms.InputTag( "hltDisplacedmumuVtxProducer" ),
    InputMuons = cms.InputTag( "hltPhase2L3Muons" ),
    InputLinks = cms.InputTag( "hltL3MuonsIterL3Links" ),
    Tracks = cms.InputTag( "hltPhase2L3MuonMerged" ),
    EcalPFClusterIsoMap = cms.InputTag( "hltPhase2L3MuonsEcalIsodR0p3dRVeto0p000" ),
    HcalPFClusterIsoMap = cms.InputTag( "hltPhase2L3MuonsHcalIsodR0p3dRVeto0p000" ),
    TrackIsoMap = cms.InputTag( 'hltPhase2L3MuonsTrkIsoRegionalNewdR0p3dRVeto0p005dz0p25dr0p20ChisqInfPtMin0p0Cut0p4','combinedRelativeIsoDeposits' ),
    muonPtCut = cms.double( 0.0 ),
    muonEtaCut = cms.double( 2.4 ),
    minVtxProbCut = cms.double( 0.001 )
)
