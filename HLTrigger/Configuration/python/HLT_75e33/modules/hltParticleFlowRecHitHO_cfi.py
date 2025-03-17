import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFClusterProducer.PFRecHitProducer import PFRecHitProducer as _PFRecHitProducer

hltParticleFlowRecHitHO = _PFRecHitProducer(
    navigator = dict(
        hcalEnums = [3],
        name = 'PFRecHitHCALDenseIdNavigator'
    ),
    producers = [dict(
        name = 'PFHORecHitCreator',
        qualityTests = [
            dict(
                name = 'PFRecHitQTestThreshold',
                threshold = 0.05
            ),
            dict(
                cleaningThresholds = [0.0],
                flags = ['Standard'],
                maxSeverities = [11],
                name = 'PFRecHitQTestHCALChannel'
            )
        ],
        src = ("hltHoreco")
    )
  ]
)
