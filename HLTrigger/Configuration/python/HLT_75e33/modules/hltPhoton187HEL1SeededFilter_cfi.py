import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaGenericQuadraticEtaFilter import HLTEgammaGenericQuadraticEtaFilter as _HLTEgammaGenericQuadraticEtaFilter

hltPhoton187HEL1SeededFilter = _HLTEgammaGenericQuadraticEtaFilter(
    absEtaLowEdges = [0.0, 1.0, 1.479, 2.1],
    candTag = ("hltPhoton187HgcalHEL1SeededFilter"),
    doRhoCorrection = False,
    effectiveAreas = [0.1, 0.1, 0.3, 0.5],
    energyLowEdges = [0.0],
    etaBoundaryEB12 = 1.0,
    etaBoundaryEE12 = 2.1,
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
    thrOverEEB1 = [0.09],
    thrOverEEB2 = [0.09],
    thrOverEEE1 = [0.0],
    thrOverEEE2 = [0.0],
    thrRegularEB1 = [0.0],
    thrRegularEB2 = [0.0],
    thrRegularEE1 = [9999.0],
    thrRegularEE2 = [9999.0],
    useEt = False,
    varTag = ("hltEgammaHoverEL1Seeded")
)
