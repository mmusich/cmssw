import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.HLT1PFTau import HLT1PFTau as _HLT1PFTau

hltHpsDoublePFTau40TrackPt1MediumChargedIsolation = _HLT1PFTau(
    MaxEta = 2.1,
    MaxMass = -1.0,
    MinE = -1.0,
    MinEta = -1.0,
    MinMass = -1.0,
    MinN = 2,
    MinPt = 40.0,
    inputTag = ("hltHpsSelectedPFTausTrackPt1MediumChargedIsolation"),
    saveTags = True,
    triggerType = 84
)
