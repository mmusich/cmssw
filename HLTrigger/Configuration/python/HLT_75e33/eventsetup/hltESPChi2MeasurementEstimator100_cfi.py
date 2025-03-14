import FWCore.ParameterSet.Config as cms

from TrackingTools.KalmanUpdators.Chi2MeasurementEstimatorESProducer import Chi2MeasurementEstimatorESProducer as _Chi2MeasurementEstimatorESProducer

hltESPChi2MeasurementEstimator100 = _Chi2MeasurementEstimatorESProducer(
    ComponentName = cms.string('hltESPChi2MeasurementEstimator100'),
    MaxChi2 = cms.double(40.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1e+12),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(4.0)
)
