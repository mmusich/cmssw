import FWCore.ParameterSet.Config as cms

from RecoTracker.PixelSeeding.CAHitQuadrupletEDProducer import CAHitQuadrupletEDProducer as _CAHitQuadrupletEDProducer

hltPhase2L3FromL1TkMuonPixelTracksHitQuadruplets = _CAHitQuadrupletEDProducer(
    CAHardPtCut = 0.0,
    CAPhiCut = 0.2,
    CAThetaCut = 0.005,
    SeedComparitorPSet = dict(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("hltSiPixelClusterShapeCache"),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = ("hltPhase2L3FromL1TkMuonPixelTracksHitDoublets"),
    extraHitRPhitolerance = 0.032,
    fitFastCircle = True,
    fitFastCircleChi2Cut = True,
    maxChi2 = dict(
        enabled = True,
        pt1 = 0.7,
        pt2 = 2.0,
        value1 = 200.0,
        value2 = 50.0
    ),
    useBendingCorrection = True
)
