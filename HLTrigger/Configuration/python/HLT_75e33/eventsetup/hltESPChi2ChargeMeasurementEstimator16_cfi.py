import FWCore.ParameterSet.Config as cms

from RecoTracker.MeasurementDet.Chi2ChargeMeasurementEstimatorESProducer import Chi2ChargeMeasurementEstimatorESProducer as _Chi2ChargeMeasurementEstimatorESProducer

hltESPChi2ChargeMeasurementEstimator16 = _Chi2ChargeMeasurementEstimatorESProducer(
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    MaxChi2 = 16.0,
    MaxDisplacement = 0.5,
    MaxSagitta = 2.0,
    MinPtForHitRecoveryInGluedDet = 1000000.0,
    MinimalTolerance = 0.5,
    appendToDataLabel = cms.string(''),
    clusterChargeCut = dict(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = 3.0,
    pTChargeCutThreshold = -1.0
)
