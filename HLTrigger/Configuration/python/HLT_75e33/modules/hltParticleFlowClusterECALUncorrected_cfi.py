import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFClusterProducer.PFClusterProducer import PFClusterProducer as _PFClusterProducer

hltParticleFlowClusterECALUncorrected = _PFClusterProducer(
    energyCorrector = dict(

    ),
    initialClusteringStep = dict(
        algoName = 'Basic2DGenericTopoClusterizer',
        thresholdsByDetector = [
            dict(
                detector = 'ECAL_BARREL',
                gatheringThreshold = 0.175,
                gatheringThresholdPt = 0.0
            ),
            dict(
                detector = 'ECAL_ENDCAP',
                gatheringThreshold = 0.3,
                gatheringThresholdPt = 0.0
            )
        ],
        useCornerCells = True
    ),
    pfClusterBuilder = dict(
        algoName = 'Basic2DGenericPFlowClusterizer',
        allCellsPositionCalc = dict(
            algoName = 'Basic2DGenericPFlowPositionCalc',
            logWeightDenominator = 0.08,
            minAllowedNormalization = 1e-09,
            minFractionInCalc = 1e-09,
            posCalcNCrystals = -1,
            timeResolutionCalcBarrel = dict(
                constantTerm = 0.428192,
                constantTermLowE = 0.0,
                corrTermLowE = 0.0510871,
                noiseTerm = 1.10889,
                noiseTermLowE = 1.31883,
                threshHighE = 5.0,
                threshLowE = 0.5
            ),
            timeResolutionCalcEndcap = dict(
                constantTerm = 0.0,
                constantTermLowE = 0.0,
                corrTermLowE = 0.0,
                noiseTerm = 5.72489999999,
                noiseTermLowE = 6.92683000001,
                threshHighE = 10.0,
                threshLowE = 1.0
            )
        ),
        excludeOtherSeeds = True,
        maxIterations = 50,
        minFracTot = 1e-20,
        minFractionToKeep = 1e-07,
        positionCalc = dict(
            algoName = 'Basic2DGenericPFlowPositionCalc',
            logWeightDenominator = 0.08,
            minAllowedNormalization = 1e-09,
            minFractionInCalc = 1e-09,
            posCalcNCrystals = 9,
            timeResolutionCalcBarrel = dict(
                constantTerm = 0.428192,
                constantTermLowE = 0.0,
                corrTermLowE = 0.0510871,
                noiseTerm = 1.10889,
                noiseTermLowE = 1.31883,
                threshHighE = 5.0,
                threshLowE = 0.5
            ),
            timeResolutionCalcEndcap = dict(
                constantTerm = 0.0,
                constantTermLowE = 0.0,
                corrTermLowE = 0.0,
                noiseTerm = 5.72489999999,
                noiseTermLowE = 6.92683000001,
                threshHighE = 10.0,
                threshLowE = 1.0
            )
        ),
        positionCalcForConvergence = dict(
            T0_EB = 7.4,
            T0_EE = 3.1,
            T0_ES = 1.2,
            W0 = 4.2,
            X0 = 0.89,
            algoName = 'ECAL2DPositionCalcWithDepthCorr',
            minAllowedNormalization = 0.0,
            minFractionInCalc = 0.0
        ),
        recHitEnergyNorms = [
            dict(
                detector = 'ECAL_BARREL',
                recHitEnergyNorm = 0.08
            ),
            dict(
                detector = 'ECAL_ENDCAP',
                recHitEnergyNorm = 0.3
            )
        ],
        showerSigma = 1.5,
        stoppingTolerance = 1e-08
    ),
    positionReCalc = dict(
        T0_EB = 7.4,
        T0_EE = 3.1,
        T0_ES = 1.2,
        W0 = 4.2,
        X0 = 0.89,
        algoName = 'ECAL2DPositionCalcWithDepthCorr',
        minAllowedNormalization = 0.0,
        minFractionInCalc = 0.0
    ),
    recHitCleaners = [],
    recHitsSource = "hltParticleFlowRecHitECALUnseeded",
    seedCleaners = [dict(
        RecHitFlagsToBeExcluded = [],
        algoName = 'FlagsCleanerECAL'
    )],
    seedFinder = dict(
        algoName = 'LocalMaximumSeedFinder',
        nNeighbours = 8,
        thresholdsByDetector = [
            dict(
                detector = 'ECAL_ENDCAP',
                seedingThreshold = 0.6,
                seedingThresholdPt = 0.15
            ),
            dict(
                detector = 'ECAL_BARREL',
                seedingThreshold = 0.4375,
                seedingThresholdPt = 0.0
            )
        ]
    ),
    usePFThresholdsFromDB = False
)
