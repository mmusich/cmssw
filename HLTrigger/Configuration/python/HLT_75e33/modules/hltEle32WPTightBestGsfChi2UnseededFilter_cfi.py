import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaGenericFilter import HLTEgammaGenericFilter as _HLTEgammaGenericFilter

hltEle32WPTightBestGsfChi2UnseededFilter = _HLTEgammaGenericFilter(
    absEtaLowEdges = [0.0, 1.479],
    candTag = ("hltEle32WPTightBestGsfNLayerITUnseededFilter"),
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
    thrOverEEB = [0],
    thrOverEEE = [0],
    thrRegularEB = [50.0],
    thrRegularEE = [50.0],
    useEt = False,
    varTag = ("hltEgammaBestGsfTrackVarsUnseeded","Chi2")
)
