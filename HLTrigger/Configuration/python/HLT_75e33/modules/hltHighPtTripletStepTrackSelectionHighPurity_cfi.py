import FWCore.ParameterSet.Config as cms

from RecoTracker.FinalTrackSelectors.TrackCollectionFilterCloner import TrackCollectionFilterCloner as _TrackCollectionFilterCloner

hltHighPtTripletStepTrackSelectionHighPurity = _TrackCollectionFilterCloner(
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    minQuality = cms.string('highPurity'),
    originalMVAVals = cms.InputTag("hltHighPtTripletStepTrackCutClassifier","MVAValues"),
    originalQualVals = cms.InputTag("hltHighPtTripletStepTrackCutClassifier","QualityMasks"),
    originalSource = cms.InputTag("hltHighPtTripletStepTracks")
)
