import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaGenericQuadraticEtaFilter import HLTEgammaGenericQuadraticEtaFilter as _HLTEgammaGenericQuadraticEtaFilter

hltEle5WPTightGsfDphiL1SeededFilter = _HLTEgammaGenericQuadraticEtaFilter(
    absEtaLowEdges = [0.0, 0.8, 1.479, 2.1],
    candTag = ("hltEle5WPTightGsfDetaL1SeededFilter"),
    doRhoCorrection = False,
    effectiveAreas = [0.0, 0.0, 0.0, 0.0],
    energyLowEdges = [0.0],
    etaBoundaryEB12 = 0.8,
    etaBoundaryEE12 = 2.1,
    l1EGCand = ("hltEgammaCandidatesL1Seeded"),
    lessThan = True,
    ncandcut = 1,
    rhoMax = 99999999.0,
    rhoScale = 1.0,
    rhoTag = (""),
    saveTags = True,
    thrOverE2EB1 = [0.0],
    thrOverE2EB2 = [0.0],
    thrOverE2EE1 = [0.0],
    thrOverE2EE2 = [0.0],
    thrOverEEB1 = [0.0],
    thrOverEEB2 = [0.0],
    thrOverEEE1 = [0.0],
    thrOverEEE2 = [0.0],
    thrRegularEB1 = [0.02],
    thrRegularEB2 = [0.09],
    thrRegularEE1 = [0.04],
    thrRegularEE2 = [0.04],
    useEt = False,
    varTag = ("hltEgammaGsfTrackVarsL1Seeded","Dphi")
)
