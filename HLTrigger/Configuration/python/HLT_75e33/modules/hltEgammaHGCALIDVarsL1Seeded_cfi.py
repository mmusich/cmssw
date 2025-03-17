import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTHGCalIDVarProducer import EgammaHLTHGCalIDVarProducer as _EgammaHLTHGCalIDVarProducer

hltEgammaHGCALIDVarsL1Seeded = _EgammaHLTHGCalIDVarProducer(
    hgcalRecHits = cms.InputTag("hltParticleFlowRecHitHGCL1Seeded"),
    layerClusters = cms.InputTag("hltHgcalMergeLayerClustersL1Seeded"),
    rCylinder = cms.double(2.8),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidatesL1Seeded")
)
