import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaGenericFilter import HLTEgammaGenericFilter as _HLTEgammaGenericFilter

hltEle32WPTightPMS2L1SeededFilter = _HLTEgammaGenericFilter(
    absEtaLowEdges = [0.0, 1.479],
    candTag = ("hltEle32WPTightPixelMatchL1SeededFilter"),
    doRhoCorrection = False,
    effectiveAreas = [0.0, 0.0],
    energyLowEdges = [0.0],
    l1EGCand = ("hltEgammaCandidatesL1Seeded"),
    lessThan = True,
    ncandcut = 1,
    rhoMax = 99999999.0,
    rhoScale = 1.0,
    rhoTag = (""),
    saveTags = True,
    thrOverE2EB = [0],
    thrOverE2EE = [0],
    thrOverEEB = [0],
    thrOverEEE = [0],
    thrRegularEB = [55.0],
    thrRegularEE = [75.0],
    useEt = False,
    varTag = ("hltEgammaPixelMatchVarsL1Seeded","s2")
)
