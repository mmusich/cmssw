import FWCore.ParameterSet.Config as cms

from RecoTracker.FinalTrackSelectors.TrackCollectionFilterCloner import TrackCollectionFilterCloner as _TrackCollectionFilterCloner

hltIter2Phase2L3FromL1TkMuonTrackSelectionHighPurity = _TrackCollectionFilterCloner(
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    minQuality = cms.string('highPurity'),
    originalMVAVals = ("hltIter2Phase2L3FromL1TkMuonTrackCutClassifier","MVAValues"),
    originalQualVals = ("hltIter2Phase2L3FromL1TkMuonTrackCutClassifier","QualityMasks"),
    originalSource = ("hltIter2Phase2L3FromL1TkMuonCtfWithMaterialTracks")
)
