import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTHcalPFClusterIsolationProducer import EgammaHLTHcalPFClusterIsolationProducer as _EgammaHLTHcalPFClusterIsolationProducer

hltEgammaHcalPFClusterIsoUnseeded = _EgammaHLTHcalPFClusterIsolationProducer(
    absEtaLowEdges = [0.0, 1.479],
    doRhoCorrection = False,
    drMax = 0.3,
    drVetoBarrel = 0.0,
    drVetoEndcap = 0.0,
    effectiveAreas = [0.2, 0.25],
    energyBarrel = 0.0,
    energyEndcap = 0.0,
    etaStripBarrel = 0.0,
    etaStripEndcap = 0.0,
    pfClusterProducerHCAL = ("hltParticleFlowClusterHCAL"),
    pfClusterProducerHFEM = (""),
    pfClusterProducerHFHAD = (""),
    recoEcalCandidateProducer = ("hltEgammaCandidatesUnseeded"),
    rhoMax = 99999999.0,
    rhoProducer = ("hltFixedGridRhoFastjetAllCaloForEGamma"),
    rhoScale = 1.0,
    useEt = True,
    useHF = False
)
