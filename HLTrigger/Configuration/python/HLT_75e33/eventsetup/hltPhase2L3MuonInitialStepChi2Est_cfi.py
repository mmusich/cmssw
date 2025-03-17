import FWCore.ParameterSet.Config as cms

from RecoTracker.MeasurementDet.Chi2ChargeMeasurementEstimatorESProducer import Chi2ChargeMeasurementEstimatorESProducer as _Chi2ChargeMeasurementEstimatorESProducer

hltPhase2L3MuonInitialStepChi2Est = _Chi2ChargeMeasurementEstimatorESProducer(
    ComponentName = cms.string('hltPhase2L3MuonInitialStepChi2Est'),
    MaxChi2 = 9.0,
    MaxDisplacement = 0.5,
    MaxSagitta = 2,
    MinPtForHitRecoveryInGluedDet = 1000000.0,
    MinimalTolerance = 0.5,
    appendToDataLabel = cms.string(''),
    clusterChargeCut = dict(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    nSigma = 3.0,
    pTChargeCutThreshold = 15.0
)
