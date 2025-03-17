import FWCore.ParameterSet.Config as cms

from TrackingTools.Producers.SmartPropagatorESProducer import SmartPropagatorESProducer as _SmartPropagatorESProducer

hltESPSmartPropagatorAnyOpposite = _SmartPropagatorESProducer(
    ComponentName = cms.string('hltESPSmartPropagatorAnyOpposite'),
    Epsilon = 5.0,
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterialOpposite')
)
