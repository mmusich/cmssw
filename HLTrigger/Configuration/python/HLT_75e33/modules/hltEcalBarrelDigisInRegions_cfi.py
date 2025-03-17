import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.HLTEcalEBDigisInRegionsProducer import HLTEcalEBDigisInRegionsProducer as _HLTEcalEBDigisInRegionsProducer

hltEcalBarrelDigisInRegions = _HLTEcalEBDigisInRegionsProducer(
    etaPhiRegions = [dict(
        inputColl = ("hltL1TEGammaFilteredCollectionProducer"),
        maxDEta = 0.0,
        maxDPhi = 0.0,
        maxDeltaR = 0.35,
        maxEt = 999999.0,
        minEt = 5.0,
        type = 'L1P2GTCandidate'
    )],
    inputCollTags = ["hltEcalDigis:ebDigis"],
    outputProductNames = ['ebDigis']
)
