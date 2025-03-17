import FWCore.ParameterSet.Config as cms

from HLTrigger.Muon.HLTMuonIsoFilter import HLTMuonIsoFilter as _HLTMuonIsoFilter

hltL3crIsoL1TkSingleMu22TrkIsoRegionalNewFiltered0p07EcalHcalHgcalTrk = _HLTMuonIsoFilter(
    CandTag = ("hltPhase2L3MuonCandidates"),
    DepTag = cms.VInputTag("hltPhase2L3MuonsTrkIsoRegionalNewdR0p3dRVeto0p005dz0p25dr0p20ChisqInfPtMin0p0Cut0p07"),
    IsolatorPSet = dict(
    ),
    MinN = 1,
    PreviousCandTag = ("hltL3crIsoL1TkSingleMu22HgcalIso4p70"),
    saveTags = True
)
