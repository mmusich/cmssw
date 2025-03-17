import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFClusterProducer.PFClusterProducer import PFClusterProducer as _PFClusterProducer

hltParticleFlowClusterHGCalFromTICLL1Seeded = _PFClusterProducer(
    energyCorrector = dict(

    ),
    initialClusteringStep = dict(
        algoName = 'PFClusterFromHGCalTrackster',
        clusterSrc = ("hltHgcalMergeLayerClustersL1Seeded"),
        filterByTracksterIteration = False,
        filterByTracksterPID = True,
        filter_on_categories = [0, 1],
        filter_on_iterations = [0, 1],
        pid_threshold = 0.8,
        thresholdsByDetector = [],
        tracksterSrc = ("hltTiclTrackstersCLUE3DHighL1Seeded")
    ),
    pfClusterBuilder = dict(

    ),
    positionReCalc = dict(
        algoName = 'Cluster3DPCACalculator',
        minFractionInCalc = 1e-09,
        updateTiming = False
    ),
    recHitCleaners = [],
    recHitsSource = ("hltParticleFlowRecHitHGCL1Seeded"),
    seedCleaners = [],
    seedFinder = dict(
        algoName = 'PassThruSeedFinder',
        nNeighbours = 8,
        thresholdsByDetector = []
    ),
    usePFThresholdsFromDB = False
)
