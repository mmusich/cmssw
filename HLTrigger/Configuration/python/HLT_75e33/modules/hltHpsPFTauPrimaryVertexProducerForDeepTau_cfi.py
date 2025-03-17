import FWCore.ParameterSet.Config as cms

from RecoTauTag.RecoTau.PFTauPrimaryVertexProducer import PFTauPrimaryVertexProducer as _PFTauPrimaryVertexProducer

hltHpsPFTauPrimaryVertexProducerForDeepTau = _PFTauPrimaryVertexProducer(
    Algorithm = 0,
    ElectronTag = ("hltEgammaCandidates"),
    MuonTag = ("hltMuons"),
    PFTauTag = ("hltHpsPFTauProducer"),
    PVTag = ("hltPhase2PixelVertices"),
    RemoveElectronTracks = False,
    RemoveMuonTracks = False,
    beamSpot = ("hltOnlineBeamSpot"),
    cut = 'pt > 18.0 & abs(eta)<2.4',
    discriminators = cms.VPSet(cms.PSet(
        discriminator = cms.InputTag("hltHpsPFTauDiscriminationByDecayModeFindingNewDMs"),
        selectionCut = cms.double(0.5)
    )),
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
            minTrackVertexWeight = -1.0
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
            minTrackVertexWeight = -1.0
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
    useBeamSpot = True,
    useSelectedTaus = False
)
