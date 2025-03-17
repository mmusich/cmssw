import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.L1TEGammaFilteredCollectionProducer import L1TEGammaFilteredCollectionProducer as _L1TEGammaFilteredCollectionProducer

hltL1TEGammaFilteredCollectionProducer = _L1TEGammaFilteredCollectionProducer(
    applyQual = True,
    inputTag = ("l1tGTProducer", "CL2Photons"),
    maxBX = 1,
    minBX = -1,
    minPt = 5.0,
    qualIsMask = True,
    quality = 0b0010,
)
