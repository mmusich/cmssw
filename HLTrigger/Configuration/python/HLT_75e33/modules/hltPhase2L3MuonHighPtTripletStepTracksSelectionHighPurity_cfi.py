import FWCore.ParameterSet.Config as cms

from RecoTracker.FinalTrackSelectors.TrackCollectionFilterCloner import TrackCollectionFilterCloner as _TrackCollectionFilterCloner

hltPhase2L3MuonHighPtTripletStepTracksSelectionHighPurity = _TrackCollectionFilterCloner(
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    minQuality = cms.string('highPurity'),
    originalMVAVals = ("hltPhase2L3MuonHighPtTripletStepTrackCutClassifier","MVAValues"),
    originalQualVals = ("hltPhase2L3MuonHighPtTripletStepTrackCutClassifier","QualityMasks"),
    originalSource = ("hltPhase2L3MuonHighPtTripletStepTracks")
)
