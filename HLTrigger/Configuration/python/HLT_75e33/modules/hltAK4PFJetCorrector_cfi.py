import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Modules.ChainedJetCorrectorProducer import ChainedJetCorrectorProducer as _ChainedJetCorrectorProducer

hltAK4PFJetCorrector = _ChainedJetCorrectorProducer(
    correctors = cms.VInputTag("hltAK4PFJetCorrectorL1", "hltAK4PFJetCorrectorL2", "hltAK4PFJetCorrectorL3")
)
