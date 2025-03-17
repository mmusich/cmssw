import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.HLTHGCalDigisInRegionsProducer import HLTHGCalDigisInRegionsProducer as _HLTHGCalDigisInRegionsProducer

hltHgcalDigisL1Seeded = _HLTHGCalDigisInRegionsProducer(
    etaPhiRegions = [dict(
        inputColl = ("hltL1TEGammaHGCFilteredCollectionProducer"),
        maxDEta = 0.0,
        maxDPhi = 0.0,
        maxDeltaR = 0.35,
        maxEt = 999999.0,
        minEt = 5.0,
        type = 'L1P2GTCandidate'
    )],
    inputCollTags = ["hltHgcalDigis:EE", "hltHgcalDigis:HEback", "hltHgcalDigis:HEfront"],
    outputProductNames = ['EE','HEback','HEfront']
)
