import FWCore.ParameterSet.Config as cms

from TrackingTools.KalmanUpdators.Chi2MeasurementEstimatorESProducer import Chi2MeasurementEstimatorESProducer as _Chi2MeasurementEstimatorESProducer

hltESPChi2MeasurementEstimator100 = _Chi2MeasurementEstimatorESProducer(
    ComponentName = cms.string('hltESPChi2MeasurementEstimator100'),
    MaxChi2 = 40.0,
    MaxDisplacement = 0.5,
    MaxSagitta = 2.0,
    MinPtForHitRecoveryInGluedDet = 1e+12,
    MinimalTolerance = 0.5,
    appendToDataLabel = cms.string(''),
    nSigma = 4.0
)
