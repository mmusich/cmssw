import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTHGCalIDVarProducer import EgammaHLTHGCalIDVarProducer as _EgammaHLTHGCalIDVarProducer

hltEgammaHGCALIDVarsUnseeded = _EgammaHLTHGCalIDVarProducer(
    hgcalRecHits = ("hltParticleFlowRecHitHGC"),
    layerClusters = ("hltHgcalMergeLayerClusters"),
    rCylinder = 2.8,
    recoEcalCandidateProducer = ("hltEgammaCandidatesUnseeded")
)
