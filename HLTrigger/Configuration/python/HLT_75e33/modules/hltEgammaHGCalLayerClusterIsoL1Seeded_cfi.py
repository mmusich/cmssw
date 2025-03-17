import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTHGCalLayerClusterIsolationProducer import EgammaHLTHGCalLayerClusterIsolationProducer as _EgammaHLTHGCalLayerClusterIsolationProducer

hltEgammaHGCalLayerClusterIsoL1Seeded = _EgammaHLTHGCalLayerClusterIsolationProducer(
    doRhoCorrection = cms.bool(False),
    drMax = cms.double(0.2),
    drVetoEM = cms.double(0.02),
    drVetoHad = cms.double(0.0),
    layerClusterProducer = cms.InputTag("hltHgcalMergeLayerClustersL1Seeded"),
    minEnergyEM = cms.double(0.02),
    minEnergyHad = cms.double(0.07),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidatesL1Seeded"),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    useEt = cms.bool(False)
)
