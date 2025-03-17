import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTHGCalIDVarProducer import EgammaHLTHGCalIDVarProducer as _EgammaHLTHGCalIDVarProducer

hltEgammaHGCALIDVarsUnseeded = _EgammaHLTHGCalIDVarProducer(
    hgcalRecHits = cms.InputTag("hltParticleFlowRecHitHGC"),
    layerClusters = cms.InputTag("hltHgcalMergeLayerClusters"),
    rCylinder = cms.double(2.8),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidatesUnseeded")
)
