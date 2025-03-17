import FWCore.ParameterSet.Config as cms

from RecoJets.JetProducers.FastjetJetProducer import FastjetJetProducer as _FastjetJetProducer

hltAk4CaloJetsForTrk = _FastjetJetProducer(
    Active_Area_Repeats = 1,
    GhostArea = 0.01,
    Ghost_EtaMax = 5.0,
    Rho_EtaMax = 4.4,
    doAreaDiskApprox = False,
    doAreaFastjet = False,
    doPUOffsetCorr = False,
    doPVCorrection = True,
    doRhoFastjet = False,
    inputEMin = 0.0,
    inputEtMin = 0.3,
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = 10.0,
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = 9999999,
    maxBadHcalCells = 9999999,
    maxProblematicEcalCells = 9999999,
    maxProblematicHcalCells = 9999999,
    maxRecoveredEcalCells = 9999999,
    maxRecoveredHcalCells = 9999999,
    minSeed = 14327,
    nSigmaPU = 1.0,
    puPtMin = 10,
    rParam = 0.4,
    radiusPU = 0.5,
    src = ("hltPhase2TowerMakerForAll"),
    srcPVs = ("hltFirstStepPrimaryVerticesUnsorted"),
    useDeterministicSeed = True,
    voronoiRfact = -0.9
)
