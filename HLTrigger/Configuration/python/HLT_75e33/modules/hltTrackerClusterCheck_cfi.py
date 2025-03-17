import FWCore.ParameterSet.Config as cms

from RecoTracker.TkSeedGenerator.ClusterCheckerEDProducer import ClusterCheckerEDProducer as _ClusterCheckerEDProducer

hltTrackerClusterCheck = _ClusterCheckerEDProducer(
    ClusterCollectionLabel = ("siStripClusters"),
    MaxNumberOfPixelClusters = 40000,
    MaxNumberOfStripClusters = 400000,
    PixelClusterCollectionLabel = ("hltSiPixelClusters"),
    cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
    doClusterCheck = False,
    mightGet = cms.optional.untracked.vstring,
    silentClusterCheck = cms.untracked.bool(False)
)
