import FWCore.ParameterSet.Config as cms

from RecoLocalTracker.SubCollectionProducers.TrackClusterRemoverPhase2 import TrackClusterRemoverPhase2 as _TrackClusterRemoverPhase2

hltIter2Phase2L3FromL1TkMuonClustersRefRemoval = _TrackClusterRemoverPhase2(
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(16.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag(""),
    overrideTrkQuals = cms.InputTag(""),
    phase2OTClusters = cms.InputTag("hltSiPhase2Clusters"),
    phase2pixelClusters = cms.InputTag("hltSiPixelClusters"),
    trackClassifier = cms.InputTag("","QualityMasks"),
    trajectories = cms.InputTag("hltIter0Phase2L3FromL1TkMuonTrackSelectionHighPurity")
)
