import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFSimProducer.EcalBarrelClusterFastTimer import EcalBarrelClusterFastTimer as _EcalBarrelClusterFastTimer

hltEcalBarrelClusterFastTimer = _EcalBarrelClusterFastTimer(
    ebClusters = cms.InputTag("hltParticleFlowClusterECALUncorrected"),
    ebTimeHits = cms.InputTag("hltEcalDetailedTimeRecHit","EcalRecHitsEB"),
    ecalDepth = cms.double(7.0),
    minEnergyToConsider = cms.double(0.0),
    minFractionToConsider = cms.double(0.1),
    resolutionModels = cms.VPSet(cms.PSet(
        modelName = cms.string('PerfectResolutionModel')
    )),
    timedVertices = cms.InputTag("hltOfflinePrimaryVertices4D")
)
