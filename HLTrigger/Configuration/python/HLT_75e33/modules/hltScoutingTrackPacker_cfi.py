import FWCore.ParameterSet.Config as cms

hltScoutingTrackPacker = cms.EDProducer( "HLTScoutingTrackProducer",
    OtherTracks = cms.InputTag( "hltPFMuonMerging" ),
    vertexCollection = cms.InputTag( "hltPhase2PixelVertices." ),
    mantissaPrecision = cms.int32( 10 ),
    vtxMinDist = cms.double( 999.0 ),
    ptMin = cms.double( 1.0 )
)
