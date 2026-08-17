import FWCore.ParameterSet.Config as cms

hltScoutingPFPacker = cms.EDProducer( "HLTScoutingPFProducer",
    pfJetCollection = cms.InputTag( "hltAK4PFJets" ),
    pfJetTagCollection = cms.InputTag( "" ),
    pfCandidateCollection = cms.InputTag( "hltParticleFlowTmp" ),
    vertexCollection = cms.InputTag( "hltPhase2PixelVertices" ),
    metCollection = cms.InputTag( "hltPFMET" ),
    rho = cms.InputTag( "hltFixedGridRhoFastjetAll" ),
    pfJetPtCut = cms.double( 20.0 ),
    pfJetEtaCut = cms.double( 5.0 ),
    pfCandidatePtCut = cms.double( 0.6 ),
    pfCandidateEtaCut = cms.double( 3.0 ),
    mantissaPrecision = cms.int32( 10 ),
    doJetTags = cms.bool( True ),
    doCandidates = cms.bool( True ),
    doMet = cms.bool( True ),
    doTrackVars = cms.bool( True ),
    relativeTrackVars = cms.bool( True ),
    doCandIndsForJets = cms.bool( False )
)
