import FWCore.ParameterSet.Config as cms

from RecoTracker.PixelSeeding.CAHitQuadrupletEDProducer import CAHitQuadrupletEDProducer as _CAHitQuadrupletEDProducer

hltPhase2PixelTracksHitSeeds = _CAHitQuadrupletEDProducer(
    CAHardPtCut = 0.0,
    CAPhiCut = 0.2,
    CAThetaCut = 0.0012,
    SeedComparitorPSet = dict(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("hltSiPixelClusterShapeCache"),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = ("hltPhase2PixelTracksHitDoublets"),
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
    mightGet = cms.optional.untracked.vstring,
    useBendingCorrection = True
)
