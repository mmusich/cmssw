import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFClusterProducer.PFRecHitProducer import PFRecHitProducer as _PFRecHitProducer

hltParticleFlowRecHitECALL1Seeded = _PFRecHitProducer(
    navigator = dict(
        barrel = dict(

        ),
        endcap = dict(

        ),
        name = 'PFRecHitECALNavigator'
    ),
    producers = [
        dict(
            name = 'PFEBRecHitCreator',
            qualityTests = [
                dict(
                    applySelectionsToAllCrystals = True,
                    name = 'PFRecHitQTestDBThreshold'
                ),
                dict(
                    cleaningThreshold = 2.0,
                    name = 'PFRecHitQTestECAL',
                    skipTTRecoveredHits = True,
                    timingCleaning = True,
                    topologicalCleaning = True
                )
            ],
            srFlags = (""),
            src = ("hltRechitInRegionsECAL","EcalRecHitsEB")
        ),
        dict(
            name = 'PFEERecHitCreator',
            qualityTests = [
                dict(
                    applySelectionsToAllCrystals = True,
                    name = 'PFRecHitQTestDBThreshold'
                ),
                dict(
                    cleaningThreshold = 2.0,
                    name = 'PFRecHitQTestECAL',
                    skipTTRecoveredHits = True,
                    timingCleaning = True,
                    topologicalCleaning = True
                )
            ],
            srFlags = (""),
            src = ("hltRechitInRegionsECAL","EcalRecHitsEE")
        )
    ]
)
