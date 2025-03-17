import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.MuonHLTEcalPFClusterIsolationProducer import MuonHLTEcalPFClusterIsolationProducer as _MuonHLTEcalPFClusterIsolationProducer

hltPhase2L3MuonsEcalIsodR0p3dRVeto0p000 = _MuonHLTEcalPFClusterIsolationProducer(
    absEtaLowEdges = [0.0, 1.479],
    doRhoCorrection = False,
    drMax = 0.3,
    drVetoBarrel = 0.0,
    drVetoEndcap = 0.0,
    effectiveAreas = [0.35, 0.193],
    energyBarrel = 0.0,
    energyEndcap = 0.0,
    etaStripBarrel = 0.0,
    etaStripEndcap = 0.0,
    pfClusterProducer = ("hltParticleFlowClusterECALUnseeded"),
    recoCandidateProducer = ("hltPhase2L3MuonCandidates"),
    rhoMax = 99999999.0,
    rhoProducer = ("hltFixedGridRhoFastjetAllCaloForEGamma"),
    rhoScale = 1.0
)
