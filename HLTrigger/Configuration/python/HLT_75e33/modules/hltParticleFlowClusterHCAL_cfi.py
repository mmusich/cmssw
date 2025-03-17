import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFClusterProducer.PFMultiDepthClusterProducer import PFMultiDepthClusterProducer as _PFMultiDepthClusterProducer

hltParticleFlowClusterHCAL = _PFMultiDepthClusterProducer(
    clustersSource = ("hltParticleFlowClusterHBHE"),
    energyCorrector = dict(

    ),
    pfClusterBuilder = dict(
        algoName = 'PFMultiDepthClusterizer',
        allCellsPositionCalc = dict(
            algoName = 'Basic2DGenericPFlowPositionCalc',
            logWeightDenominatorByDetector = [
                dict(
                    depths = [1, 2, 3, 4],
                    detector = 'HCAL_BARREL1',
                    logWeightDenominator = [0.1, 0.2, 0.3, 0.3]
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
        minFractionToKeep = 1e-07,
        nSigmaEta = 2.0,
        nSigmaPhi = 2.0
    ),
    positionReCalc = dict(

    ),
    usePFThresholdsFromDB = True
)
