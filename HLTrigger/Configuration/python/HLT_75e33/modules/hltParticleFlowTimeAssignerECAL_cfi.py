import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFClusterProducer.PFClusterTimeAssigner import PFClusterTimeAssigner as _PFClusterTimeAssigner

hltParticleFlowTimeAssignerECAL = _PFClusterTimeAssigner(
    mightGet = cms.optional.untracked.vstring,
    src = ("hltParticleFlowClusterECALUncorrected"),
    timeResoSrc = ("hltEcalBarrelClusterFastTimer","PerfectResolutionModelResolution"),
    timeSrc = ("hltEcalBarrelClusterFastTimer","PerfectResolutionModel")
)
