import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.HLT1PFJet import HLT1PFJet as _HLT1PFJet

hltPFPuppiCentralJetQuad30MaxEta2p4 = _HLT1PFJet(
    MaxEta = 2.4,
    MaxMass = -1.0,
    MinE = -1.0,
    MinEta = -2.4,
    MinMass = -1.0,
    MinN = 4,
    MinPt = 30.0,
    inputTag = ("hltAK4PFPuppiJetsCorrected"),
    saveTags = True,
    triggerType = 86
)
