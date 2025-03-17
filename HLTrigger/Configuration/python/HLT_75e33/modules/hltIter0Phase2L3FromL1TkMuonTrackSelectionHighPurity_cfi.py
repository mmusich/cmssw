import FWCore.ParameterSet.Config as cms

from RecoTracker.FinalTrackSelectors.TrackCollectionFilterCloner import TrackCollectionFilterCloner as _TrackCollectionFilterCloner

hltIter0Phase2L3FromL1TkMuonTrackSelectionHighPurity = _TrackCollectionFilterCloner(
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    minQuality = cms.string('highPurity'),
    originalMVAVals = cms.InputTag("hltIter0Phase2L3FromL1TkMuonTrackCutClassifier","MVAValues"),
    originalQualVals = cms.InputTag("hltIter0Phase2L3FromL1TkMuonTrackCutClassifier","QualityMasks"),
    originalSource = cms.InputTag("hltIter0Phase2L3FromL1TkMuonCtfWithMaterialTracks")
)
