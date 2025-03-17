import FWCore.ParameterSet.Config as cms

from HLTrigger.Muon.HLTMuonTrkL1TkMuFilter import HLTMuonTrkL1TkMuFilter as _HLTMuonTrkL1TkMuFilter

hltL3fL1TkTripleMu533PreFiltered555 = _HLTMuonTrkL1TkMuFilter(
    inputCandCollection = ("hltPhase2L3MuonCandidates"),
    inputMuonCollection = ("hltPhase2L3Muons"),
    maxAbsEta = 2.5,
    maxNormalizedChi2 = 1e+99,
    minMuonHits = -1,
    minMuonStations = 1,
    minN = 3,
    minPt = 5.0,
    minTrkHits = -1,
    l1GTAlgoBlockTag = ("l1tGTAlgoBlockProducer"),
    l1GTAlgoNames = ["pTripleTkMuon5_3_3"],
    saveTags = True
)
