import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaGenericQuadraticEtaFilter import HLTEgammaGenericQuadraticEtaFilter as _HLTEgammaGenericQuadraticEtaFilter

hltEle30WPTightGsfTrackIsoFromL1TracksL1SeededFilter = _HLTEgammaGenericQuadraticEtaFilter(
    absEtaLowEdges = [0.0, 0.8, 1.479, 2.0],
    candTag = ("hltEle30WPTightBestGsfChi2L1SeededFilter"),
    doRhoCorrection = False,
    effectiveAreas = [0.0, 0.0, 0.0, 0.0],
    energyLowEdges = [0.0],
    etaBoundaryEB12 = 0.8,
    etaBoundaryEE12 = 2.0,
    l1EGCand = ("hltEgammaCandidatesL1Seeded"),
    lessThan = True,
    ncandcut = 1,
    rhoMax = 99999999.0,
    rhoScale = 1.0,
    rhoTag = ("hltFixedGridRhoFastjetAllCaloForEGamma"),
    saveTags = True,
    thrOverE2EB1 = [0.0],
    thrOverE2EB2 = [0.0],
    thrOverE2EE1 = [0.0],
    thrOverE2EE2 = [0.0],
    thrOverEEB1 = [0.0],
    thrOverEEB2 = [0.0],
    thrOverEEE1 = [0.0],
    thrOverEEE2 = [0.0],
    thrRegularEB1 = [5.5],
    thrRegularEB2 = [8.0],
    thrRegularEE1 = [5.5],
    thrRegularEE2 = [5.5],
    useEt = True,
    varTag = ("hltEgammaEleL1TrkIsoL1Seeded")
)
