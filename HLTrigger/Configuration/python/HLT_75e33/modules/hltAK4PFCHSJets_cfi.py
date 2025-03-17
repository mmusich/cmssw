import FWCore.ParameterSet.Config as cms

from RecoJets.JetProducers.FastjetJetProducer import FastjetJetProducer as _FastjetJetProducer

hltAK4PFCHSJets = _FastjetJetProducer(
    Active_Area_Repeats = 1,
    GhostArea = 0.01,
    Ghost_EtaMax = 5.0,
    Rho_EtaMax = 4.4,
    applyWeight = False,
    doAreaDiskApprox = False,
    doAreaFastjet = True,
    doPUOffsetCorr = False,
    doPVCorrection = False,
    doRhoFastjet = False,
    inputEMin = 0.0,
    inputEtMin = 0.0,
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = 5.0,
    jetType = cms.string('PFJet'),
    maxBadEcalCells = 9999999,
    maxBadHcalCells = 9999999,
    maxProblematicEcalCells = 9999999,
    maxProblematicHcalCells = 9999999,
    maxRecoveredEcalCells = 9999999,
    maxRecoveredHcalCells = 9999999,
    minSeed = 14327,
    rParam = 0.4,
    src = ("hltPfNoPileUpJME"),
    srcPVs = (""),
    useDeterministicSeed = True,
    voronoiRfact = -0.9
)
