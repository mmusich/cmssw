import FWCore.ParameterSet.Config as cms

from RecoTracker.MeasurementDet.Chi2ChargeMeasurementEstimatorESProducer import Chi2ChargeMeasurementEstimatorESProducer as _Chi2ChargeMeasurementEstimatorESProducer

hltESPChi2ChargeMeasurementEstimator2000 = _Chi2ChargeMeasurementEstimatorESProducer(
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator2000'),
    MaxChi2 = 2000.0,
    MaxDisplacement = 100.0,
    MaxSagitta = -1.0,
    MinPtForHitRecoveryInGluedDet = 1000000.0,
    MinimalTolerance = 10.0,
    appendToDataLabel = cms.string(''),
    clusterChargeCut = dict(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    nSigma = 3.0,
    pTChargeCutThreshold = -1.0
)
