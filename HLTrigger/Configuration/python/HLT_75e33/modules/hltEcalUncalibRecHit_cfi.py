import FWCore.ParameterSet.Config as cms

from RecoLocalCalo.EcalRecProducers.EcalUncalibRecHitProducer import EcalUncalibRecHitProducer as _EcalUncalibRecHitProducer

hltEcalUncalibRecHit = _EcalUncalibRecHitProducer(
    EBdigiCollection = ("hltEcalDigis","ebDigis"),
    EBhitCollection = cms.string('EcalUncalibRecHitsEB'),
    EEdigiCollection = ("hltEcalDigis","eeDigis"),
    EEhitCollection = cms.string('EcalUncalibRecHitsEE'),
    algo = cms.string('EcalUncalibRecHitWorkerMultiFit'),
    algoPSet = dict(
        EBamplitudeFitParameters = [1.138, 1.652],
        EBtimeConstantTerm = 0.6,
        EBtimeFitLimits_Lower = 0.2,
        EBtimeFitLimits_Upper = 1.4,
        EBtimeFitParameters = cms.vdouble(
            -2.015452, 3.130702, -12.3473, 41.88921, -82.83944,
            91.01147, -50.35761, 11.05621
        ),
        EBtimeNconst = 28.5,
        EEamplitudeFitParameters = [1.89, 1.4],
        EEtimeConstantTerm = 1.0,
        EEtimeFitLimits_Lower = 0.2,
        EEtimeFitLimits_Upper = 1.4,
        EEtimeFitParameters = cms.vdouble(
            -2.390548, 3.553628, -17.62341, 67.67538, -133.213,
            140.7432, -75.41106, 16.20277
        ),
        EEtimeNconst = 31.8,
        activeBXs = cms.vint32(
            -5, -4, -3, -2, -1,
            0, 1, 2, 3, 4
        ),
        addPedestalUncertaintyEB = 0.0,
        addPedestalUncertaintyEE = 0.0,
        ampErrorCalculation = True,
        amplitudeThresholdEB = 10,
        amplitudeThresholdEE = 10,
        doPrefitEB = False,
        doPrefitEE = False,
        dynamicPedestalsEB = False,
        dynamicPedestalsEE = False,
        gainSwitchUseMaxSampleEB = True,
        gainSwitchUseMaxSampleEE = False,
        mitigateBadSamplesEB = False,
        mitigateBadSamplesEE = False,
        outOfTimeThresholdGain12mEB = 5,
        outOfTimeThresholdGain12mEE = 1000,
        outOfTimeThresholdGain12pEB = 5,
        outOfTimeThresholdGain12pEE = 1000,
        outOfTimeThresholdGain61mEB = 5,
        outOfTimeThresholdGain61mEE = 1000,
        outOfTimeThresholdGain61pEB = 5,
        outOfTimeThresholdGain61pEE = 1000,
        prefitMaxChiSqEB = 25.0,
        prefitMaxChiSqEE = 10.0,
        selectiveBadSampleCriteriaEB = False,
        selectiveBadSampleCriteriaEE = False,
        simplifiedNoiseModelForGainSwitch = True,
        timealgo = cms.string('None'),
        useLumiInfoRunHeader = False
    )
)
