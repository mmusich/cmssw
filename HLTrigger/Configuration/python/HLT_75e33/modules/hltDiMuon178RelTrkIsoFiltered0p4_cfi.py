import FWCore.ParameterSet.Config as cms

from HLTrigger.Muon.HLTMuonIsoFilter import HLTMuonIsoFilter as _HLTMuonIsoFilter

hltDiMuon178RelTrkIsoFiltered0p4 = _HLTMuonIsoFilter(
    CandTag = cms.InputTag("hltPhase2L3MuonCandidates"),
    DepTag = cms.VInputTag("hltPhase2L3MuonsTrkIsoRegionalNewdR0p3dRVeto0p005dz0p25dr0p20ChisqInfPtMin0p0Cut0p4"),
    IsolatorPSet = cms.PSet(

    ),
    MinN = cms.int32(2),
    PreviousCandTag = cms.InputTag("hltL3fL1DoubleMu155fPreFiltered8"),
    saveTags = cms.bool(True)
)
