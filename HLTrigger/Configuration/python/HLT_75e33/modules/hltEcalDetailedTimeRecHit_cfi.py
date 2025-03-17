import FWCore.ParameterSet.Config as cms

from RecoLocalCalo.EcalRecProducers.EcalDetailedTimeRecHitProducer import EcalDetailedTimeRecHitProducer as _EcalDetailedTimeRecHitProducer

hltEcalDetailedTimeRecHit = _EcalDetailedTimeRecHitProducer(
    EBDetailedTimeRecHitCollection = cms.string('EcalRecHitsEB'),
    EBRecHitCollection = ("hltEcalRecHit","EcalRecHitsEB"),
    EBTimeDigiCollection = ("mix","EBTimeDigi"),
    EBTimeLayer = 7,
    EEDetailedTimeRecHitCollection = cms.string('EcalRecHitsEE'),
    EERecHitCollection = ("hltEcalRecHit","EcalRecHitsEE"),
    EETimeDigiCollection = ("mix","EETimeDigi"),
    EETimeLayer = 3,
    correctForVertexZPosition = False,
    simVertex = ("g4SimHits"),
    useMCTruthVertex = False
)
