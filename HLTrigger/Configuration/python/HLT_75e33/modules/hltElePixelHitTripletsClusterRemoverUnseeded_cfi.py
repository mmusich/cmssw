import FWCore.ParameterSet.Config as cms

from RecoLocalTracker.SubCollectionProducers.SeedClusterRemoverPhase2 import SeedClusterRemoverPhase2 as _SeedClusterRemoverPhase2

hltElePixelHitTripletsClusterRemoverUnseeded = _SeedClusterRemoverPhase2(
    phase2OTClusters = cms.InputTag("hltSiPhase2Clusters"),
    pixelClusters = cms.InputTag("hltSiPixelClusters"),
    trajectories = cms.InputTag("hltElePixelSeedsTripletsUnseeded")
)
