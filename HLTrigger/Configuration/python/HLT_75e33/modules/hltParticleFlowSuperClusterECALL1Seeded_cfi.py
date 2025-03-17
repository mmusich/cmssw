import FWCore.ParameterSet.Config as cms

from RecoEcal.EgammaClusterProducers.PFECALSuperClusterProducer import PFECALSuperClusterProducer as _PFECALSuperClusterProducer

hltParticleFlowSuperClusterECALL1Seeded = _PFECALSuperClusterProducer(
    BeamSpot = ("hltOnlineBeamSpot"),
    ClusteringType = cms.string('Mustache'),
    ESAssociation = ("hltParticleFlowClusterECALL1Seeded"),
    EnergyWeight = cms.string('Raw'),
    PFBasicClusterCollectionBarrel = cms.string('particleFlowBasicClusterECALBarrel'),
    PFBasicClusterCollectionEndcap = cms.string('particleFlowBasicClusterECALEndcap'),
    PFBasicClusterCollectionPreshower = cms.string('particleFlowBasicClusterECALPreshower'),
    PFClusters = ("hltParticleFlowClusterECALL1Seeded"),
    PFSuperClusterCollectionBarrel = cms.string('particleFlowSuperClusterECALBarrel'),
    PFSuperClusterCollectionEndcap = cms.string('particleFlowSuperClusterECALEndcap'),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string('particleFlowSuperClusterECALEndcapWithPreshower'),
    applyCrackCorrections = False,
    barrelRecHits = ("hltRechitInRegionsECAL","EcalRecHitsEB"),
    doSatelliteClusterMerge = False,
    dropUnseedable = False,
    endcapRecHits = ("hltRechitInRegionsECAL","EcalRecHitsEE"),
    etawidth_SuperClusterBarrel = 0.04,
    etawidth_SuperClusterEndcap = 0.04,
    isOOTCollection = False,
    phiwidth_SuperClusterBarrel = 0.6,
    phiwidth_SuperClusterEndcap = 0.6,
    regressionConfig = dict(
        ecalRecHitsEB = ("hltEcalRecHitL1Seeded","EcalRecHitsEB"),
        ecalRecHitsEE = ("hltEcalRecHitL1Seeded","EcalRecHitsEE"),
        isHLT = True,
        regressionKeyEB = cms.string('pfscecal_EBCorrection_online'),
        regressionKeyEE = cms.string('pfscecal_EECorrection_online'),
        uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_online'),
        uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_online')
    ),
    satelliteClusterSeedThreshold = 50.0,
    satelliteMajorityFraction = 0.5,
    seedThresholdIsET = True,
    thresh_PFClusterBarrel = 0.5,
    thresh_PFClusterES = 0.5,
    thresh_PFClusterEndcap = 0.5,
    thresh_PFClusterSeedBarrel = 1.0,
    thresh_PFClusterSeedEndcap = 1.0,
    thresh_SCEt = 10.0,
    useDynamicDPhiWindow = True,
    useRegression = True,
    verbose = cms.untracked.bool(False)
)
