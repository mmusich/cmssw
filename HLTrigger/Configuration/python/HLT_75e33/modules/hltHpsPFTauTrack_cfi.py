import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.HLT1PFTau import HLT1PFTau as _HLT1PFTau

hltHpsPFTauTrack = _HLT1PFTau(
    MaxEta = 2.5,
    MaxMass = -1.0,
    MinE = -1.0,
    MinEta = -1.0,
    MinMass = -1.0,
    MinN = 1,
    MinPt = 0.0,
    inputTag = ("hltHpsPFTauProducer"),
    saveTags = True,
    triggerType = 84
)
