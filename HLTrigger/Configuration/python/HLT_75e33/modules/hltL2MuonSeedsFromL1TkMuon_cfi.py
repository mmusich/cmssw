import FWCore.ParameterSet.Config as cms

from RecoMuon.L2MuonSeedGenerator.L2MuonSeedGeneratorFromL1TkMu import L2MuonSeedGeneratorFromL1TkMu as _L2MuonSeedGeneratorFromL1TkMu

hltL2MuonSeedsFromL1TkMuon = _L2MuonSeedGeneratorFromL1TkMu(
    EtaMatchingBins = [0.0, 2.5],
    InputObjects = ("l1tTkMuonsGmt"),
    L1MaxEta = 2.5,
    L1MinPt = 0.0,
    MatchDR = [0.3],
    MinPL1Tk = 3.5,
    MinPtL1TkBarrel = 3.5,
    OfflineSeedLabel = ("hltL2OfflineMuonSeeds"),
    Propagator = 'SteppingHelixPropagatorAny',
    ServiceParameters = dict(
        Propagators = ['SteppingHelixPropagatorAny'],
        RPCLayers = True,
        UseMuonNavigation = True
    ),
    SetMinPtBarrelTo = 3.5,
    SetMinPtEndcapTo = 1.0,
    UseOfflineSeed = True,
    UseUnassociatedL1 = False
)

from RecoMuon.L2MuonSeedGenerator.Phase2L2MuonSeedCreator import Phase2L2MuonSeedCreator as _Phase2L2MuonSeedCreator
phase2HltL2MuonSeedsFromL1TkMuon = _Phase2L2MuonSeedCreator(
    inputObjects = ('l1tTkMuonsGmt'),
    cscRecSegmentLabel = ('hltCscSegments'),
    dtRecSegmentLabel = ('hltDt4DSegments'),
    minPL1Tk = 3.5,
    maxPL1Tk = 200,
    stubMatchDPhi = 0.05,
    stubMatchDTheta = 0.1,
    extrapolationWindowClose = 0.2,
    extrapolationWindowFar = 0.1,
    maximumEtaBarrel = 0.7,
    maximumEtaOverlap = 1.3,
    propagator = 'SteppingHelixPropagatorAny',
    serviceParameters = dict(
        Propagators = ['SteppingHelixPropagatorAny'],
        RPCLayers = True,
        UseMuonNavigation = True
    ),
    estimatorMaxChi2 = 1000.0
)   

from Configuration.ProcessModifiers.phase2L2AndL3Muons_cff import phase2L2AndL3Muons
phase2L2AndL3Muons.toReplaceWith(
    hltL2MuonSeedsFromL1TkMuon,
    phase2HltL2MuonSeedsFromL1TkMuon
    )
