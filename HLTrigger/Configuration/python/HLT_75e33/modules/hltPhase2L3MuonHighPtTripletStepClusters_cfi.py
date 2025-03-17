import FWCore.ParameterSet.Config as cms

from RecoLocalTracker.SubCollectionProducers.TrackClusterRemoverPhase2 import TrackClusterRemoverPhase2 as _TrackClusterRemoverPhase2

hltPhase2L3MuonHighPtTripletStepClusters = _TrackClusterRemoverPhase2(
    TrackQuality = cms.string('highPurity'),
    maxChi2 = 9.0,
    mightGet = cms.optional.untracked.vstring,
    minNumberOfLayersWithMeasBeforeFiltering = 0,
    oldClusterRemovalInfo = (""),
    overrideTrkQuals = (""),
    phase2OTClusters = ("hltSiPhase2Clusters"),
    phase2pixelClusters = ("hltSiPixelClusters"),
    trackClassifier = ("","QualityMasks"),
    trajectories = ("hltPhase2L3MuonInitialStepTracksSelectionHighPurity")
)
