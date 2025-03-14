import FWCore.ParameterSet.Config as cms

from RecoTracker.FinalTrackSelectors.TrackAlgoPriorityOrderESProducer import TrackAlgoPriorityOrderESProducer as _TrackAlgoPriorityOrderESProducer

hltESPTrackAlgoPriorityOrder = _TrackAlgoPriorityOrderESProducer(
    ComponentName = cms.string('hltESPTrackAlgoPriorityOrder'),
    algoOrder = cms.vstring(),
    appendToDataLabel = cms.string('')
)
