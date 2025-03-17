import FWCore.ParameterSet.Config as cms

from RecoTauTag.RecoTau.PFRecoTauDiscriminationByIsolation import PFRecoTauDiscriminationByIsolation as _PFRecoTauDiscriminationByIsolation

hltHpsPFTauMediumRelativeChargedIsolationDiscriminator = _PFRecoTauDiscriminationByIsolation(
    ApplyDiscriminationByECALIsolation = False,
    ApplyDiscriminationByTrackerIsolation = True,
    ApplyDiscriminationByWeightedECALIsolation = False,
    PFTauProducer = ("hltHpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    UseAllPFCandsForWeights = False,
    WeightECALIsolation = 1.0,
    applyDeltaBetaCorrection = False,
    applyFootprintCorrection = False,
    applyOccupancyCut = False,
    applyPhotonPtSumOutsideSignalConeCut = False,
    applyRelativeSumPtCut = True,
    applyRhoCorrection = False,
    applySumPtCut = False,
    customOuterCone = -1.0,
    deltaBetaFactor = '0.38',
    deltaBetaPUTrackPtCutOverride = True,
    deltaBetaPUTrackPtCutOverride_val = 0.5,
    enableHGCalWorkaround = False,
    footprintCorrections = [
        dict(
            offset = '0.0',
            selection = 'decayMode() = 0'
        ),
        dict(
            offset = '0.0',
            selection = 'decayMode() = 1 || decayMode() = 2'
        ),
        dict(
            offset = '2.7',
            selection = 'decayMode() = 5'
        ),
        dict(
            offset = '0.0',
            selection = 'decayMode() = 6'
        ),
        dict(
            offset = 'max(2.0, 0.22*pt() - 2.0)',
            selection = 'decayMode() = 10'
        )
    ],
    isoConeSizeForDeltaBeta = 0.3,
    maxAbsPhotonSumPt_outsideSignalCone = 1000000000.0,
    maxRelPhotonSumPt_outsideSignalCone = 0.1,
    maximumOccupancy = 0,
    maximumSumPtCut = 2.0,
    minTauPtForNoIso = -99.0,
    particleFlowSrc = ("hltParticleFlowTmp"),
    qualityCuts = dict(
        isolationQualityCuts = dict(
            maxDeltaZ = 0.2,
            maxTrackChi2 = 100.0,
            maxTransverseImpactParameter = 0.1,
            minGammaEt = 0.5,
            minTrackHits = 3,
            minTrackPixelHits = 0,
            minTrackPt = 0.5,
            useTracksInsteadOfPFHadrons = False
        ),
        primaryVertexSrc = ("hltPhase2PixelVertices"),
        pvFindingAlgo = 'closestInDeltaZ',
        recoverLeadingTrk = False,
        signalQualityCuts = dict(
            maxDeltaZ = 0.2,
            maxTrackChi2 = 1000.0,
            maxTransverseImpactParameter = 0.2,
            minGammaEt = 0.5,
            minNeutralHadronEt = 1.0,
            minTrackHits = 3,
            minTrackPixelHits = 0,
            minTrackPt = 0.0,
            useTracksInsteadOfPFHadrons = False
        ),
        vertexTrackFiltering = False,
        vxAssocQualityCuts = dict(
            maxTrackChi2 = 1000.0,
            maxTransverseImpactParameter = 0.2,
            minGammaEt = 0.5,
            minTrackHits = 3,
            minTrackPixelHits = 0,
            minTrackPt = 0.0,
            useTracksInsteadOfPFHadrons = False
        )
    ),
    relativeSumPtCut = 0.05,
    relativeSumPtOffset = 60.0,
    rhoConeSize = 0.5,
    rhoProducer = ("hltFixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = 1.0,
    storeRawFootprintCorrection = False,
    storeRawOccupancy = False,
    storeRawPUsumPt = False,
    storeRawPhotonSumPt_outsideSignalCone = False,
    storeRawSumPt = False,
    verbosity = 0,
    vertexSrc = ("NotUsed")
)
