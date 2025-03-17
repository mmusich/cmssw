import FWCore.ParameterSet.Config as cms

from HLTrigger.JetMET.HLTHtMhtProducer import HLTHtMhtProducer as _HLTHtMhtProducer

hltPFPuppiMHT = _HLTHtMhtProducer(
    excludePFMuons = cms.bool(False),
    jetsLabel = cms.InputTag("hltAK4PFPuppiJetsCorrected"),
    maxEtaJetHt = cms.double(5.0),
    maxEtaJetMht = cms.double(5.0),
    minNJetHt = cms.int32(0),
    minNJetMht = cms.int32(0),
    minPtJetHt = cms.double(30.0),
    minPtJetMht = cms.double(30.0),
    pfCandidatesLabel = cms.InputTag(""),
    usePt = cms.bool(False)
)
