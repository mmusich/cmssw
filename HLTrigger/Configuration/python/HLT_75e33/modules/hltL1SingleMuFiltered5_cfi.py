import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.L1TTkMuonFilter import L1TTkMuonFilter as _L1TTkMuonFilter

hltL1SingleMuFiltered5 = _L1TTkMuonFilter(
    MaxEta = 2.4,
    MinEta = -2.4,
    MinN = 1,
    MinPt = 5.0,
    Scalings = dict(
        barrel = [0.820128, 1.04124, 0.0],
        endcap = [0.864715, 1.03215, 0.0],
        overlap = [0.920897, 1.03712, 0.0]
    ),
    inputTag = ("l1tTkMuonsGmt"),
    saveTags = True
)
