import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Modules.ChainedJetCorrectorProducer import ChainedJetCorrectorProducer as _ChainedJetCorrectorProducer

hltAK8PFPuppiJetCorrector = _ChainedJetCorrectorProducer(
    correctors = cms.VInputTag("hltAK8PFPuppiJetCorrectorL1", "hltAK8PFPuppiJetCorrectorL2", "hltAK8PFPuppiJetCorrectorL3")
)
