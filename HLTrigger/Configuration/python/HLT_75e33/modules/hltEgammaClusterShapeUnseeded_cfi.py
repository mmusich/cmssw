import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTClusterShapeProducer import EgammaHLTClusterShapeProducer as _EgammaHLTClusterShapeProducer

hltEgammaClusterShapeUnseeded = _EgammaHLTClusterShapeProducer(
    ecalRechitEB = ("hltEcalRecHit","EcalRecHitsEB"),
    ecalRechitEE = ("hltEcalRecHit","EcalRecHitsEE"),
    recoEcalCandidateProducer = ("hltEgammaCandidatesUnseeded")
)
