import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTEcalPFClusterIsolationProducer import EgammaHLTEcalPFClusterIsolationProducer as _EgammaHLTEcalPFClusterIsolationProducer

hltEgammaEcalPFClusterIsoL1Seeded = _EgammaHLTEcalPFClusterIsolationProducer(
    absEtaLowEdges = [0.0, 1.479],
    doRhoCorrection = False,
    drMax = 0.2,
    drVetoBarrel = 0.0,
    drVetoEndcap = 0.0,
    effectiveAreas = [0.29, 0.21],
    energyBarrel = 0.0,
    energyEndcap = 0.0,
    etaStripBarrel = 0.0,
    etaStripEndcap = 0.0,
    pfClusterProducer = ("hltParticleFlowClusterECALL1Seeded"),
    recoEcalCandidateProducer = ("hltEgammaCandidatesL1Seeded"),
    rhoMax = 99999999.0,
    rhoProducer = ("hltFixedGridRhoFastjetAllCaloForEGamma"),
    rhoScale = 1.0
)
