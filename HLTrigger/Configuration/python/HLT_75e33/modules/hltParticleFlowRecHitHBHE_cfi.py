import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFClusterProducer.PFRecHitProducer import PFRecHitProducer as _PFRecHitProducer

hltParticleFlowRecHitHBHE = _PFRecHitProducer(
    navigator = dict(
        hcalEnums = [1, 2],
        name = 'PFRecHitHCALDenseIdNavigator'
    ),
    producers = [dict(
        name = 'PFHBHERecHitCreator',
        qualityTests = [
            dict(
                cuts = [
                    dict(
                        depth = [1, 2, 3, 4],
                        detectorEnum = 1,
                        threshold = [0.1, 0.2, 0.3, 0.3]
                    ),
                    dict(
                        depth = [
                            1, 2, 3, 4, 5,
                            6, 7
                        ],
                        detectorEnum = 2,
                        threshold = [
                            0.1, 0.2, 0.2, 0.2, 0.2,
                            0.2, 0.2
                        ]
                    )
                ],
                name = 'PFRecHitQTestHCALThresholdVsDepth',
                usePFThresholdsFromDB = True
            ),
            dict(
                cleaningThresholds = [0.0],
                flags = ['Standard'],
                maxSeverities = [11],
                name = 'PFRecHitQTestHCALChannel'
            )
        ],
        src = ("hltHbhereco")
    )]
)
