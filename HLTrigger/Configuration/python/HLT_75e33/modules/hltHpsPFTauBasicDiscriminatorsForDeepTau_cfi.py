import FWCore.ParameterSet.Config as cms

from RecoTauTag.RecoTau.PFRecoTauDiscriminationByIsolationContainer import PFRecoTauDiscriminationByIsolationContainer as _PFRecoTauDiscriminationByIsolationContainer

hltHpsPFTauBasicDiscriminatorsForDeepTau = _PFRecoTauDiscriminationByIsolationContainer(
    IDWPdefinitions = [],
    IDdefinitions = [
        dict(
            ApplyDiscriminationByTrackerIsolation = True,
            IDname = 'ChargedIsoPtSum',
            storeRawSumPt = True
        ),
        dict(
            ApplyDiscriminationByECALIsolation = True,
            IDname = 'NeutralIsoPtSum',
            storeRawSumPt = True
        ),
        dict(
            ApplyDiscriminationByWeightedECALIsolation = True,
            IDname = 'NeutralIsoPtSumWeight',
            UseAllPFCandsForWeights = True,
            storeRawSumPt = True
        ),
        dict(
            IDname = 'TauFootprintCorrection',
            storeRawFootprintCorrection = True
        ),
        dict(
            IDname = 'PhotonPtSumOutsideSignalCone',
            storeRawPhotonSumPt_outsideSignalCone = True
        ),
        dict(
            IDname = 'PUcorrPtSum',
            applyDeltaBetaCorrection = True,
            storeRawPUsumPt = True
        )
    ],
    PFTauProducer = ("hltHpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    WeightECALIsolation = 1.0,
    applyFootprintCorrection = False,
    applyRhoCorrection = False,
    customOuterCone = 0.5,
    deltaBetaFactor = '0.2000',
    deltaBetaPUTrackPtCutOverride = True,
    deltaBetaPUTrackPtCutOverride_val = 0.5,
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
    isoConeSizeForDeltaBeta = 0.8,
    minTauPtForNoIso = -99.0,
    particleFlowSrc = ("hltParticleFlowTmp"),
    qualityCuts = dict(
        isolationQualityCuts = dict(
            maxDeltaZ = 0.2,
            maxDeltaZToLeadTrack = -1.0,
            maxTrackChi2 = 100.0,
            maxTransverseImpactParameter = 0.03,
            minGammaEt = 1.5,
            minTrackHits = 8,
            minTrackPixelHits = 0,
            minTrackPt = 1.0,
            minTrackVertexWeight = -1.0,
            useTracksInsteadOfPFHadrons = False
        ),
        leadingTrkOrPFCandOption = 'leadPFCand',
        primaryVertexSrc = ("hltPhase2PixelVertices"),
        pvFindingAlgo = 'closestInDeltaZ',
        recoverLeadingTrk = False,
        signalQualityCuts = dict(
            maxDeltaZ = 0.4,
            maxDeltaZToLeadTrack = -1.0,
            maxTrackChi2 = 100.0,
            maxTransverseImpactParameter = 0.1,
            minGammaEt = 1.0,
            minNeutralHadronEt = 30.0,
            minTrackHits = 3,
            minTrackPixelHits = 0,
            minTrackPt = 0.5,
            minTrackVertexWeight = -1.0,
            useTracksInsteadOfPFHadrons = False
        ),
        vertexTrackFiltering = False,
        vxAssocQualityCuts = dict(
            maxTrackChi2 = 100.0,
            maxTransverseImpactParameter = 0.1,
            minGammaEt = 1.0,
            minTrackHits = 3,
            minTrackPixelHits = 0,
            minTrackPt = 0.5,
            minTrackVertexWeight = -1.0
        )
    ),
    rhoConeSize = 0.5,
    rhoProducer = ("hltFixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = 1.0,
    verbosity = 0,
    vertexSrc = ("hltPhase2PixelVertices")
)
