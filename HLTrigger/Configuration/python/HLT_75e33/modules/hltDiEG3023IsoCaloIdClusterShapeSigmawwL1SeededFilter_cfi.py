import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaGenericFilter import HLTEgammaGenericFilter as _HLTEgammaGenericFilter

hltDiEG3023IsoCaloIdClusterShapeSigmawwL1SeededFilter = _HLTEgammaGenericFilter(
    absEtaLowEdges = [0.0, 1.479],
    candTag = ("hltDiEG3023IsoCaloIdClusterShapeSigmavvL1SeededFilter"),
    doRhoCorrection = False,
    effectiveAreas = [0.0, 0.0],
    energyLowEdges = [0.0],
    l1EGCand = ("hltEgammaCandidatesL1Seeded"),
    lessThan = True,
    ncandcut = 2,
    rhoMax = 99999999.0,
    rhoScale = 1.0,
    rhoTag = (""),
    saveTags = True,
    thrOverE2EB = [0],
    thrOverE2EE = [0],
    thrOverEEB = [0.04],
    thrOverEEE = [0.04],
    thrRegularEB = [64],
    thrRegularEE = [64],
    useEt = True,
    varTag = ("hltEgammaHGCALIDVarsL1Seeded","sigma2ww")
)
