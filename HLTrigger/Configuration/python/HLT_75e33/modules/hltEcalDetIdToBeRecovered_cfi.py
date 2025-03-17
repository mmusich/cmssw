import FWCore.ParameterSet.Config as cms

from RecoLocalCalo.EcalRecProducers.EcalDetIdToBeRecoveredProducer import EcalDetIdToBeRecoveredProducer as _EcalDetIdToBeRecoveredProducer

hltEcalDetIdToBeRecovered = _EcalDetIdToBeRecoveredProducer(
    ebDetIdToBeRecovered = cms.string('ebDetId'),
    ebFEToBeRecovered = cms.string('ebFE'),
    ebIntegrityChIdErrors = ("hltEcalDigis","EcalIntegrityChIdErrors"),
    ebIntegrityGainErrors = ("hltEcalDigis","EcalIntegrityGainErrors"),
    ebIntegrityGainSwitchErrors = ("hltEcalDigis","EcalIntegrityGainSwitchErrors"),
    ebSrFlagCollection = ("hltEcalDigis"),
    eeDetIdToBeRecovered = cms.string('eeDetId'),
    eeFEToBeRecovered = cms.string('eeFE'),
    eeIntegrityChIdErrors = ("hltEcalDigis","EcalIntegrityChIdErrors"),
    eeIntegrityGainErrors = ("hltEcalDigis","EcalIntegrityGainErrors"),
    eeIntegrityGainSwitchErrors = ("hltEcalDigis","EcalIntegrityGainSwitchErrors"),
    eeSrFlagCollection = ("hltEcalDigis"),
    integrityBlockSizeErrors = ("hltEcalDigis","EcalIntegrityBlockSizeErrors"),
    integrityTTIdErrors = ("hltEcalDigis","EcalIntegrityTTIdErrors")
)
