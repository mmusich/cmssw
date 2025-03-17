import FWCore.ParameterSet.Config as cms

from RecoTracker.PixelSeeding.CAHitTripletEDProducer import CAHitTripletEDProducer as _CAHitTripletEDProducer

hltPhase2L3MuonHighPtTripletStepHitTriplets = _CAHitTripletEDProducer(
    CAHardPtCut = 0.5,
    CAPhiCut = 0.06,
    CAThetaCut = 0.003,
    SeedComparitorPSet = dict(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("hltSiPixelClusterShapeCache"),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = ("hltPhase2L3MuonHighPtTripletStepHitDoublets"),
    extraHitRPhitolerance = 0.032,
    maxChi2 = dict(
        enabled = True,
        pt1 = 0.8,
        pt2 = 8,
        value1 = 100,
        value2 = 6
    ),
    useBendingCorrection = True
)
