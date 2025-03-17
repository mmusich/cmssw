import FWCore.ParameterSet.Config as cms

from TrackingTools.Producers.SmartPropagatorESProducer import SmartPropagatorESProducer as _SmartPropagatorESProducer

hltESPSmartPropagator = _SmartPropagatorESProducer(
    ComponentName = cms.string('hltESPSmartPropagator'),
    Epsilon = 5.0,
    MuonPropagator = cms.string('hltESPSteppingHelixPropagatorAlong'),
    PropagationDirection = cms.string('alongMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterial')
)
