import FWCore.ParameterSet.Config as cms

from RecoTauTag.RecoTau.PFRecoTauChargedHadronProducer import PFRecoTauChargedHadronProducer as _PFRecoTauChargedHadronProducer

hltHpsTauPFJetsRecoTauChargedHadronsWithNeutrals = _PFRecoTauChargedHadronProducer(
    builders = [
        dict(
            chargedHadronCandidatesParticleIds = [1, 2, 3],
            dRmergeNeutralHadronWrtChargedHadron = 0.005,
            dRmergeNeutralHadronWrtElectron = 0.05,
            dRmergeNeutralHadronWrtNeutralHadron = 0.01,
            dRmergeNeutralHadronWrtOther = 0.005,
            dRmergePhotonWrtChargedHadron = 0.005,
            dRmergePhotonWrtElectron = 0.005,
            dRmergePhotonWrtNeutralHadron = 0.01,
            dRmergePhotonWrtOther = 0.005,
            maxUnmatchedBlockElementsNeutralHadron = 1,
            maxUnmatchedBlockElementsPhoton = 1,
            minBlockElementMatchesNeutralHadron = 2,
            minBlockElementMatchesPhoton = 2,
            minMergeChargedHadronPt = 100.0,
            minMergeGammaEt = 0.0,
            minMergeNeutralHadronEt = 0.0,
            name = 'chargedPFCandidates',
            plugin = 'PFRecoTauChargedHadronFromPFCandidatePlugin',
            qualityCuts = dict(
                primaryVertexSrc = ("hltPhase2PixelVertices"),
                pvFindingAlgo = 'closestInDeltaZ',
                recoverLeadingTrk = False,
                signalQualityCuts = dict(
                    maxDeltaZ = 0.2,
                    maxTrackChi2 = 1000.0,
                    maxTransverseImpactParameter = 0.2,
                    minGammaEt = 0.5,
                    minNeutralHadronEt = 30.0,
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
            )
        ),
        dict(
            chargedHadronCandidatesParticleIds = [5],
            dRmergeNeutralHadronWrtChargedHadron = 0.005,
            dRmergeNeutralHadronWrtElectron = 0.05,
            dRmergeNeutralHadronWrtNeutralHadron = 0.01,
            dRmergeNeutralHadronWrtOther = 0.005,
            dRmergePhotonWrtChargedHadron = 0.005,
            dRmergePhotonWrtElectron = 0.005,
            dRmergePhotonWrtNeutralHadron = 0.01,
            dRmergePhotonWrtOther = 0.005,
            maxUnmatchedBlockElementsNeutralHadron = 1,
            maxUnmatchedBlockElementsPhoton = 1,
            minBlockElementMatchesNeutralHadron = 2,
            minBlockElementMatchesPhoton = 2,
            minMergeChargedHadronPt = 0.0,
            minMergeGammaEt = 0.0,
            minMergeNeutralHadronEt = 0.0,
            name = 'PFNeutralHadrons',
            plugin = 'PFRecoTauChargedHadronFromPFCandidatePlugin',
            qualityCuts = dict(
                primaryVertexSrc = ("hltPhase2PixelVertices"),
                pvFindingAlgo = 'closestInDeltaZ',
                recoverLeadingTrk = False,
                signalQualityCuts = dict(
                    maxDeltaZ = 0.2,
                    maxTrackChi2 = 1000.0,
                    maxTransverseImpactParameter = 0.2,
                    minGammaEt = 0.5,
                    minNeutralHadronEt = 30.0,
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
            )
        )
    ],
    jetSrc = ("hltAK4PFJets"),
    maxJetAbsEta = 99.0,
    minJetPt = -1.0,
    outputSelection = 'pt > 0.5',
    ranking = [
        dict(
            name = 'ChargedPFCandidate',
            plugin = 'PFRecoTauChargedHadronStringQuality',
            selection = "algoIs(\'kChargedPFCandidate\')",
            selectionFailValue = 1000.0,
            selectionPassFunction = '-pt'
        ),
        dict(
            name = 'ChargedPFCandidate',
            plugin = 'PFRecoTauChargedHadronStringQuality',
            selection = "algoIs(\'kPFNeutralHadron\')",
            selectionFailValue = 1000.0,
            selectionPassFunction = '-pt'
        )
    ],
    verbosity = 0
)
