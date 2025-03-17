import FWCore.ParameterSet.Config as cms

from CommonTools.PileupAlgos.PuppiProducer import PuppiProducer as _PuppiProducer

hltPFPuppi = _PuppiProducer(
    DeltaZCut = 0.1,
    DeltaZCutForChargedFromPUVtxs = 0.2,
    EtaMaxCharged = 99999.0,
    EtaMaxPhotons = 2.5,
    EtaMinUseDeltaZ = -1.0,
    MinPuppiWeight = 0.01,
    NumOfPUVtxsForCharged = 0,
    PUProxyValue = ("hltPixelClustersMultiplicity"),
    PtMaxCharged = -1.0,
    PtMaxNeutrals = 200.0,
    PtMaxNeutralsStartSlope = 0.0,
    PtMaxPhotons = -1.0,
    UseDeltaZCut = True,
    UseFromPVLooseTight = False,
    algos = [
        dict(
            EtaMaxExtrap = 2.0,
            MedEtaSF = [1.0, 1.0],
            MinNeutralPt = [0.5105, 0.821],
            MinNeutralPtSlope = [9.51e-06, 1.902e-05],
            RMSEtaSF = [1.0, 1.0],
            etaMax = [2.5, 3.5],
            etaMin = [0.0, 2.5],
            ptMin = [0.0, 0.0],
            puppiAlgos = [dict(
                algoId = 5,
                applyLowPUCorr = True,
                combOpt = 0,
                cone = 0.4,
                rmsPtMin = 0.1,
                rmsScaleFactor = 1.0,
                useCharged = True
            )]
        ),
        dict(
            EtaMaxExtrap = 2.0,
            MedEtaSF = [0.75],
            MinNeutralPt = [3.656],
            MinNeutralPtSlope = [5.072e-05],
            RMSEtaSF = [1.0],
            etaMax = [10.0],
            etaMin = [3.5],
            ptMin = [0.0],
            puppiAlgos = [dict(
                algoId = 5,
                applyLowPUCorr = True,
                combOpt = 0,
                cone = 0.4,
                rmsPtMin = 0.5,
                rmsScaleFactor = 1.0,
                useCharged = False
            )]
        )
    ],
    applyCHS = True,
    candName = ("hltParticleFlowTmp"),
    clonePackedCands = False,
    invertPuppi = False,
    puppiDiagnostics = False,
    puppiNoLep = False,
    useExistingWeights = False,
    useExp = False,
    usePUProxyValue = True,
    vertexName = ("hltGoodOfflinePrimaryVertices"),
    vtxNdofCut = 4,
    vtxZCut = 24
)
