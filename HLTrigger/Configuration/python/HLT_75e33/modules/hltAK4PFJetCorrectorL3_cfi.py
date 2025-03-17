import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Modules.LXXXCorrectorProducer import LXXXCorrectorProducer as _LXXXCorrectorProducer

hltAK4PFJetCorrectorL3 = _LXXXCorrectorProducer(
    algorithm = cms.string('AK4PF'),
    level = cms.string('L3Absolute')
)
