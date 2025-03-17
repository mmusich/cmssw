import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaGenericQuadraticEtaFilter import HLTEgammaGenericQuadraticEtaFilter as _HLTEgammaGenericQuadraticEtaFilter

hltEle26WP70HgcalIsoUnseededFilter = _HLTEgammaGenericQuadraticEtaFilter(
    absEtaLowEdges = [0.0, 1.0, 1.479, 2.0],
    candTag = ("hltEle26WP70EcalIsoUnseededFilter"),
    doRhoCorrection = False,
    effectiveAreas = [0.0, 0.0, 0.0, 0.0],
    energyLowEdges = [0.0],
    etaBoundaryEB12 = 1.0,
    etaBoundaryEE12 = 2.0,
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
    thrOverEEB1 = [0.05],
    thrOverEEB2 = [0.05],
    thrOverEEE1 = [0.05],
    thrOverEEE2 = [0.05],
    thrRegularEB1 = [130],
    thrRegularEB2 = [130],
    thrRegularEE1 = [130],
    thrRegularEE2 = [340],
    useEt = False,
    varTag = ("hltEgammaHGCalLayerClusterIsoUnseeded")
)
