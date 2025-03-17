import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Modules.LXXXCorrectorProducer import LXXXCorrectorProducer as _LXXXCorrectorProducer

hltAK8PFJetCorrectorL2 = _LXXXCorrectorProducer(
    algorithm = cms.string('AK8PF'),
    level = cms.string('L2Relative')
)
