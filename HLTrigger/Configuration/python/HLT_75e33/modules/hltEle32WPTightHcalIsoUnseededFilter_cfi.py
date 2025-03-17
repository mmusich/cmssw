import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaGenericQuadraticEtaFilter import HLTEgammaGenericQuadraticEtaFilter as _HLTEgammaGenericQuadraticEtaFilter

hltEle32WPTightHcalIsoUnseededFilter = _HLTEgammaGenericQuadraticEtaFilter(
    absEtaLowEdges = [0.0, 1.0, 1.479, 2.0],
    candTag = ("hltEle32WPTightHgcalIsoUnseededFilter"),
    doRhoCorrection = False,
    effectiveAreas = [0.2, 0.2, 0.4, 0.5],
    energyLowEdges = [0.0],
    etaBoundaryEB12 = 1.0,
    etaBoundaryEE12 = 2.0,
    l1EGCand = ("hltEgammaCandidatesUnseeded"),
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
    thrOverEEB1 = [0.02],
    thrOverEEB2 = [0.02],
    thrOverEEE1 = [0.02],
    thrOverEEE2 = [0.02],
    thrRegularEB1 = [19],
    thrRegularEB2 = [19],
    thrRegularEE1 = [19],
    thrRegularEE2 = [19],
    useEt = True,
    varTag = ("hltEgammaHcalPFClusterIsoUnseeded")
)
