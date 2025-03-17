import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.HLT2MuonMuonDZ import HLT2MuonMuonDZ as _HLT2MuonMuonDZ

hltDiMuon178RelTrkIsoFiltered0p4DzFiltered0p2 = _HLT2MuonMuonDZ(
    MaxDZ = 0.2,
    MinDR = 0.001,
    MinN = 1,
    MinPixHitsForDZ = 0,
    checkSC = False,
    inputTag1 = ("hltDiMuon178RelTrkIsoFiltered0p4"),
    inputTag2 = ("hltDiMuon178RelTrkIsoFiltered0p4"),
    originTag1 = cms.VInputTag("hltPhase2L3MuonCandidates"),
    originTag2 = cms.VInputTag("hltPhase2L3MuonCandidates"),
    saveTags = True,
    triggerType1 = 83,
    triggerType2 = 83
)
