import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Modules.ChainedJetCorrectorProducer import ChainedJetCorrectorProducer as _ChainedJetCorrectorProducer

hltAK4PFCHSJetCorrector = _ChainedJetCorrectorProducer(
    correctors = cms.VInputTag("hltAK4PFCHSJetCorrectorL1", "hltAK4PFCHSJetCorrectorL2", "hltAK4PFCHSJetCorrectorL3")
)
