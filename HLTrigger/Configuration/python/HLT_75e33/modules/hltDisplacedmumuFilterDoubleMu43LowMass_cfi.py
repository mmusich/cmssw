import FWCore.ParameterSet.Config as cms
 
hltDisplacedmumuFilterDoubleMu43LowMass = cms.EDFilter("HLTDisplacedmumuFilter",
    saveTags = cms.bool(True),
    FastAccept = cms.bool(False),
    MinLxySignificance = cms.double(0.0),
    MaxLxySignificance = cms.double(0.0),
    MaxNormalisedChi2 = cms.double(999.0),
    MinVtxProbability = cms.double(0.005),
    MinCosinePointingAngle = cms.double(-2.0),
    DisplacedVertexTag = cms.InputTag("hltDisplacedmumuVtxProducerDoubleMu43LowMass"),
    BeamSpotTag = cms.InputTag("hltOnlineBeamSpot"),
    MuonTag = cms.InputTag("hltPhase2L3MuonCandidates"),
)

