import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTEgammaGenericFilter import HLTEgammaGenericFilter as _HLTEgammaGenericFilter

hltEle5DphiUnseededFilter = _HLTEgammaGenericFilter(
    absEtaLowEdges = [0.0, 1.479],
    candTag = ("hltEgammaCandidatesWrapperUnseeded"),
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
    thrOverE2EB = [-1.0],
    thrOverE2EE = [-1.0],
    thrOverEEB = [-1.0],
    thrOverEEE = [-1.0],
    thrRegularEB = [10],
    thrRegularEE = [10],
    useEt = False,
    varTag = ("hltEgammaGsfTrackVarsUnseeded","Dphi")
)
