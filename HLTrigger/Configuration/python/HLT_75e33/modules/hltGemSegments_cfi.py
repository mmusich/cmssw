import FWCore.ParameterSet.Config as cms

from RecoLocalMuon.GEMSegment.GEMSegmentProducer import GEMSegmentProducer as _GEMSegmentProducer

hltGemSegments = _GEMSegmentProducer(
    algo_name = cms.string('GEMSegmentAlgorithm'),
    algo_pset = dict(
        GEMDebug = cms.untracked.bool(True),
        clusterOnlySameBXRecHits = True,
        dEtaChainBoxMax = 0.05,
        dPhiChainBoxMax = 0.02,
        dXclusBoxMax = 1.0,
        dYclusBoxMax = 5.0,
        maxRecHitsInCluster = 4,
        minHitsPerSegment = 2,
        preClustering = True,
        preClusteringUseChaining = True
    ),
    ge0_name = cms.string('GE0SegAlgoRU'),
    ge0_pset = dict(
        allowWideSegments = True,
        doCollisions = True,
        maxChi2Additional = 100.0,
        maxChi2GoodSeg = 50,
        maxChi2Prune = 50,
        maxETASeeds = 0.1,
        maxNumberOfHits = 300,
        maxNumberOfHitsPerLayer = 100,
        maxPhiAdditional = 0.001096605744,
        maxPhiSeeds = 0.001096605744,
        maxTOFDiff = 25,
        minNumberOfHits = 4,
        requireCentralBX = True
    ),
    gemRecHitLabel = ("hltGemRecHits")
)
