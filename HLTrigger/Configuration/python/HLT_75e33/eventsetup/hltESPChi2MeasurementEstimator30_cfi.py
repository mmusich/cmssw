import FWCore.ParameterSet.Config as cms

from TrackingTools.KalmanUpdators.Chi2MeasurementEstimatorESProducer import Chi2MeasurementEstimatorESProducer as _Chi2MeasurementEstimatorESProducer

hltESPChi2MeasurementEstimator30 = _Chi2MeasurementEstimatorESProducer(
    ComponentName = cms.string('hltESPChi2MeasurementEstimator30'),
    MaxChi2 = 30.0,
    MaxDisplacement = 100.0,
    MaxSagitta = -1.0,
    MinPtForHitRecoveryInGluedDet = 1000000.0,
    MinimalTolerance = 10.0,
    appendToDataLabel = cms.string(''),
    nSigma = 3.0
)
