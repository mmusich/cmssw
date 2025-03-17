import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaGenericFilter import HLTEgammaGenericFilter as _HLTEgammaGenericFilter

hltDiEG3023IsoCaloIdClusterShapeUnseededFilter = _HLTEgammaGenericFilter(
    absEtaLowEdges = [0.0, 1.479],
    candTag = ("hltDiEG23EtUnseededFilter"),
    doRhoCorrection = False,
    effectiveAreas = [0.0, 0.0],
    energyLowEdges = [0.0],
    l1EGCand = ("hltEgammaCandidatesUnseeded"),
    lessThan = True,
    ncandcut = 2,
    rhoMax = 99999999.0,
    rhoScale = 1.0,
    rhoTag = (""),
    saveTags = True,
    thrOverE2EB = [0],
    thrOverE2EE = [0],
    thrOverEEB = [0],
    thrOverEEE = [0],
    thrRegularEB = [0.0113],
    thrRegularEE = [0.0113],
    useEt = False,
    varTag = ("hltEgammaClusterShapeUnseeded","sigmaIEtaIEta5x5")
)
