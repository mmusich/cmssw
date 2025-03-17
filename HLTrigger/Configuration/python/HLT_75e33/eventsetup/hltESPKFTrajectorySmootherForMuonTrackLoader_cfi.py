import FWCore.ParameterSet.Config as cms

from TrackingTools.TrackFitters.KFTrajectorySmootherESProducer import KFTrajectorySmootherESProducer as _KFTrajectorySmootherESProducer

hltESPKFTrajectorySmootherForMuonTrackLoader = _KFTrajectorySmootherESProducer(
    ComponentName = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPSmartPropagatorAnyOpposite'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = 10.0,
    minHits = 3
)
