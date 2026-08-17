import FWCore.ParameterSet.Config as cms

hltDisplacedmumuVtxProducer = cms.EDProducer( "HLTDisplacedmumuVtxProducer",
    Src = cms.InputTag( "hltPhase2L3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "" ),
    matchToPrevious = cms.bool( False ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinPtPair = cms.double( 0.0 ),
    MinInvMass = cms.double( 0.0 ),
    MaxInvMass = cms.double( 99999.0 ),
    ChargeOpt = cms.int32( 0 )
)
