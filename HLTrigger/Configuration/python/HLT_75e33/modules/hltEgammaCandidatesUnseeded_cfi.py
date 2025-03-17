import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTRecoEcalCandidateProducers import EgammaHLTRecoEcalCandidateProducers as _EgammaHLTRecoEcalCandidateProducers

hltEgammaCandidatesUnseeded = _EgammaHLTRecoEcalCandidateProducers(
    recoEcalCandidateCollection = cms.string(''),
    scHybridBarrelProducer = cms.InputTag("hltParticleFlowSuperClusterECALUnseeded","particleFlowSuperClusterECALBarrel"),
    scIslandEndcapProducer = cms.InputTag("hltParticleFlowSuperClusterHGCalFromTICLUnseeded")
)

from Configuration.ProcessModifiers.ticl_v5_cff import ticl_v5
ticl_v5.toModify(hltEgammaCandidatesUnseeded, scIslandEndcapProducer = cms.InputTag("hltTiclEGammaSuperClusterProducerUnseeded"))
