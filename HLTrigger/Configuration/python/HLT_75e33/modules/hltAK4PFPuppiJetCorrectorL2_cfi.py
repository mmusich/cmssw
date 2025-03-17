import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Modules.LXXXCorrectorProducer import LXXXCorrectorProducer as _LXXXCorrectorProducer

hltAK4PFPuppiJetCorrectorL2 = _LXXXCorrectorProducer(
    algorithm = cms.string('AK4PFPuppiHLT'),
    level = cms.string('L2Relative')
)
