import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTClusterShapeProducer import EgammaHLTClusterShapeProducer as _EgammaHLTClusterShapeProducer

hltEgammaClusterShapeL1Seeded = _EgammaHLTClusterShapeProducer(
    ecalRechitEB = ("hltRechitInRegionsECAL","EcalRecHitsEB"),
    ecalRechitEE = ("hltRechitInRegionsECAL","EcalRecHitsEE"),
    recoEcalCandidateProducer = ("hltEgammaCandidatesL1Seeded")
)
