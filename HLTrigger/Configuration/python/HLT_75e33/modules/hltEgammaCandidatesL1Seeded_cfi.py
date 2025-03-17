import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTRecoEcalCandidateProducers import EgammaHLTRecoEcalCandidateProducers as _EgammaHLTRecoEcalCandidateProducers

hltEgammaCandidatesL1Seeded = _EgammaHLTRecoEcalCandidateProducers(
    recoEcalCandidateCollection = cms.string(''),
    scHybridBarrelProducer = ("hltParticleFlowSuperClusterECALL1Seeded","particleFlowSuperClusterECALBarrel"),
    scIslandEndcapProducer = ("hltParticleFlowSuperClusterHGCalFromTICLL1Seeded")
)

from Configuration.ProcessModifiers.ticl_v5_cff import ticl_v5
ticl_v5.toModify(hltEgammaCandidatesL1Seeded, scIslandEndcapProducer = ("hltTiclEGammaSuperClusterProducerL1Seeded"))
