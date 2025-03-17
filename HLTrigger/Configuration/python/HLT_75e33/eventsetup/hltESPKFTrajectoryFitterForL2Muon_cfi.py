import FWCore.ParameterSet.Config as cms

from TrackingTools.TrackFitters.KFTrajectoryFitterESProducer import KFTrajectoryFitterESProducer as _KFTrajectoryFitterESProducer

hltESPKFTrajectoryFitterForL2Muon = _KFTrajectoryFitterESProducer(
    ComponentName = cms.string('hltESPKFTrajectoryFitterForL2Muon'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = 3
)
