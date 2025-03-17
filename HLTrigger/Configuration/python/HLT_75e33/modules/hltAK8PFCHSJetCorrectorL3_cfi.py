import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Modules.LXXXCorrectorProducer import LXXXCorrectorProducer as _LXXXCorrectorProducer

hltAK8PFCHSJetCorrectorL3 = _LXXXCorrectorProducer(
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L3Absolute')
)
