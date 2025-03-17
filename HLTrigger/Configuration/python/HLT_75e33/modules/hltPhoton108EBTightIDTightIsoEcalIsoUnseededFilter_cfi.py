import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaGenericQuadraticEtaFilter import HLTEgammaGenericQuadraticEtaFilter as _HLTEgammaGenericQuadraticEtaFilter

hltPhoton108EBTightIDTightIsoEcalIsoUnseededFilter = _HLTEgammaGenericQuadraticEtaFilter(
    absEtaLowEdges = [0.0, 1.0, 1.479, 2.1],
    candTag = ("hltPhoton108EBTightIDTightIsoHEUnseededFilter"),
    doRhoCorrection = False,
    effectiveAreas = [0.2, 0.2, 0.25, 0.3],
    energyLowEdges = [0.0],
    etaBoundaryEB12 = 1.0,
    etaBoundaryEE12 = 2.1,
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
    thrOverEEE1 = [0.0],
    thrOverEEE2 = [0.0],
    thrRegularEB1 = [2.5],
    thrRegularEB2 = [2.5],
    thrRegularEE1 = [0.0],
    thrRegularEE2 = [0.0],
    useEt = True,
    varTag = ("hltEgammaEcalPFClusterIsoUnseeded")
)
