import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTHGCalIDVarProducer import EgammaHLTHGCalIDVarProducer as _EgammaHLTHGCalIDVarProducer

hltEgammaHGCALIDVarsL1Seeded = _EgammaHLTHGCalIDVarProducer(
    hgcalRecHits = ("hltParticleFlowRecHitHGCL1Seeded"),
    layerClusters = ("hltHgcalMergeLayerClustersL1Seeded"),
    rCylinder = 2.8,
    recoEcalCandidateProducer = ("hltEgammaCandidatesL1Seeded")
)
