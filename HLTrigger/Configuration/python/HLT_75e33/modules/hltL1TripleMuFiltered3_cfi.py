import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.L1TTkMuonFilter import L1TTkMuonFilter as _L1TTkMuonFilter

hltL1TripleMuFiltered3 = _L1TTkMuonFilter(
    MaxEta = 2.4,
    MinEta = -2.4,
    MinN = 3,
    MinPt = 3.0,
    Scalings = dict(
        barrel = [0.820128, 1.04124, 0.0],
        endcap = [0.864715, 1.03215, 0.0],
        overlap = [0.920897, 1.03712, 0.0]
    ),
    inputTag = ("l1tTkMuonsGmt"),
    saveTags = True
)
