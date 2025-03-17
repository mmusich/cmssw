import FWCore.ParameterSet.Config as cms

from RecoTracker.FinalTrackSelectors.TrackListMerger import TrackListMerger as _TrackListMerger

hltPhase2L3MuonGeneralTracks = _TrackListMerger(
    Epsilon = -0.001,
    FoundHitBonus = 5.0,
    LostHitPenalty = 5.0,
    MaxNormalizedChisq = 1000.0,
    MinFound = 3,
    MinPT = 0.9,
    ShareFrac = 0.19,
    TrackProducers = ["hltPhase2L3MuonInitialStepTracksSelectionHighPurity", "hltPhase2L3MuonHighPtTripletStepTracksSelectionHighPurity"],
    allowFirstHitShare = True,
    copyExtras = True,
    copyMVA = False,
    hasSelector = [0, 0],
    indivShareFrac = [1.0, 1.0],
    makeReKeyedSeeds = False,
    newQuality = 'confirmed',
    selectedTrackQuals = [("hltPhase2L3MuonInitialStepTracksSelectionHighPurity"), ("hltPhase2L3MuonHighPtTripletStepTracksSelectionHighPurity")],
    setsToMerge = [dict(
        pQual = True,
        tLists = [0, 1]
    )],
    trackAlgoPriorityOrder = 'hltPhase2L3MuonTrackAlgoPriorityOrder',
    writeOnlyTrkQuals = False
)
