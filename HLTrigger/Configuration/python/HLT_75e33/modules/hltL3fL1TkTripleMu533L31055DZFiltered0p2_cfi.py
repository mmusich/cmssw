import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.HLT2MuonMuonDZ import HLT2MuonMuonDZ as _HLT2MuonMuonDZ

hltL3fL1TkTripleMu533L31055DZFiltered0p2 = _HLT2MuonMuonDZ(
    MaxDZ = 0.2,
    MinDR = 0.001,
    MinN = 3,
    MinPixHitsForDZ = 1,
    checkSC = False,
    inputTag1 = ("hltL3fL1TkTripleMu533PreFiltered555"),
    inputTag2 = ("hltL3fL1TkTripleMu533PreFiltered555"),
    originTag1 = cms.VInputTag("hltPhase2L3MuonCandidates"),
    originTag2 = cms.VInputTag("hltPhase2L3MuonCandidates"),
    saveTags = True,
    triggerType1 = 83,
    triggerType2 = 83
)
