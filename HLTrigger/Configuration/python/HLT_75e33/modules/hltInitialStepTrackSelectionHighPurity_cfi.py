import FWCore.ParameterSet.Config as cms

from RecoTracker.FinalTrackSelectors.TrackCollectionFilterCloner import TrackCollectionFilterCloner as _TrackCollectionFilterCloner

hltInitialStepTrackSelectionHighPurity = _TrackCollectionFilterCloner(
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    minQuality = cms.string('highPurity'),
    originalMVAVals = ("hltInitialStepTrackCutClassifier","MVAValues"),
    originalQualVals = ("hltInitialStepTrackCutClassifier","QualityMasks"),
    originalSource = ("hltInitialStepTracks")
)
