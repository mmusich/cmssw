import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTRecoEcalCandidateProducers import EgammaHLTRecoEcalCandidateProducers as _EgammaHLTRecoEcalCandidateProducers

hltEgammaCandidatesUnseeded = _EgammaHLTRecoEcalCandidateProducers(
    recoEcalCandidateCollection = cms.string(''),
    scHybridBarrelProducer = ("hltParticleFlowSuperClusterECALUnseeded","particleFlowSuperClusterECALBarrel"),
    scIslandEndcapProducer = ("hltParticleFlowSuperClusterHGCalFromTICLUnseeded")
)

from Configuration.ProcessModifiers.ticl_v5_cff import ticl_v5
ticl_v5.toModify(hltEgammaCandidatesUnseeded, scIslandEndcapProducer = ("hltTiclEGammaSuperClusterProducerUnseeded"))
