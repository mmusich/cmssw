import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.HLTEcalRecHitsInRegionsProducer import HLTEcalRecHitsInRegionsProducer as _HLTEcalRecHitsInRegionsProducer

hltRechitInRegionsECAL = _HLTEcalRecHitsInRegionsProducer(
    etaPhiRegions = [dict(
        inputColl = ("hltL1TEGammaFilteredCollectionProducer"),
        maxDEta = 0.0,
        maxDPhi = 0.0,
        maxDeltaR = 0.35,
        maxEt = 999999.0,
        minEt = 5.0,
        type = 'L1P2GTCandidate'
    )],
    inputCollTags = ["hltEcalRecHitL1Seeded:EcalRecHitsEB", "hltEcalRecHitL1Seeded:EcalRecHitsEE"],
    outputProductNames = ['EcalRecHitsEB', 'EcalRecHitsEE']
)

