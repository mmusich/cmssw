import FWCore.ParameterSet.Config as cms

from RecoTracker.FinalTrackSelectors.TrackListMerger import TrackListMerger as _TrackListMerger

hltIter2Phase2L3FromL1TkMuonMerged = _TrackListMerger(
    Epsilon = -0.001,
    FoundHitBonus = 5.0,
    LostHitPenalty = 20.0,
    MaxNormalizedChisq = 1000.0,
    MinFound = 3,
    MinPT = 0.05,
    ShareFrac = 0.19,
    TrackProducers = ["hltIter0Phase2L3FromL1TkMuonTrackSelectionHighPurity", "hltIter2Phase2L3FromL1TkMuonTrackSelectionHighPurity"],
    allowFirstHitShare = True,
    copyExtras = cms.untracked.bool(True),
    copyMVA = False,
    hasSelector = [0, 0],
    indivShareFrac = [1.0, 1.0],
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = ["hltIter0Phase2L3FromL1TkMuonTrackSelectionHighPurity", "hltIter2Phase2L3FromL1TkMuonTrackSelectionHighPurity"],
    setsToMerge = [dict(
        pQual = False,
        tLists = [0, 1]
    )],
    trackAlgoPriorityOrder = cms.string('hltESPTrackAlgoPriorityOrder'),
    writeOnlyTrkQuals = False
)
