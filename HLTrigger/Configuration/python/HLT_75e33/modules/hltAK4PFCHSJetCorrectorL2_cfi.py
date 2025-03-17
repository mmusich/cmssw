import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Modules.LXXXCorrectorProducer import LXXXCorrectorProducer as _LXXXCorrectorProducer

hltAK4PFCHSJetCorrectorL2 = _LXXXCorrectorProducer(
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2Relative')
)
