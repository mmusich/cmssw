import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaGenericQuadraticEtaFilter import HLTEgammaGenericQuadraticEtaFilter as _HLTEgammaGenericQuadraticEtaFilter

hltDiEG2312IsoEcalIsoL1SeededFilter = _HLTEgammaGenericQuadraticEtaFilter(
    absEtaLowEdges = [0.0, 1.0, 1.479, 2.1],
    candTag = ("hltDiEG2312IsoHEL1SeededFilter"),
    doRhoCorrection = False,
    effectiveAreas = [0.2, 0.2, 0.25, 0.3],
    energyLowEdges = [0.0],
    etaBoundaryEB12 = 1.0,
    etaBoundaryEE12 = 2.1,
    l1EGCand = ("hltEgammaCandidatesL1Seeded"),
    lessThan = True,
    ncandcut = 2,
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
    thrRegularEB1 = [80],
    thrRegularEB2 = [80],
    thrRegularEE1 = [80],
    thrRegularEE2 = [80],
    useEt = True,
    varTag = ("hltEgammaEcalPFClusterIsoL1Seeded")
)
