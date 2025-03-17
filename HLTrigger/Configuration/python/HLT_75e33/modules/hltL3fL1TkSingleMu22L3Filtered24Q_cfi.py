import FWCore.ParameterSet.Config as cms

from HLTrigger.Muon.HLTMuonTrkL1TkMuFilter import HLTMuonTrkL1TkMuFilter as _HLTMuonTrkL1TkMuFilter

hltL3fL1TkSingleMu22L3Filtered24Q = _HLTMuonTrkL1TkMuFilter(
    inputCandCollection = ("hltPhase2L3MuonCandidates"),
    inputMuonCollection = ("hltPhase2L3Muons"),
    maxAbsEta = 1e+99,
    maxNormalizedChi2 = 1e+99,
    minMuonHits = -1,
    minMuonStations = 1,
    minN = 1,
    minPt = 24.0,
    minTrkHits = -1,
    l1GTAlgoBlockTag = ("l1tGTAlgoBlockProducer"),
    l1GTAlgoNames = cms.vstring("pSingleTkMuon22"),
    saveTags = True
)
