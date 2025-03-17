import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFClusterProducer.PFRecHitProducer import PFRecHitProducer as _PFRecHitProducer

hltParticleFlowRecHitHGCL1Seeded = _PFRecHitProducer(
    navigator = cms.PSet(
        hgcee = cms.PSet(
            name = cms.string('PFRecHitHGCEENavigator'),
            topologySource = cms.string('HGCalEESensitive')
        ),
        hgcheb = cms.PSet(
            name = cms.string('PFRecHitHGCHENavigator'),
            topologySource = cms.string('HGCalHEScintillatorSensitive')
        ),
        hgchef = cms.PSet(
            name = cms.string('PFRecHitHGCHENavigator'),
            topologySource = cms.string('HGCalHESiliconSensitive')
        ),
        name = cms.string('PFRecHitHGCNavigator')
    ),
    producers = cms.VPSet(
        cms.PSet(
            geometryInstance = cms.string('HGCalEESensitive'),
            name = cms.string('PFHGCalEERecHitCreator'),
            qualityTests = cms.VPSet(cms.PSet(
                name = cms.string('PFRecHitQTestHGCalThresholdSNR'),
                thresholdSNR = cms.double(5.0)
            )),
            src = cms.InputTag("hltHGCalRecHitL1Seeded","HGCEERecHits")
        ),
        cms.PSet(
            geometryInstance = cms.string('HGCalHESiliconSensitive'),
            name = cms.string('PFHGCalHSiRecHitCreator'),
            qualityTests = cms.VPSet(cms.PSet(
                name = cms.string('PFRecHitQTestHGCalThresholdSNR'),
                thresholdSNR = cms.double(5.0)
            )),
            src = cms.InputTag("hltHGCalRecHitL1Seeded","HGCHEFRecHits")
        ),
        cms.PSet(
            geometryInstance = cms.string(''),
            name = cms.string('PFHGCalHScRecHitCreator'),
            qualityTests = cms.VPSet(cms.PSet(
                name = cms.string('PFRecHitQTestHGCalThresholdSNR'),
                thresholdSNR = cms.double(5.0)
            )),
            src = cms.InputTag("hltHGCalRecHitL1Seeded","HGCHEBRecHits")
        )
    )
)
