import FWCore.ParameterSet.Config as cms

from HLTrigger.Muon.HLTMuonTrkL1TkMuFilter import HLTMuonTrkL1TkMuFilter as _HLTMuonTrkL1TkMuFilter

hltL3fL1TkSingleMu22L3Filtered24Q = _HLTMuonTrkL1TkMuFilter(
    inputCandCollection = cms.InputTag("hltPhase2L3MuonCandidates"),
    inputMuonCollection = cms.InputTag("hltPhase2L3Muons"),
    maxAbsEta = cms.double(1e+99),
    maxNormalizedChi2 = cms.double(1e+99),
    minMuonHits = cms.int32(-1),
    minMuonStations = cms.int32(1),
    minN = cms.uint32(1),
    minPt = cms.double(24.0),
    minTrkHits = cms.int32(-1),
    l1GTAlgoBlockTag = cms.InputTag("l1tGTAlgoBlockProducer"),
    l1GTAlgoNames = cms.vstring("pSingleTkMuon22"),
    saveTags = cms.bool(True)
)
