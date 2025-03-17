import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFClusterProducer.PFClusterProducer import PFClusterProducer as _PFClusterProducer

hltParticleFlowClusterHGCal = _PFClusterProducer(
    energyCorrector = dict(

    ),
    initialClusteringStep = dict(
        algoName = 'PFClusterFromHGCalTrackster',
        clusterSrc = ("hltHgcalMergeLayerClusters"),
        filterByTracksterIteration = True,
        filterByTracksterPID = False,
        filter_on_categories = [0, 1],
        filter_on_iterations = [0, 1],
        pid_threshold = 0.8,
        thresholdsByDetector = [],
        tracksterSrc = ("hltTiclTrackstersMerge")
    ),
    pfClusterBuilder = dict(

    ),
    positionReCalc = dict(
        algoName = 'Cluster3DPCACalculator',
        minFractionInCalc = 1e-09,
        updateTiming = False
    ),
    recHitCleaners = [],
    recHitsSource = ("hltParticleFlowRecHitHGC"),
    seedCleaners = [],
    seedFinder = dict(
        algoName = 'PassThruSeedFinder',
        nNeighbours = 8,
        thresholdsByDetector = []
    ),
    usePFThresholdsFromDB = False
)

from Configuration.ProcessModifiers.ticl_v5_cff import ticl_v5
ticl_v5.toModify(hltParticleFlowClusterHGCal.initialClusteringStep, tracksterSrc = "hltTiclCandidate")
