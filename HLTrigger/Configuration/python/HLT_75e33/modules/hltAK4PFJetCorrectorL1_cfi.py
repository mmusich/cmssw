import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Modules.L1FastjetCorrectorProducer import L1FastjetCorrectorProducer as _L1FastjetCorrectorProducer

hltAK4PFJetCorrectorL1 = _L1FastjetCorrectorProducer(
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("hltFixedGridRhoFastjetAll")
)
