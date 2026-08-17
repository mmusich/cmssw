import FWCore.ParameterSet.Config as cms

hltScoutingRecHitPacker = cms.EDProducer( "HLTScoutingRecHitProducer",
    pfRecHitsECAL = cms.InputTag( "hltParticleFlowRecHitECALUnseeded" ),
    pfRecHitsECALCleaned = cms.InputTag( 'hltParticleFlowRecHitECALUnseeded','Cleaned' ),
    pfRecHitsHBHE = cms.InputTag( "hltParticleFlowRecHitHBHE" ),
    minEnergyEB = cms.double( -1.0 ),
    minEnergyEE = cms.double( -1.0 ),
    minEnergyCleanedEB = cms.double( -1.0 ),
    minEnergyCleanedEE = cms.double( -1.0 ),
    minEnergyHBHE = cms.double( 1.0 ),
    mantissaPrecision = cms.int32( 10 )
)
