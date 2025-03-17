import FWCore.ParameterSet.Config as cms

from RecoTracker.FinalTrackSelectors.TrackListMerger import TrackListMerger as _TrackListMerger

hltPhase2L3MuonMerged = _TrackListMerger(
    Epsilon = -0.001,
    FoundHitBonus = 5.0,
    LostHitPenalty = 20.0,
    MaxNormalizedChisq = 1000.0,
    MinFound = 3,
    MinPT = 0.05,
    ShareFrac = 0.19,
    TrackProducers = [
        "hltPhase2L3OIMuonTrackSelectionHighPurity",
        "hltIter2Phase2L3FromL1TkMuonMerged",
    ],
    allowFirstHitShare = True,
    copyExtras = cms.untracked.bool(True),
    copyMVA = False,
    hasSelector = [0, 0],
    indivShareFrac = [1.0, 1.0],
    newQuality = "confirmed",
    selectedTrackQuals = [
        "hltPhase2L3OIMuonTrackSelectionHighPurity",
        "hltIter2Phase2L3FromL1TkMuonMerged",
    ],
    setsToMerge = [dict(pQual = False, tLists = [0, 1])],
    trackAlgoPriorityOrder = "hltESPTrackAlgoPriorityOrder",
    writeOnlyTrkQuals = False,
)

from Configuration.ProcessModifiers.phase2L2AndL3Muons_cff import phase2L2AndL3Muons
phase2L2AndL3Muons.toModify(
    hltPhase2L3MuonMerged,
    TrackProducers = [
        "hltPhase2L3OIMuonTrackSelectionHighPurity",
        "hltPhase2L3MuonFilter:L3IOTracksFiltered",
    ],
    selectedTrackQuals = [
        "hltPhase2L3OIMuonTrackSelectionHighPurity",
        "hltPhase2L3MuonFilter:L3IOTracksFiltered",
    ],
)

from Configuration.ProcessModifiers.phase2L3MuonsOIFirst_cff import phase2L3MuonsOIFirst
(phase2L2AndL3Muons & phase2L3MuonsOIFirst).toModify(
    hltPhase2L3MuonMerged,
    TrackProducers = [
        "hltPhase2L3MuonFilter:L3OITracksFiltered",
        "hltIter2Phase2L3FromL1TkMuonMerged",
    ],
    selectedTrackQuals = [
        "hltPhase2L3MuonFilter:L3OITracksFiltered",
        "hltIter2Phase2L3FromL1TkMuonMerged",
    ],
)
