import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Modules.ChainedJetCorrectorProducer import ChainedJetCorrectorProducer as _ChainedJetCorrectorProducer

hltAK8PFJetCorrector = _ChainedJetCorrectorProducer(
    correctors = cms.VInputTag("hltAK8PFJetCorrectorL1", "hltAK8PFJetCorrectorL2", "hltAK8PFJetCorrectorL3")
)
