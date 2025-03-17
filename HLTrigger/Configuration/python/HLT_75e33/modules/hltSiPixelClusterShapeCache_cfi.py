import FWCore.ParameterSet.Config as cms

from RecoTracker.PixelLowPtUtilities.SiPixelClusterShapeCacheProducer import SiPixelClusterShapeCacheProducer as _SiPixelClusterShapeCacheProducer

hltSiPixelClusterShapeCache = _SiPixelClusterShapeCacheProducer(
    mightGet = cms.optional.untracked.vstring,
    onDemand = False,
    src = ("hltSiPixelClusters")
)
