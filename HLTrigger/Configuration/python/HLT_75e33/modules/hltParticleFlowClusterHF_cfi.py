import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFClusterProducer.PFClusterProducer import PFClusterProducer as _PFClusterProducer

hltParticleFlowClusterHF = _PFClusterProducer(
    energyCorrector = dict(

    ),
    initialClusteringStep = dict(
        algoName = 'Basic2DGenericTopoClusterizer',
        thresholdsByDetector = [
            dict(
                detector = 'HF_EM',
                gatheringThreshold = 0.8,
                gatheringThresholdPt = 0.0
            ),
            dict(
                detector = 'HF_HAD',
                gatheringThreshold = 0.8,
                gatheringThresholdPt = 0.0
            )
        ],
        useCornerCells = False
    ),
    pfClusterBuilder = dict(
        algoName = 'Basic2DGenericPFlowClusterizer',
        allCellsPositionCalc = dict(
            algoName = 'Basic2DGenericPFlowPositionCalc',
            logWeightDenominator = 0.8,
            minAllowedNormalization = 1e-09,
            minFractionInCalc = 1e-09,
            posCalcNCrystals = -1
        ),
        excludeOtherSeeds = True,
        maxIterations = 50,
        minFracTot = 1e-20,
        minFractionToKeep = 1e-07,
        positionCalc = dict(
            algoName = 'Basic2DGenericPFlowPositionCalc',
            logWeightDenominator = 0.8,
            minAllowedNormalization = 1e-09,
            minFractionInCalc = 1e-09,
            posCalcNCrystals = 5
        ),
        recHitEnergyNorms = [
            dict(
                detector = 'HF_EM',
                recHitEnergyNorm = 0.8
            ),
            dict(
                detector = 'HF_HAD',
                recHitEnergyNorm = 0.8
            )
        ],
        showerSigma = 10.0,
        stoppingTolerance = 1e-08
    ),
    positionReCalc = dict(

    ),
    recHitCleaners = [],
    recHitsSource = ("hltParticleFlowRecHitHF"),
    seedCleaners = [],
    seedFinder = dict(
        algoName = 'LocalMaximumSeedFinder',
        nNeighbours = 0,
        thresholdsByDetector = [
            dict(
                detector = 'HF_EM',
                seedingThreshold = 1.4,
                seedingThresholdPt = 0.0
            ),
            dict(
                detector = 'HF_HAD',
                seedingThreshold = 1.4,
                seedingThresholdPt = 0.0
            )
        ]
    ),
    usePFThresholdsFromDB = False
)
