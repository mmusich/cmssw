import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTClusterShapeProducer import EgammaHLTClusterShapeProducer as _EgammaHLTClusterShapeProducer

hltEgammaClusterShapeUnseeded = _EgammaHLTClusterShapeProducer(
    ecalRechitEB = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
    ecalRechitEE = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidatesUnseeded")
)
