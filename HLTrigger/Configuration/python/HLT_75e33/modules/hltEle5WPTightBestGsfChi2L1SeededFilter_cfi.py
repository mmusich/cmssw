import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaGenericFilter import HLTEgammaGenericFilter as _HLTEgammaGenericFilter

hltEle5WPTightBestGsfChi2L1SeededFilter = _HLTEgammaGenericFilter(
    absEtaLowEdges = [0.0, 1.479],
    candTag = ("hltEle5WPTightBestGsfNLayerITL1SeededFilter"),
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
    thrRegularEB = [50.0],
    thrRegularEE = [50.0],
    useEt = False,
    varTag = ("hltEgammaBestGsfTrackVarsL1Seeded","Chi2")
)
