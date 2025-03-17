import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.L1TPFTauFilter import L1TPFTauFilter as _L1TPFTauFilter

hltL1SingleNNTau150 = _L1TPFTauFilter(
    MaxEta = 2.172,
    MinEta = -2.172,
    MinN = 1,
    MinPt = 150.0,
    PassLooseNN = 0,
    Scalings = dict(
        barrel = [-9.54135, 1.73403, 0],
        endcap = [-36.157, 3.83749, 0]
    ),
    inputTag = ("l1tNNTauProducerPuppi","L1PFTausNN"),
    saveTags = True
)
