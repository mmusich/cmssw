import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFClusterProducer.CorrectedECALPFClusterProducer import CorrectedECALPFClusterProducer as _CorrectedECALPFClusterProducer

hltParticleFlowClusterECAL = _CorrectedECALPFClusterProducer(
    energyCorrector = dict(
        applyCrackCorrections = False,
        applyMVACorrections = True,
        autoDetectBunchSpacing = True,
        bunchSpacing = 25,
        ebSrFlagLabel = ("hltEcalDigis"),
        eeSrFlagLabel = ("hltEcalDigis"),
        maxPtForMVAEvaluation = 300.0,
        recHitsEBLabel = ("hltEcalRecHit","EcalRecHitsEB"),
        recHitsEELabel = ("hltEcalRecHit","EcalRecHitsEE"),
        setEnergyUncertainty = False,
        srfAwareCorrection = True
    ),
    inputECAL = ("hltParticleFlowTimeAssignerECAL"),
    mightGet = cms.optional.untracked.vstring,
    minimumPSEnergy = 0,
    skipPS = True
)
