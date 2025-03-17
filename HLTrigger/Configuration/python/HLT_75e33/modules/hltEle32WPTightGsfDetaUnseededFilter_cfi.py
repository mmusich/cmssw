import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaGenericQuadraticEtaFilter import HLTEgammaGenericQuadraticEtaFilter as _HLTEgammaGenericQuadraticEtaFilter

hltEle32WPTightGsfDetaUnseededFilter = _HLTEgammaGenericQuadraticEtaFilter(
    absEtaLowEdges = [0.0, 0.8, 1.479, 2.1],
    candTag = ("hltEle32WPTightGsfOneOEMinusOneOPUnseededFilter"),
    doRhoCorrection = False,
    effectiveAreas = [0.0, 0.0, 0.0, 0.0],
    energyLowEdges = [0.0],
    etaBoundaryEB12 = 0.8,
    etaBoundaryEE12 = 2.1,
    l1EGCand = ("hltEgammaCandidatesUnseeded"),
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
    thrRegularEB1 = [0.003],
    thrRegularEB2 = [0.009],
    thrRegularEE1 = [0.004],
    thrRegularEE2 = [0.004],
    useEt = False,
    varTag = ("hltEgammaGsfTrackVarsUnseeded","DetaSeed")
)
