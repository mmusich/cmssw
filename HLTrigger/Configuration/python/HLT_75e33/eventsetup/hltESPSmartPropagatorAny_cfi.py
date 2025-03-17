import FWCore.ParameterSet.Config as cms

from TrackingTools.Producers.SmartPropagatorESProducer import SmartPropagatorESProducer as _SmartPropagatorESProducer

hltESPSmartPropagatorAny = _SmartPropagatorESProducer(
    ComponentName = cms.string('hltESPSmartPropagatorAny'),
    Epsilon = 5.0,
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('alongMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterial')
)
