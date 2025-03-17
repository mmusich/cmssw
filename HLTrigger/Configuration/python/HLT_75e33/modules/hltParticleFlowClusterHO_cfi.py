import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFClusterProducer.PFClusterProducer import PFClusterProducer as _PFClusterProducer

hltParticleFlowClusterHO = _PFClusterProducer(
    energyCorrector = dict(

    ),
    initialClusteringStep = dict(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = [
            dict(
                detector = cms.string('HCAL_BARREL2_RING0'),
                gatheringThreshold = 0.05,
                gatheringThresholdPt = 0.0
            ),
            dict(
                detector = cms.string('HCAL_BARREL2_RING1'),
                gatheringThreshold = 0.05,
                gatheringThresholdPt = 0.0
            )
        ],
        useCornerCells = True
    ),
    pfClusterBuilder = dict(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = dict(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = 0.05,
            minAllowedNormalization = 1e-09,
            minFractionInCalc = 1e-09,
            posCalcNCrystals = -1
        ),
        excludeOtherSeeds = True,
        maxIterations = 50,
        minFracTot = 1e-20,
        minFractionToKeep = 1e-07,
        positionCalc = dict(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = 0.05,
            minAllowedNormalization = 1e-09,
            minFractionInCalc = 1e-09,
            posCalcNCrystals = 5
        ),
        recHitEnergyNorms = [
            dict(
                detector = cms.string('HCAL_BARREL2_RING0'),
                recHitEnergyNorm = 0.05
            ),
            dict(
                detector = cms.string('HCAL_BARREL2_RING1'),
                recHitEnergyNorm = 0.05
            )
        ],
        showerSigma = 10.0,
        stoppingTolerance = 1e-08
    ),
    positionReCalc = dict(

    ),
    recHitCleaners = [],
    recHitsSource = ("hltParticleFlowRecHitHO"),
    seedCleaners = [],
    seedFinder = dict(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = 4,
        thresholdsByDetector = [
            dict(
                detector = cms.string('HCAL_BARREL2_RING0'),
                seedingThreshold = 0.08,
                seedingThresholdPt = 0.0
            ),
            dict(
                detector = cms.string('HCAL_BARREL2_RING1'),
                seedingThreshold = 0.08,
                seedingThresholdPt = 0.0
            )
        ]
    ),
    usePFThresholdsFromDB = False
)
