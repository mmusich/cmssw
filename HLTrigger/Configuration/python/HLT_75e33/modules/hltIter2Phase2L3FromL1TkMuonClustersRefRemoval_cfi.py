import FWCore.ParameterSet.Config as cms

from RecoLocalTracker.SubCollectionProducers.TrackClusterRemoverPhase2 import TrackClusterRemoverPhase2 as _TrackClusterRemoverPhase2

hltIter2Phase2L3FromL1TkMuonClustersRefRemoval = _TrackClusterRemoverPhase2(
    TrackQuality = cms.string('highPurity'),
    maxChi2 = 16.0,
    minNumberOfLayersWithMeasBeforeFiltering = 0,
    oldClusterRemovalInfo = (""),
    overrideTrkQuals = (""),
    phase2OTClusters = ("hltSiPhase2Clusters"),
    phase2pixelClusters = ("hltSiPixelClusters"),
    trackClassifier = ("","QualityMasks"),
    trajectories = ("hltIter0Phase2L3FromL1TkMuonTrackSelectionHighPurity")
)
