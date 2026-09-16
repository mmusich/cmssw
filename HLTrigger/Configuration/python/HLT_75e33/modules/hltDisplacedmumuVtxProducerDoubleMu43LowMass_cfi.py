import FWCore.ParameterSet.Config as cms

hltDisplacedmumuVtxProducerDoubleMu43LowMass = cms.EDProducer("HLTDisplacedmumuVtxProducer",
    Src = cms.InputTag("hltPhase2L3MuonCandidates"),
    PreviousCandTag = cms.InputTag("hltDoubleMu43LowMassL3Filtered"),
    matchToPrevious = cms.bool(True),
    MaxEta = cms.double(2.5),
    MinPt = cms.double(0.0),
    MinPtPair = cms.double(0.0),
    MinInvMass = cms.double(0.2),
    MaxInvMass = cms.double(8.5),
    ChargeOpt = cms.int32(-1),
)
