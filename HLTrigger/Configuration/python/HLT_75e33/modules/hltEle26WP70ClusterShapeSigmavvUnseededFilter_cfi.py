import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaGenericFilter import HLTEgammaGenericFilter as _HLTEgammaGenericFilter

hltEle26WP70ClusterShapeSigmavvUnseededFilter = _HLTEgammaGenericFilter(
    absEtaLowEdges = [0.0, 1.479],
    candTag = ("hltEle26WP70ClusterShapeUnseededFilter"),
    doRhoCorrection = False,
    effectiveAreas = [0.0, 0.0],
    energyLowEdges = [0.0],
    l1EGCand = ("hltEgammaCandidatesUnseeded"),
    lessThan = True,
    ncandcut = 1,
    rhoMax = 99999999.0,
    rhoScale = 1.0,
    rhoTag = (""),
    saveTags = True,
    thrOverE2EB = [0],
    thrOverE2EE = [0],
    thrOverEEB = [0.0008],
    thrOverEEE = [0.0008],
    thrRegularEB = [0.64],
    thrRegularEE = [0.64],
    useEt = True,
    varTag = ("hltEgammaHGCALIDVarsUnseeded","sigma2vv")
)
