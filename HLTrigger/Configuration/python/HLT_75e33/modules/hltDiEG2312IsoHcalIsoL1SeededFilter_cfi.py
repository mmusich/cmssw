import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaGenericQuadraticEtaFilter import HLTEgammaGenericQuadraticEtaFilter as _HLTEgammaGenericQuadraticEtaFilter

hltDiEG2312IsoHcalIsoL1SeededFilter = _HLTEgammaGenericQuadraticEtaFilter(
    absEtaLowEdges = [0.0, 0.8, 1.479, 2.0],
    candTag = ("hltDiEG2312IsoHgcalIsoL1SeededFilter"),
    doRhoCorrection = False,
    effectiveAreas = [0.2, 0.2, 0.4, 0.5],
    energyLowEdges = [0.0],
    etaBoundaryEB12 = 0.8,
    etaBoundaryEE12 = 2.0,
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
    thrRegularEB1 = [100],
    thrRegularEB2 = [100],
    thrRegularEE1 = [100],
    thrRegularEE2 = [100],
    useEt = True,
    varTag = ("hltEgammaHcalPFClusterIsoL1Seeded")
)
