import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.L1TTkEmFilter import L1TTkEmFilter as _L1TTkEmFilter

l1tTkEmDouble12Filter = _L1TTkEmFilter(
    ApplyQual1 = True,
    ApplyQual2 = True,
    EtaBinsForIsolation = [0.0, 1.479, 2.4],
    MaxAbsEta1 = 1.479,
    MaxAbsEta2 = 2.4,
    MinAbsEta1 = 0.0,
    MinAbsEta2 = 1.479,
    MinN = 2,
    MinPt = 12.0,
    Qual1IsMask = True,
    Qual2IsMask = True,
    Quality1 = 2,
    Quality2 = 4,
    Scalings = dict(
        barrel = [2.6604, 1.06077, 0.0],
        endcap = [3.17445, 1.13219, 0.0]
    ),
    TrkIsolation = [99999.0, 99999.0],
    inputTag1 = ("l1tLayer1EG","L1TkEmEB"),
    inputTag2 = ("l1tLayer1EG","L1TkEmEE"),
    saveTags = True
)
