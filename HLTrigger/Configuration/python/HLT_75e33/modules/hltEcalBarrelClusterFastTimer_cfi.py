import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFSimProducer.EcalBarrelClusterFastTimer import EcalBarrelClusterFastTimer as _EcalBarrelClusterFastTimer

hltEcalBarrelClusterFastTimer = _EcalBarrelClusterFastTimer(
    ebClusters = ("hltParticleFlowClusterECALUncorrected"),
    ebTimeHits = ("hltEcalDetailedTimeRecHit","EcalRecHitsEB"),
    ecalDepth = 7.0,
    minEnergyToConsider = 0.0,
    minFractionToConsider = 0.1,
    resolutionModels = [dict(
        modelName = 'PerfectResolutionModel'
    )],
    timedVertices = ("hltOfflinePrimaryVertices4D")
)
