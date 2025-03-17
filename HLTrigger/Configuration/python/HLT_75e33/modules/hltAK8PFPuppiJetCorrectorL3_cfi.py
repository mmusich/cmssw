import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Modules.LXXXCorrectorProducer import LXXXCorrectorProducer as _LXXXCorrectorProducer

hltAK8PFPuppiJetCorrectorL3 = _LXXXCorrectorProducer(
    algorithm = cms.string('AK8PFPuppi'),
    level = cms.string('L3Absolute')
)
