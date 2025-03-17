import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.MuonHLTHcalPFClusterIsolationProducer import MuonHLTHcalPFClusterIsolationProducer as _MuonHLTHcalPFClusterIsolationProducer

hltPhase2L3MuonsHcalIsodR0p3dRVeto0p000 = _MuonHLTHcalPFClusterIsolationProducer(
    absEtaLowEdges = [0.0, 1.479],
    doRhoCorrection = False,
    drMax = 0.3,
    drVetoBarrel = 0.0,
    drVetoEndcap = 0.0,
    effectiveAreas = [0.227, 0.372],
    energyBarrel = 0.0,
    energyEndcap = 0.0,
    etaStripBarrel = 0.0,
    etaStripEndcap = 0.0,
    pfClusterProducerHCAL = ("hltParticleFlowClusterHCAL"),
    pfClusterProducerHFEM = (""),
    pfClusterProducerHFHAD = (""),
    recoCandidateProducer = ("hltPhase2L3MuonCandidates"),
    rhoMax = 99999999.0,
    rhoProducer = ("hltFixedGridRhoFastjetAllCaloForEGamma"),
    rhoScale = 1.0,
    useEt = True,
    useHF = False
)
