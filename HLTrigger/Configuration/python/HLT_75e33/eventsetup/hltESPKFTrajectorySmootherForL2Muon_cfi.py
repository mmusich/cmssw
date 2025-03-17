import FWCore.ParameterSet.Config as cms

from TrackingTools.TrackFitters.KFTrajectorySmootherESProducer import KFTrajectorySmootherESProducer as _KFTrajectorySmootherESProducer

hltESPKFTrajectorySmootherForL2Muon = _KFTrajectorySmootherESProducer(
    ComponentName = cms.string('hltESPKFTrajectorySmootherForL2Muon'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = 100.0,
    minHits = 3
)
