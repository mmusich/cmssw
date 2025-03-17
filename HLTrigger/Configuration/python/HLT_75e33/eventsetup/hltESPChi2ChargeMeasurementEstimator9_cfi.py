import FWCore.ParameterSet.Config as cms

from RecoTracker.MeasurementDet.Chi2ChargeMeasurementEstimatorESProducer import Chi2ChargeMeasurementEstimatorESProducer as _Chi2ChargeMeasurementEstimatorESProducer

hltESPChi2ChargeMeasurementEstimator9 = _Chi2ChargeMeasurementEstimatorESProducer(
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    MaxChi2 = 9.0,
    MaxDisplacement = 0.5,
    MaxSagitta = 2.0,
    MinPtForHitRecoveryInGluedDet = 1000000.0,
    MinimalTolerance = 0.5,
    appendToDataLabel = cms.string(''),
    clusterChargeCut = dict(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = 3.0,
    pTChargeCutThreshold = 15.0
)
