import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.HLT1PFJet import HLT1PFJet as _HLT1PFJet

hlt2PFPuppiCentralJet60MaxEta2p4 = _HLT1PFJet(
    MaxEta = 2.4,
    MaxMass = -1.0,
    MinE = -1.0,
    MinEta = -2.4,
    MinMass = -1.0,
    MinN = 2,
    MinPt = 60.0,
    inputTag = ("hltAK4PFPuppiJetsCorrected"),
    saveTags = True,
    triggerType = 86
)
