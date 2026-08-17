import FWCore.ParameterSet.Config as cms

hltPFMuonMerging = cms.EDProducer( "TrackListMerger",
    copyExtras = cms.untracked.bool( True ),
    copyMVA = cms.bool( False ),
    TrackProducers = cms.VInputTag( 'hltIterL3MuonTracks','hltGeneralTracks' ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    MinPT = cms.double( 0.05 ),
    MinFound = cms.int32( 3 ),
    Epsilon = cms.double( -0.001 ),
    ShareFrac = cms.double( 0.19 ),
    allowFirstHitShare = cms.bool( True ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    newQuality = cms.string( "confirmed" ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    hasSelector = cms.vint32( 0, 0 ),
    selectedTrackQuals = cms.VInputTag( 'hltIterL3MuonTracks','hltGeneralTracks' ),
    writeOnlyTrkQuals = cms.bool( False ),
    makeReKeyedSeeds = cms.untracked.bool( False ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" )
)
