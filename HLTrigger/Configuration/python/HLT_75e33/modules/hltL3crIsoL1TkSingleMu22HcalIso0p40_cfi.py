import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTMuonGenericFilter import HLTMuonGenericFilter as _HLTMuonGenericFilter

hltL3crIsoL1TkSingleMu22HcalIso0p40 = _HLTMuonGenericFilter(
    absEtaLowEdges = [0.0, 1.479],
    candTag = ("hltL3crIsoL1TkSingleMu22EcalIso0p41"),
    doRhoCorrection = False,
    effectiveAreas = [0.0, 0.0],
    energyLowEdges = [0.0],
    l1EGCand = ("hltPhase2L3MuonCandidates"),
    lessThan = True,
    ncandcut = 1,
    rhoMax = 99999999.0,
    rhoScale = 1.0,
    rhoTag = (""),
    saveTags = True,
    thrOverE2EB = [-1.0],
    thrOverE2EE = [-1.0],
    thrOverEEB = [0.4],
    thrOverEEE = [0.4],
    thrRegularEB = [-1.0],
    thrRegularEE = [-1.0],
    useEt = True,
    varTag = ("hltPhase2L3MuonsHcalIsodR0p3dRVeto0p000")
)
