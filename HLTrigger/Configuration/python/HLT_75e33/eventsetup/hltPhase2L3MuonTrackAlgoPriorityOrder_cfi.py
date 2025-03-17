import FWCore.ParameterSet.Config as cms

from RecoTracker.FinalTrackSelectors.TrackAlgoPriorityOrderESProducer import TrackAlgoPriorityOrderESProducer as _TrackAlgoPriorityOrderESProducer

hltPhase2L3MuonTrackAlgoPriorityOrder = _TrackAlgoPriorityOrderESProducer(
    ComponentName = cms.string('hltPhase2L3MuonTrackAlgoPriorityOrder'),
    algoOrder = cms.vstring(
        'initialStep',
        'highPtTripletStep'
    ),
    appendToDataLabel = cms.string('')
)
