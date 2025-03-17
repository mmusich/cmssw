import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFClusterProducer.PFClusterProducer import PFClusterProducer as _PFClusterProducer

hltParticleFlowClusterHBHE = _PFClusterProducer(
    energyCorrector = dict(

    ),
    initialClusteringStep = dict(
        algoName = 'Basic2DGenericTopoClusterizer',
        thresholdsByDetector = [
            dict(
                depths = cms.vint32(1, 2, 3, 4),
                detector = 'HCAL_BARREL1',
                gatheringThreshold = cms.vdouble(0.1, 0.2, 0.3, 0.3),
                gatheringThresholdPt = cms.vdouble(0.0, 0.0, 0.0, 0.0)
            ),
            dict(
                depths = cms.vint32(
                    1, 2, 3, 4, 5,
                    6, 7
                ),
                detector = 'HCAL_ENDCAP',
                gatheringThreshold = cms.vdouble(
                    0.1, 0.2, 0.2, 0.2, 0.2,
                    0.2, 0.2
                ),
                gatheringThresholdPt = cms.vdouble(
                    0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 0.0
                )
            )
        ],
        useCornerCells = True
    ),
    pfClusterBuilder = dict(
        algoName = 'Basic2DGenericPFlowClusterizer',
        allCellsPositionCalc = dict(
            algoName = 'Basic2DGenericPFlowPositionCalc',
            logWeightDenominatorByDetector = [
                dict(
                    depths = cms.vint32(1, 2, 3, 4),
                    detector = 'HCAL_BARREL1',
                    logWeightDenominator = cms.vdouble(0.1, 0.2, 0.3, 0.3)
                ),
                dict(
                    depths = cms.vint32(
                        1, 2, 3, 4, 5,
                        6, 7
                    ),
                    detector = 'HCAL_ENDCAP',
                    logWeightDenominator = cms.vdouble(
                        0.1, 0.2, 0.2, 0.2, 0.2,
                        0.2, 0.2
                    )
                )
            ],
            minAllowedNormalization = 1e-09,
            minFractionInCalc = 1e-09,
            posCalcNCrystals = -1
        ),
        clusterTimeResFromSeed = False,
        excludeOtherSeeds = True,
        maxIterations = 5,
        maxNSigmaTime = 10.0,
        minChi2Prob = 0.0,
        minFracTot = 1e-20,
        minFractionToKeep = 1e-07,
        positionCalc = dict(
            algoName = 'Basic2DGenericPFlowPositionCalc',
            logWeightDenominatorByDetector = [
                dict(
                    depths = cms.vint32(1, 2, 3, 4),
                    detector = 'HCAL_BARREL1',
                    logWeightDenominator = cms.vdouble(0.1, 0.2, 0.3, 0.3)
                ),
                dict(
                    depths = cms.vint32(
                        1, 2, 3, 4, 5,
                        6, 7
                    ),
                    detector = 'HCAL_ENDCAP',
                    logWeightDenominator = cms.vdouble(
                        0.1, 0.2, 0.2, 0.2, 0.2,
                        0.2, 0.2
                    )
                )
            ],
            minAllowedNormalization = 1e-09,
            minFractionInCalc = 1e-09,
            posCalcNCrystals = 5
        ),
        recHitEnergyNorms = [
            dict(
                depths = cms.vint32(1, 2, 3, 4),
                detector = 'HCAL_BARREL1',
                recHitEnergyNorm = cms.vdouble(0.1, 0.2, 0.3, 0.3)
            ),
            dict(
                depths = cms.vint32(
                    1, 2, 3, 4, 5,
                    6, 7
                ),
                detector = 'HCAL_ENDCAP',
                recHitEnergyNorm = cms.vdouble(
                    0.1, 0.2, 0.2, 0.2, 0.2,
                    0.2, 0.2
                )
            )
        ],
        showerSigma = 10.0,
        stoppingTolerance = 1e-08,
        timeResolutionCalcBarrel = dict(
            constantTerm = 2.82,
            constantTermLowE = 4.24,
            corrTermLowE = 0.0,
            noiseTerm = 21.86,
            noiseTermLowE = 8,
            threshHighE = 15.0,
            threshLowE = 6.0
        ),
        timeResolutionCalcEndcap = dict(
            constantTerm = 2.82,
            constantTermLowE = 4.24,
            corrTermLowE = 0.0,
            noiseTerm = 21.86,
            noiseTermLowE = 8,
            threshHighE = 15.0,
            threshLowE = 6.0
        ),
        timeSigmaEB = 10.0,
        timeSigmaEE = 10.0
    ),
    positionReCalc = dict(

    ),
    recHitCleaners = [],
    recHitsSource = ("hltParticleFlowRecHitHBHE"),
    seedCleaners = [],
    seedFinder = dict(
        algoName = 'LocalMaximumSeedFinder',
        nNeighbours = 4,
        thresholdsByDetector = [
            dict(
                depths = cms.vint32(1, 2, 3, 4),
                detector = 'HCAL_BARREL1',
                seedingThreshold = cms.vdouble(0.125, 0.25, 0.35, 0.35),
                seedingThresholdPt = cms.vdouble(0.0, 0.0, 0.0, 0.0)
            ),
            dict(
                depths = cms.vint32(
                    1, 2, 3, 4, 5,
                    6, 7
                ),
                detector = 'HCAL_ENDCAP',
                seedingThreshold = cms.vdouble(
                    0.1375, 0.275, 0.275, 0.275, 0.275,
                    0.275, 0.275
                ),
                seedingThresholdPt = cms.vdouble(
                    0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 0.0
                )
            )
        ]
    ),
    usePFThresholdsFromDB = True
)
