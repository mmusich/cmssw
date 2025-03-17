import FWCore.ParameterSet.Config as cms

from RecoTracker.MeasurementDet.Chi2ChargeMeasurementEstimatorESProducer import Chi2ChargeMeasurementEstimatorESProducer as _Chi2ChargeMeasurementEstimatorESProducer

highPtTripletStepChi2Est = _Chi2ChargeMeasurementEstimatorESProducer(
    ComponentName = cms.string('highPtTripletStepChi2Est'),
    MaxChi2 = 16.0,
    MaxDisplacement = 0.5,
    MaxSagitta = 2,
    MinPtForHitRecoveryInGluedDet = 1000000.0,
    MinimalTolerance = 0.5,
    appendToDataLabel = cms.string(''),
    clusterChargeCut = dict(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    nSigma = 3,
    pTChargeCutThreshold = -1
)
