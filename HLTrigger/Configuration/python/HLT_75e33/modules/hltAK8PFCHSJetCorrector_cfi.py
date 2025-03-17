import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Modules.ChainedJetCorrectorProducer import ChainedJetCorrectorProducer as _ChainedJetCorrectorProducer

hltAK8PFCHSJetCorrector = _ChainedJetCorrectorProducer(
    correctors = cms.VInputTag("hltAK8PFCHSJetCorrectorL1", "hltAK8PFCHSJetCorrectorL2", "hltAK8PFCHSJetCorrectorL3")
)
