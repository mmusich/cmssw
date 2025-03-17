import FWCore.ParameterSet.Config as cms

from RecoTracker.FinalTrackSelectors.TrackCollectionFilterCloner import TrackCollectionFilterCloner as _TrackCollectionFilterCloner

hltPhase2L3MuonInitialStepTracksSelectionHighPurity = _TrackCollectionFilterCloner(
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    minQuality = cms.string('highPurity'),
    originalMVAVals = ("hltPhase2L3MuonInitialStepTrackCutClassifier","MVAValues"),
    originalQualVals = ("hltPhase2L3MuonInitialStepTrackCutClassifier","QualityMasks"),
    originalSource = ("hltPhase2L3MuonInitialStepTracks")
)
