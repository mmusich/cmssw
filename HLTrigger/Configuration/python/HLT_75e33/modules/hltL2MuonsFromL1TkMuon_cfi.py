import FWCore.ParameterSet.Config as cms

from RecoMuon.L2MuonProducer.L2MuonProducer import L2MuonProducer as _L2MuonProducer

hltL2MuonsFromL1TkMuon = _L2MuonProducer(
    DoSeedRefit = False,
    InputObjects = ("hltL2MuonSeedsFromL1TkMuon"),
    L2TrajBuilderParameters = dict(
        BWFilterParameters = dict(
            BWSeedType = cms.string('fromGenerator'),
            CSCRecSegmentLabel = ("hltCscSegments"),
            DTRecSegmentLabel = ("hltDt4DSegments"),
            EnableCSCMeasurement = True,
            EnableDTMeasurement = True,
            EnableRPCMeasurement = True,
            FitDirection = cms.string('outsideIn'),
            MaxChi2 = 100.0,
            MuonTrajectoryUpdatorParameters = dict(
                ExcludeRPCFromFit = False,
                Granularity = 0,
                MaxChi2 = 25.0,
                RescaleError = False,
                RescaleErrorFactor = 100.0,
                UseInvalidHits = True
            ),
            NumberOfSigma = 3.0,
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
            RPCRecSegmentLabel = ("hltRpcRecHits")
        ),
        DoBackwardFilter = True,
        DoRefit = False,
        DoSeedRefit = False,
        FilterParameters = dict(
            CSCRecSegmentLabel = ("hltCscSegments"),
            DTRecSegmentLabel = ("hltDt4DSegments"),
            EnableCSCMeasurement = True,
            EnableDTMeasurement = True,
            EnableGEMMeasurement = True,
            EnableME0Measurement = False,
            EnableRPCMeasurement = True,
            FitDirection = cms.string('insideOut'),
            GEMRecSegmentLabel = ("hltGemRecHits"),
            ME0RecSegmentLabel = (""),
            MaxChi2 = 1000.0,
            MuonTrajectoryUpdatorParameters = dict(
                ExcludeRPCFromFit = False,
                Granularity = 0,
                MaxChi2 = 25.0,
                RescaleError = False,
                RescaleErrorFactor = 100.0,
                UseInvalidHits = True
            ),
            NumberOfSigma = 3.0,
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
            RPCRecSegmentLabel = ("hltRpcRecHits")
        ),
        NavigationType = cms.string('Standard'),
        SeedPosition = cms.string('in'),
        SeedPropagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
        SeedTransformerParameters = dict(
            Fitter = cms.string('hltESPKFFittingSmootherForL2Muon'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            NMinRecHits = 2,
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
            RescaleError = 100.0,
            UseSubRecHits = False
        )
    ),
    MuonTrajectoryBuilder = cms.string('Exhaustive'),
    SeedTransformerParameters = dict(
        Fitter = cms.string('hltESPKFFittingSmootherForL2Muon'),
        MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
        NMinRecHits = 2,
        Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
        RescaleError = 100.0,
        UseSubRecHits = False
    ),
    ServiceParameters = dict(
        Propagators = cms.untracked.vstring(
            'hltESPFastSteppingHelixPropagatorAny',
            'hltESPFastSteppingHelixPropagatorOpposite'
        ),
        RPCLayers = True,
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = dict(
        DoSmoothing = False,
        MuonUpdatorAtVertexParameters = dict(
            BeamSpotPosition = [0.0, 0.0, 0.0],
            BeamSpotPositionErrors = [0.1, 0.1, 5.3],
            MaxChi2 = 1000000.0,
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorOpposite')
        ),
        Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        VertexConstraint = True,
        beamSpot = ("hltOnlineBeamSpot")
    )
)
