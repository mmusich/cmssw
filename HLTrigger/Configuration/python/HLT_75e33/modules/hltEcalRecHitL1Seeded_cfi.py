import FWCore.ParameterSet.Config as cms

from RecoLocalCalo.EcalRecProducers.EcalRecHitProducer import EcalRecHitProducer as _EcalRecHitProducer

hltEcalRecHitL1Seeded = _EcalRecHitProducer(
    ChannelStatusToBeExcluded = cms.vstring(
        'kDAC',
        'kNoisy',
        'kNNoisy',
        'kFixedG6',
        'kFixedG1',
        'kFixedG0',
        'kNonRespondingIsolated',
        'kDeadVFE',
        'kDeadFE',
        'kNoDataNoTP'
    ),
    EBLaserMAX = 3.0,
    EBLaserMIN = 0.5,
    EBrechitCollection = cms.string('EcalRecHitsEB'),
    EBuncalibRecHitCollection = ("hltEcalUncalibRecHitL1Seeded","EcalUncalibRecHitsEB"),
    EELaserMAX = 8.0,
    EELaserMIN = 0.5,
    EErechitCollection = cms.string('EcalRecHitsEE'),
    EEuncalibRecHitCollection = ("hltEcalUncalibRecHitL1Seeded","EcalUncalibRecHitsEE"),
    algo = cms.string('EcalRecHitWorkerSimple'),
    algoRecover = cms.string('EcalRecHitWorkerRecover'),
    bdtWeightFileCracks = cms.FileInPath('RecoLocalCalo/EcalDeadChannelRecoveryAlgos/data/BDTWeights/bdtgAllRH_8GT700MeV_onlyCracks_ZskimData2017_v1.xml'),
    bdtWeightFileNoCracks = cms.FileInPath('RecoLocalCalo/EcalDeadChannelRecoveryAlgos/data/BDTWeights/bdtgAllRH_8GT700MeV_noCracks_ZskimData2017_v1.xml'),
    cleaningConfig = dict(
        cThreshold_barrel = 4,
        cThreshold_double = 10,
        cThreshold_endcap = 15,
        e4e1Threshold_barrel = 0.08,
        e4e1Threshold_endcap = 0.3,
        e4e1_a_barrel = 0.02,
        e4e1_a_endcap = 0.02,
        e4e1_b_barrel = 0.02,
        e4e1_b_endcap = -0.0125,
        e6e2thresh = 0.04,
        ignoreOutOfTimeThresh = 1000000000.0,
        tightenCrack_e1_double = 2,
        tightenCrack_e1_single = 1,
        tightenCrack_e4e1_single = 2.5,
        tightenCrack_e6e2_double = 3
    ),
    dbStatusToBeExcludedEB = [14, 78, 142],
    dbStatusToBeExcludedEE = [14, 78, 142],
    ebDetIdToBeRecovered = ("hltEcalDetIdToBeRecovered","ebDetId"),
    ebFEToBeRecovered = ("hltEcalDetIdToBeRecovered","ebFE"),
    eeDetIdToBeRecovered = ("hltEcalDetIdToBeRecovered","eeDetId"),
    eeFEToBeRecovered = ("hltEcalDetIdToBeRecovered","eeFE"),
    flagsMapDBReco = dict(
        kDead = cms.vstring('kNoDataNoTP'),
        kGood = cms.vstring(
            'kOk',
            'kDAC',
            'kNoLaser',
            'kNoisy'
        ),
        kNeighboursRecovered = cms.vstring(
            'kFixedG0',
            'kNonRespondingIsolated',
            'kDeadVFE'
        ),
        kNoisy = cms.vstring(
            'kNNoisy',
            'kFixedG6',
            'kFixedG1'
        ),
        kTowerRecovered = cms.vstring('kDeadFE')
    ),
    killDeadChannels = True,
    laserCorrection = True,
    logWarningEtThreshold_EB_FE = 50,
    logWarningEtThreshold_EE_FE = 50,
    recoverEBFE = True,
    recoverEBIsolatedChannels = False,
    recoverEBVFE = False,
    recoverEEFE = True,
    recoverEEIsolatedChannels = False,
    recoverEEVFE = False,
    singleChannelRecoveryMethod = cms.string('BDTG'),
    singleChannelRecoveryThreshold = 0.7,
    skipTimeCalib = False,
    sum8ChannelRecoveryThreshold = 0.0,
    triggerPrimitiveDigiCollection = ("hltEcalDigis","EcalTriggerPrimitives")
)
