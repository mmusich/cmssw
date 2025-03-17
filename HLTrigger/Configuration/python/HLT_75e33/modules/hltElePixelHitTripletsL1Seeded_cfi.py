import FWCore.ParameterSet.Config as cms

from RecoTracker.PixelSeeding.CAHitTripletEDProducer import CAHitTripletEDProducer as _CAHitTripletEDProducer

hltElePixelHitTripletsL1Seeded = _CAHitTripletEDProducer(
    CAHardPtCut = 0.3,
    CAPhiCut = 0.1,
    CAThetaCut = 0.004,
    SeedComparitorPSet = dict(
        ComponentName = cms.string('none')
    ),
    doublets = ("hltElePixelHitDoubletsForTripletsL1Seeded"),
    extraHitRPhitolerance = 0.032,
    maxChi2 = dict(
        enabled = True,
        pt1 = 0.8,
        pt2 = 8.0,
        value1 = 100.0,
        value2 = 6.0
    ),
    useBendingCorrection = True
)
