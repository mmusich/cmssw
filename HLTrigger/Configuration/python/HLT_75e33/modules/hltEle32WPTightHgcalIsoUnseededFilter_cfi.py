import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaGenericQuadraticEtaFilter import HLTEgammaGenericQuadraticEtaFilter as _HLTEgammaGenericQuadraticEtaFilter

hltEle32WPTightHgcalIsoUnseededFilter = _HLTEgammaGenericQuadraticEtaFilter(
    absEtaLowEdges = [0.0, 1.0, 1.479, 2.0],
    candTag = ("hltEle32WPTightEcalIsoUnseededFilter"),
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
    thrRegularEB1 = [150],
    thrRegularEB2 = [150],
    thrRegularEE1 = [150],
    thrRegularEE2 = [350],
    useEt = False,
    varTag = ("hltEgammaHGCalLayerClusterIsoUnseeded")
)
