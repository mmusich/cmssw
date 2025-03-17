import FWCore.ParameterSet.Config as cms

from RecoTracker.FinalTrackSelectors.TrackListMerger import TrackListMerger as _TrackListMerger

hltGeneralTracks = _TrackListMerger(
    Epsilon = -0.001,
    FoundHitBonus = 5.0,
    LostHitPenalty = 5.0,
    MaxNormalizedChisq = 1000.0,
    MinFound = 3,
    MinPT = 0.9,
    ShareFrac = 0.19,
    TrackProducers = ["hltInitialStepTrackSelectionHighPurity", "hltHighPtTripletStepTrackSelectionHighPurity"],
    allowFirstHitShare = True,
    copyExtras = cms.untracked.bool(True),
    copyMVA = False,
    hasSelector = [0, 0],
    indivShareFrac = [1.0, 1.0],
    makeReKeyedSeeds = cms.untracked.bool(False),
    newQuality = 'confirmed',
    selectedTrackQuals = ["hltInitialStepTrackSelectionHighPurity", "hltHighPtTripletStepTrackSelectionHighPurity"],
    setsToMerge = [dict(
        pQual = True,
        tLists = [0, 1]
    )],
    trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder'),
    writeOnlyTrkQuals = False
)

_hltGeneralTracksSingleIterPatatrack = hltGeneralTracks.clone(
    TrackProducers = ["hltInitialStepTrackSelectionHighPurity"],
    hasSelector = [0],
    indivShareFrac = [1.0],
    selectedTrackQuals = ["hltInitialStepTrackSelectionHighPurity"],
    setsToMerge = [dict(
        pQual = True,
        tLists = [0]
    )]
)

from Configuration.ProcessModifiers.singleIterPatatrack_cff import singleIterPatatrack
singleIterPatatrack.toReplaceWith(hltGeneralTracks, _hltGeneralTracksSingleIterPatatrack)

_hltGeneralTracksLST = hltGeneralTracks.clone(
    TrackProducers = ["hltInitialStepTrackSelectionHighPuritypTTCLST", "hltInitialStepTrackSelectionHighPuritypLSTCLST", "hltInitialStepTracksT5TCLST", "hltHighPtTripletStepTrackSelectionHighPurity"],
    hasSelector = [0,0,0,0],
    indivShareFrac = [0.1,0.1,0.1,0.1],
    selectedTrackQuals = ["hltInitialStepTrackSelectionHighPuritypTTCLST", "hltInitialStepTrackSelectionHighPuritypLSTCLST", "hltInitialStepTracksT5TCLST", "hltHighPtTripletStepTrackSelectionHighPurity"],
    setsToMerge = [dict(
        pQual = True,
        tLists = [0,1,2,3]
    )]
)

from Configuration.ProcessModifiers.trackingLST_cff import trackingLST
trackingLST.toReplaceWith(hltGeneralTracks, _hltGeneralTracksLST)

_hltGeneralTracksLSTSingleIterPatatrack = hltGeneralTracks.clone(
    TrackProducers = ["hltInitialStepTrackSelectionHighPuritypTTCLST", "hltInitialStepTrackSelectionHighPuritypLSTCLST", "hltInitialStepTracksT5TCLST"],
    hasSelector = [0,0,0],
    indivShareFrac = [0.1,0.1,0.1],
    selectedTrackQuals = ["hltInitialStepTrackSelectionHighPuritypTTCLST", "hltInitialStepTrackSelectionHighPuritypLSTCLST", "hltInitialStepTracksT5TCLST"],
    setsToMerge = [dict(
        pQual = True,
        tLists = [0,1,2]
    )]
)

(singleIterPatatrack & trackingLST).toReplaceWith(hltGeneralTracks, _hltGeneralTracksLSTSingleIterPatatrack)

_hltGeneralTracksLSTSeeding = hltGeneralTracks.clone(
            TrackProducers = ["hltInitialStepTrackSelectionHighPuritypTTCLST", "hltInitialStepTracksT5TCLST", "hltHighPtTripletStepTrackSelectionHighPuritypLSTCLST"],
            hasSelector = [0,0,0],
            indivShareFrac = [0.1,0.1,0.1],
            selectedTrackQuals = ["hltInitialStepTrackSelectionHighPuritypTTCLST", "hltInitialStepTracksT5TCLST", "hltHighPtTripletStepTrackSelectionHighPuritypLSTCLST"],
            setsToMerge = [dict(
               pQual = True,
               tLists = [0,1,2]
            )]
    )

from Configuration.ProcessModifiers.seedingLST_cff import seedingLST
(seedingLST & trackingLST).toReplaceWith(hltGeneralTracks, _hltGeneralTracksLSTSeeding)
