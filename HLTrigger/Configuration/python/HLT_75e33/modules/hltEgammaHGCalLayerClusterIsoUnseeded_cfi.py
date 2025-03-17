import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTHGCalLayerClusterIsolationProducer import EgammaHLTHGCalLayerClusterIsolationProducer as _EgammaHLTHGCalLayerClusterIsolationProducer

hltEgammaHGCalLayerClusterIsoUnseeded = _EgammaHLTHGCalLayerClusterIsolationProducer(
    doRhoCorrection = False,
    drMax = 0.2,
    drVetoEM = 0.02,
    drVetoHad = 0.0,
    layerClusterProducer = ("hltHgcalMergeLayerClusters"),
    minEnergyEM = 0.02,
    minEnergyHad = 0.07,
    recoEcalCandidateProducer = ("hltEgammaCandidatesUnseeded"),
    rhoMax = 99999999.0,
    rhoScale = 1.0,
    useEt = False
)
