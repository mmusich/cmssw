import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.L1TTkEleFilter import L1TTkEleFilter as _L1TTkEleFilter

l1tTkIsoEleSingle28Filter = _L1TTkEleFilter(
    ApplyQual1 = True,
    ApplyQual2 = True,
    EtaBinsForIsolation = [0.0, 1.479, 2.4],
    MaxAbsEta1 = 1.479,
    MaxAbsEta2 = 2.4,
    MinAbsEta1 = 0.0,
    MinAbsEta2 = 1.479,
    MinN = 1,
    MinPt = 28.0,
    Qual1IsMask = True,
    Qual2IsMask = True,
    Quality1 = 2,
    Quality2 = 2,
    Scalings = dict(
        barrel = [0.434262, 1.20586, 0.0],
        endcap = [0.266186, 1.25976, 0.0]
    ),
    TrkIsolation = [0.12, 0.2],
    inputTag1 = ("l1tLayer1EG","L1TkEleEB"),
    inputTag2 = ("l1tLayer1EG","L1TkEleEE"),
    saveTags = True
)
