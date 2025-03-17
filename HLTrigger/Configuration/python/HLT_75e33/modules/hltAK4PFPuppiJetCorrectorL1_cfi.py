import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Modules.L1FastjetCorrectorProducer import L1FastjetCorrectorProducer as _L1FastjetCorrectorProducer

hltAK4PFPuppiJetCorrectorL1 = _L1FastjetCorrectorProducer(
    algorithm = cms.string('AK4PFPuppiHLT'),
    level = cms.string('L1FastJet'),
    srcRho = ("hltFixedGridRhoFastjetAll")
)
