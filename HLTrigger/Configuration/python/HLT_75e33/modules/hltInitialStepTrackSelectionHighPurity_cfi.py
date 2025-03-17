import FWCore.ParameterSet.Config as cms

from RecoTracker.FinalTrackSelectors.TrackCollectionFilterCloner import TrackCollectionFilterCloner as _TrackCollectionFilterCloner

hltInitialStepTrackSelectionHighPurity = _TrackCollectionFilterCloner(
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    minQuality = cms.string('highPurity'),
    originalMVAVals = cms.InputTag("hltInitialStepTrackCutClassifier","MVAValues"),
    originalQualVals = cms.InputTag("hltInitialStepTrackCutClassifier","QualityMasks"),
    originalSource = cms.InputTag("hltInitialStepTracks")
)
