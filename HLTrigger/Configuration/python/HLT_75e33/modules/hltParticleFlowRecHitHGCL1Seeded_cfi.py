import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFClusterProducer.PFRecHitProducer import PFRecHitProducer as _PFRecHitProducer

hltParticleFlowRecHitHGCL1Seeded = _PFRecHitProducer(
    navigator = dict(
        hgcee = dict(
            name = 'PFRecHitHGCEENavigator',
            topologySource = 'HGCalEESensitive'
        ),
        hgcheb = dict(
            name = 'PFRecHitHGCHENavigator',
            topologySource = 'HGCalHEScintillatorSensitive'
        ),
        hgchef = dict(
            name = 'PFRecHitHGCHENavigator',
            topologySource = 'HGCalHESiliconSensitive'
        ),
        name = 'PFRecHitHGCNavigator'
    ),
    producers = [
        dict(
            geometryInstance = 'HGCalEESensitive',
            name = 'PFHGCalEERecHitCreator',
            qualityTests = [dict(
                name = 'PFRecHitQTestHGCalThresholdSNR',
                thresholdSNR = 5.0
            )],
            src = ("hltHGCalRecHitL1Seeded","HGCEERecHits")
        ),
        dict(
            geometryInstance = 'HGCalHESiliconSensitive',
            name = 'PFHGCalHSiRecHitCreator',
            qualityTests = [dict(
                name = 'PFRecHitQTestHGCalThresholdSNR',
                thresholdSNR = 5.0
            )],
            src = ("hltHGCalRecHitL1Seeded","HGCHEFRecHits")
        ),
        dict(
            geometryInstance = '',
            name = 'PFHGCalHScRecHitCreator',
            qualityTests = [dict(
                name = 'PFRecHitQTestHGCalThresholdSNR',
                thresholdSNR = 5.0
            )],
            src = ("hltHGCalRecHitL1Seeded","HGCHEBRecHits")
        )
    ]
)
