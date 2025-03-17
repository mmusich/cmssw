import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Modules.LXXXCorrectorProducer import LXXXCorrectorProducer as _LXXXCorrectorProducer

hltAK8PFCHSJetCorrectorL2 = _LXXXCorrectorProducer(
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L2Relative')
)
