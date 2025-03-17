import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFClusterProducer.PFClusterTimeAssigner import PFClusterTimeAssigner as _PFClusterTimeAssigner

hltParticleFlowTimeAssignerECAL = _PFClusterTimeAssigner(
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("hltParticleFlowClusterECALUncorrected"),
    timeResoSrc = cms.InputTag("hltEcalBarrelClusterFastTimer","PerfectResolutionModelResolution"),
    timeSrc = cms.InputTag("hltEcalBarrelClusterFastTimer","PerfectResolutionModel")
)
