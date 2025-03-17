import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTHGCalLayerClusterIsolationProducer import EgammaHLTHGCalLayerClusterIsolationProducer as _EgammaHLTHGCalLayerClusterIsolationProducer

hltEgammaHGCalLayerClusterIsoL1Seeded = _EgammaHLTHGCalLayerClusterIsolationProducer(
    doRhoCorrection = False,
    drMax = 0.2,
    drVetoEM = 0.02,
    drVetoHad = 0.0,
    layerClusterProducer = ("hltHgcalMergeLayerClustersL1Seeded"),
    minEnergyEM = 0.02,
    minEnergyHad = 0.07,
    recoEcalCandidateProducer = ("hltEgammaCandidatesL1Seeded"),
    rhoMax = 99999999.0,
    rhoScale = 1.0,
    useEt = False
)
