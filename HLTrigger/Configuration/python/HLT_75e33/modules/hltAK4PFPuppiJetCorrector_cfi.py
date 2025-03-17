import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Modules.ChainedJetCorrectorProducer import ChainedJetCorrectorProducer as _ChainedJetCorrectorProducer

hltAK4PFPuppiJetCorrector = _ChainedJetCorrectorProducer(
    correctors = cms.VInputTag("hltAK4PFPuppiJetCorrectorL1", "hltAK4PFPuppiJetCorrectorL2", "hltAK4PFPuppiJetCorrectorL3")
)
