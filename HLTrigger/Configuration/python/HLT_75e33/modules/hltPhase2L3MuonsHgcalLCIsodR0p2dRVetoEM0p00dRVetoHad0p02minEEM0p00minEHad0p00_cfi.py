import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.MuonHLTHGCalLayerClusterIsolationProducer import MuonHLTHGCalLayerClusterIsolationProducer as _MuonHLTHGCalLayerClusterIsolationProducer

hltPhase2L3MuonsHgcalLCIsodR0p2dRVetoEM0p00dRVetoHad0p02minEEM0p00minEHad0p00 = _MuonHLTHGCalLayerClusterIsolationProducer(
    doRhoCorrection = False,
    drMax = 0.2,
    drVetoEM = 0.0,
    drVetoHad = 0.02,
    effectiveAreas = [0.0, 0.0],
    layerClusterProducer = ("hltHgcalMergeLayerClusters"),
    minEnergyEM = 0.0,
    minEnergyHad = 0.0,
    minEtEM = 0.0,
    minEtHad = 0.0,
    recoCandidateProducer = ("hltPhase2L3MuonCandidates"),
    rhoMax = 99999999.0,
    rhoProducer = ("hltFixedGridRhoFastjetAllCaloForEGamma"),
    rhoScale = 1.0,
    useEt = False
)
