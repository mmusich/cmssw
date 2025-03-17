import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTClusterShapeProducer import EgammaHLTClusterShapeProducer as _EgammaHLTClusterShapeProducer

hltEgammaClusterShapeL1Seeded = _EgammaHLTClusterShapeProducer(
    ecalRechitEB = cms.InputTag("hltRechitInRegionsECAL","EcalRecHitsEB"),
    ecalRechitEE = cms.InputTag("hltRechitInRegionsECAL","EcalRecHitsEE"),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidatesL1Seeded")
)
