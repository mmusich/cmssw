import FWCore.ParameterSet.Config as cms

from RecoTracker.PixelSeeding.CAHitTripletEDProducer import CAHitTripletEDProducer as _CAHitTripletEDProducer

hltIter2Phase2L3FromL1TkMuonPixelHitTriplets = _CAHitTripletEDProducer(
    CAHardPtCut = 0.3,
    CAPhiCut = 0.1,
    CAThetaCut = 0.015,
    SeedComparitorPSet = dict(
        ComponentName = cms.string('none')
    ),
    doublets = ("hltIter2Phase2L3FromL1TkMuonPixelHitDoublets"),
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
