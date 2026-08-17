import FWCore.ParameterSet.Config as cms

hltScoutingPrimaryVertexPacker = cms.EDProducer( "HLTScoutingPrimaryVertexProducer",
    vertexCollection = cms.InputTag( "hltPhase2PixelVertices" ),
    mantissaPrecision = cms.int32( 10 )
)
