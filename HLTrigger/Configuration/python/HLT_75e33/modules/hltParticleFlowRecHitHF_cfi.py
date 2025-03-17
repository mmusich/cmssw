import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFClusterProducer.PFRecHitProducer import PFRecHitProducer as _PFRecHitProducer

hltParticleFlowRecHitHF = _PFRecHitProducer(
    navigator = dict(
        hcalEnums = [4],
        name = 'PFRecHitHCALDenseIdNavigator'
    ),
    producers = [dict(
        EMDepthCorrection = 22.0,
        HADDepthCorrection = 25.0,
        HFCalib29 = 1.07,
        LongFibre_Cut = 120.0,
        LongFibre_Fraction = 0.1,
        ShortFibre_Cut = 60.0,
        ShortFibre_Fraction = 0.01,
        name = 'PFHFRecHitCreator',
        qualityTests = [
            dict(
                cleaningThresholds = [0.0, 120.0, 60.0],
                flags = ['Standard', 'HFLong', 'HFShort'],
                maxSeverities = [11, 9, 9],
                name = 'PFRecHitQTestHCALChannel'
            ),
            dict(
                cuts = [dict(
                    depth = [1, 2],
                    detectorEnum = 4,
                    threshold = [1.2, 1.8]
                )],
                name = 'PFRecHitQTestHCALThresholdVsDepth',
                usePFThresholdsFromDB = False
            )
        ],
        src = ("hltHfreco"),
        thresh_HF = 0.4
    )]
)
