import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.HLT1PFTau import HLT1PFTau as _HLT1PFTau

hltHpsPFTau27LooseTauWPDeepTau = _HLT1PFTau(
    MaxEta = 2.1,
    MaxMass = -1.0,
    MinE = -1.0,
    MinEta = -1.0,
    MinMass = -1.0,
    MinN = 1,
    MinPt = 27.0,
    inputTag = ("hltHpsSelectedPFTauLooseTauWPDeepTau"),
    saveTags = True,
    triggerType = 84
)
