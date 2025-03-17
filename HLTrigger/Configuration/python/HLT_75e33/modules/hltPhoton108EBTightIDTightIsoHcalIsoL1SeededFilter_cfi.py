import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaGenericQuadraticEtaFilter import HLTEgammaGenericQuadraticEtaFilter as _HLTEgammaGenericQuadraticEtaFilter

hltPhoton108EBTightIDTightIsoHcalIsoL1SeededFilter = _HLTEgammaGenericQuadraticEtaFilter(
    absEtaLowEdges = [0.0, 0.8, 1.479, 2.0],
    candTag = ("hltPhoton108EBTightIDTightIsoEcalIsoL1SeededFilter"),
    doRhoCorrection = False,
    effectiveAreas = [0.2, 0.2, 0.4, 0.5],
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
    thrOverEEB1 = [0.02],
    thrOverEEB2 = [0.02],
    thrOverEEE1 = [0.0],
    thrOverEEE2 = [0.0],
    thrRegularEB1 = [3.8],
    thrRegularEB2 = [6.0],
    thrRegularEE1 = [0],
    thrRegularEE2 = [0],
    useEt = True,
    varTag = ("hltEgammaHcalPFClusterIsoL1Seeded")
)
