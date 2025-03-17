import FWCore.ParameterSet.Config as cms

from RecoTauTag.RecoTau.RecoTauPiZeroProducer import RecoTauPiZeroProducer as _RecoTauPiZeroProducer

hltPFTauPiZeros = _RecoTauPiZeroProducer(
    builders = [dict(
        applyElecTrackQcuts = False,
        makeCombinatoricStrips = False,
        maxStripBuildIterations = -1,
        minGammaEtStripAdd = 0.0,
        minGammaEtStripSeed = 0.5,
        minStripEt = 1.0,
        name = 's',
        plugin = 'RecoTauPiZeroStripPlugin2',
        qualityCuts = dict(
            primaryVertexSrc = ("hltPhase2PixelVertices"),
            pvFindingAlgo = 'closestInDeltaZ',
            recoverLeadingTrk = False,
            signalQualityCuts = dict(
                maxDeltaZ = 0.2,
                maxTrackChi2 = 1000.0,
                maxTransverseImpactParameter = 0.2,
                minGammaEt = 0.5,
                minTrackHits = 3,
                minTrackPixelHits = 0,
                minTrackPt = 0.0,
                useTracksInsteadOfPFHadrons = False
            ),
            vertexTrackFiltering = False
        ),
        stripCandidatesParticleIds = [2, 4],
        stripEtaAssociationDistance = 0.05,
        stripPhiAssociationDistance = 0.2,
        updateStripAfterEachDaughter = False
    )],
    jetSrc = ("hltAK4PFJets"),
    massHypothesis = 0.136,
    maxJetAbsEta = 99.0,
    minJetPt = -1.0,
    outputSelection = 'pt > 0',
    ranking = [dict(
        name = 'InStrip',
        plugin = 'RecoTauPiZeroStringQuality',
        selection = "algoIs(\'kStrips\')",
        selectionFailValue = 1000.0,
        selectionPassFunction = 'abs(mass() - 0.13579)'
    )],
    verbosity = 0
)
