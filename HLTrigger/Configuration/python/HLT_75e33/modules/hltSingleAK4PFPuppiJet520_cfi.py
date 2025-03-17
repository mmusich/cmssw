import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.HLT1PFJet import HLT1PFJet as _HLT1PFJet

hltSingleAK4PFPuppiJet520 = _HLT1PFJet(
    MaxEta = 5.0,
    MaxMass = -1.0,
    MinE = -1.0,
    MinEta = -1.0,
    MinMass = -1.0,
    MinN = 1,
    MinPt = 520.0,
    inputTag = ("hltAK4PFPuppiJetsCorrected"),
    saveTags = True,
    triggerType = 85
)
