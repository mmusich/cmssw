import FWCore.ParameterSet.Config as cms

from TrackingTools.TrackFitters.KFTrajectoryFitterESProducer import KFTrajectoryFitterESProducer as _KFTrajectoryFitterESProducer

hltESPL3MuKFTrajectoryFitter = _KFTrajectoryFitterESProducer(
    ComponentName = cms.string('hltESPL3MuKFTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPSmartPropagatorAny'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)
