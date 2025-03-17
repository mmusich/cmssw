import FWCore.ParameterSet.Config as cms

from HLTrigger.Egamma.HLTElectronPixelMatchFilter import HLTElectronPixelMatchFilter as _HLTElectronPixelMatchFilter

hltDiEle2312IsoPixelMatchL1SeededFilter = _HLTElectronPixelMatchFilter(
    candTag = ("hltDiEG2312IsoHcalIsoL1SeededFilter"),
    l1EGCand = ("hltEgammaCandidatesL1Seeded"),
    l1PixelSeedsTag = ("hltEgammaElectronPixelSeedsL1Seeded"),
    ncandcut = 2,
    npixelmatchcut = 1.0,
    pixelVeto = False,
    s2_threshold = 0.4,
    s_a_phi1B = 0.0069,
    s_a_phi1F = 0.0076,
    s_a_phi1I = 0.0088,
    s_a_phi2B = 0.00037,
    s_a_phi2F = 0.00906,
    s_a_phi2I = 0.0007,
    s_a_rF = 0.04,
    s_a_rI = 0.027,
    s_a_zB = 0.012,
    saveTags = True,
    tanhSO10BarrelThres = 0.35,
    tanhSO10ForwardThres = 1.0,
    tanhSO10InterThres = 1.0,
    useS = False
)
