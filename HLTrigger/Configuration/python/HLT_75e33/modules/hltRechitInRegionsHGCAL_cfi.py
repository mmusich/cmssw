import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.HLTHGCalRecHitsInRegionsProducer import HLTHGCalRecHitsInRegionsProducer as _HLTHGCalRecHitsInRegionsProducer

hltRechitInRegionsHGCAL = _HLTHGCalRecHitsInRegionsProducer(
    etaPhiRegions = [dict(
        inputColl = ("hltL1TEGammaHGCFilteredCollectionProducer"),
        maxDEta = 0.0,
        maxDPhi = 0.0,
        maxDeltaR = 0.35,
        maxEt = 999999.0,
        minEt = 5.0,
        type = 'L1P2GTCandidate',
    )],
    inputCollTags = ["hltHGCalRecHitL1Seeded:HGCEERecHits", "hltHGCalRecHitL1Seeded:HGCHEBRecHits", "hltHGCalRecHitL1Seeded:HGCHEFRecHits"],
    outputProductNames = ['HGCEERecHits', 'HGCHEBRecHits', 'HGCHEFRecHits']
)
