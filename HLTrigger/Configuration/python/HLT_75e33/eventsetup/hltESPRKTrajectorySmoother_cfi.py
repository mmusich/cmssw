import FWCore.ParameterSet.Config as cms

from TrackingTools.TrackFitters.KFTrajectorySmootherESProducer import KFTrajectorySmootherESProducer as _KFTrajectorySmootherESProducer

hltESPRKTrajectorySmoother = _KFTrajectorySmootherESProducer(
    ComponentName = cms.string('hltESPRKTrajectorySmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = 100.0,
    minHits = 3
)
