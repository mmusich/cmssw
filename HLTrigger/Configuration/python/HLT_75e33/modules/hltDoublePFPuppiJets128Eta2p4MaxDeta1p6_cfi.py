import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.HLT2PFJetPFJet import HLT2PFJetPFJet as _HLT2PFJetPFJet

hltDoublePFPuppiJets128Eta2p4MaxDeta1p6 = _HLT2PFJetPFJet(
    MaxDelR = 1000.0,
    MaxDeta = 1.6,
    MaxDphi = 10000000.0,
    MaxMinv = 10000000.0,
    MaxPt = 10000000.0,
    MinDelR = 0.0,
    MinDeta = -1000.0,
    MinDphi = 0.0,
    MinMinv = 0.0,
    MinN = 1,
    MinPt = 0.0,
    inputTag1 = ("hltDoublePFPuppiJets128MaxEta2p4"),
    inputTag2 = ("hltDoublePFPuppiJets128MaxEta2p4"),
    originTag1 = cms.VInputTag("hltAK4PFPuppiJetsCorrected"),
    originTag2 = cms.VInputTag("hltAK4PFPuppiJetsCorrected"),
    saveTags = True,
    triggerType1 = 86,
    triggerType2 = 86
)
