import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Modules.LXXXCorrectorProducer import LXXXCorrectorProducer as _LXXXCorrectorProducer

hltAK8PFJetCorrectorL3 = _LXXXCorrectorProducer(
    algorithm = cms.string('AK8PF'),
    level = cms.string('L3Absolute')
)
