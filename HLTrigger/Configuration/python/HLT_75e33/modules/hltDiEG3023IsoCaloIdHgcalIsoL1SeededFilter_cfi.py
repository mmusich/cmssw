import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaGenericQuadraticEtaFilter import HLTEgammaGenericQuadraticEtaFilter as _HLTEgammaGenericQuadraticEtaFilter

hltDiEG3023IsoCaloIdHgcalIsoL1SeededFilter = _HLTEgammaGenericQuadraticEtaFilter(
    absEtaLowEdges = [0.0, 1.0, 1.479, 2.0],
    candTag = ("hltDiEG3023IsoCaloIdEcalIsoL1SeededFilter"),
    doRhoCorrection = False,
    effectiveAreas = [0.0, 0.0, 0.0, 0.0],
    energyLowEdges = [0.0],
    etaBoundaryEB12 = 1.0,
    etaBoundaryEE12 = 2.0,
    l1EGCand = ("hltEgammaCandidatesL1Seeded"),
    lessThan = True,
    ncandcut = 2,
    rhoMax = 99999999.0,
    rhoScale = 1.0,
    rhoTag = (""),
    saveTags = True,
    thrOverE2EB1 = [0.0],
    thrOverE2EB2 = [0.0],
    thrOverE2EE1 = [0.0],
    thrOverE2EE2 = [0.0],
    thrOverEEB1 = [0.05],
    thrOverEEB2 = [0.05],
    thrOverEEE1 = [0.05],
    thrOverEEE2 = [0.05],
    thrRegularEB1 = [140],
    thrRegularEB2 = [140],
    thrRegularEE1 = [140],
    thrRegularEE2 = [370],
    useEt = False,
    varTag = ("hltEgammaHGCalLayerClusterIsoL1Seeded")
)
