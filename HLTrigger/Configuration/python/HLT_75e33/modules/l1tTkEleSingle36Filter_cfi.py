import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.L1TTkEleFilter import L1TTkEleFilter as _L1TTkEleFilter

l1tTkEleSingle36Filter = _L1TTkEleFilter(
    ApplyQual1 = True,
    ApplyQual2 = True,
    EtaBinsForIsolation = [0.0, 1.479, 2.4],
    MaxAbsEta1 = 1.479,
    MaxAbsEta2 = 2.4,
    MinAbsEta1 = 0.0,
    MinAbsEta2 = 1.479,
    MinN = 1,
    MinPt = 36.0,
    Qual1IsMask = True,
    Qual2IsMask = True,
    Quality1 = 2,
    Quality2 = 2,
    Scalings = dict(
        barrel = [0.805095, 1.18336, 0.0],
        endcap = [0.453144, 1.26205, 0.0]
    ),
    TrkIsolation = [99999.0, 99999.0],
    inputTag1 = ("l1tLayer1EG","L1TkEleEB"),
    inputTag2 = ("l1tLayer1EG","L1TkEleEE"),
    saveTags = True
)
