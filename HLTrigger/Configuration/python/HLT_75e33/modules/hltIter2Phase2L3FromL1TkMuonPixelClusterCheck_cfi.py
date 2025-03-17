import FWCore.ParameterSet.Config as cms

from RecoTracker.TkSeedGenerator.ClusterCheckerEDProducer import ClusterCheckerEDProducer as _ClusterCheckerEDProducer

hltIter2Phase2L3FromL1TkMuonPixelClusterCheck = _ClusterCheckerEDProducer(
    ClusterCollectionLabel = ("hltMeasurementTrackerEvent"),
    MaxNumberOfPixelClusters = 10000,
    MaxNumberOfStripClusters = 50000,
    PixelClusterCollectionLabel = ("hltSiPixelClusters"),
    cut = cms.string(''),
    doClusterCheck = False,
    silentClusterCheck = cms.untracked.bool(False)
)
