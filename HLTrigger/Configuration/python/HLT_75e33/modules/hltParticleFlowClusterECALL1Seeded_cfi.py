import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFClusterProducer.CorrectedECALPFClusterProducer import CorrectedECALPFClusterProducer as _CorrectedECALPFClusterProducer

hltParticleFlowClusterECALL1Seeded = _CorrectedECALPFClusterProducer(
    energyCorrector = dict(
        applyCrackCorrections = False,
        applyMVACorrections = True,
        autoDetectBunchSpacing = True,
        bunchSpacing = 25,
        ebSrFlagLabel = ("hltEcalDigis"),
        eeSrFlagLabel = ("hltEcalDigis"),
        maxPtForMVAEvaluation = 300.0,
        recHitsEBLabel = ("hltRechitInRegionsECAL","EcalRecHitsEB"),
        recHitsEELabel = ("hltRechitInRegionsECAL","EcalRecHitsEE"),
        setEnergyUncertainty = False,
        srfAwareCorrection = True
    ),
    inputECAL = ("hltParticleFlowClusterECALUncorrectedL1Seeded"),
    mightGet = cms.optional.untracked.vstring,
    minimumPSEnergy = 0,
    skipPS = True
)
