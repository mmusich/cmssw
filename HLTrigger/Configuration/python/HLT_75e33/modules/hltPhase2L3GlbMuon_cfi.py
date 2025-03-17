import FWCore.ParameterSet.Config as cms

from RecoMuon.L3MuonProducer.L3MuonProducer import L3MuonProducer as _L3MuonProducer

hltPhase2L3GlbMuon = _L3MuonProducer(
    L3TrajBuilderParameters = dict(
        GlbRefitterParameters = dict(
            CSCRecSegmentLabel = ("hltCscSegments"),
            Chi2CutCSC = 150.0,
            Chi2CutDT = 10.0,
            Chi2CutRPC = 1.0,
            DTRecSegmentLabel = ("hltDt4DSegments"),
            DYTthrs = [30, 15],
            DoPredictionsOnly = False,
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            HitThreshold = 1,
            MuonHitsOption = 1,
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            PropDirForCosmics = False,
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            RefitDirection = cms.string('insideOut'),
            RefitFlag = True,
            RefitRPCHits = True,
            SkipStation = -1,
            TrackerRecHitBuilder = cms.string('WithTrackAngle'),
            TrackerSkipSection = -1,
            TrackerSkipSystem = -1
        ),
        GlobalMuonTrackMatcher = dict(
            Chi2Cut_1 = 50.0,
            Chi2Cut_2 = 50.0,
            Chi2Cut_3 = 200.0,
            DeltaDCut_1 = 40.0,
            DeltaDCut_2 = 10.0,
            DeltaDCut_3 = 15.0,
            DeltaRCut_1 = 0.1,
            DeltaRCut_2 = 0.2,
            DeltaRCut_3 = 1.0,
            Eta_threshold = 1.2,
            LocChi2Cut = 0.001,
            MinP = 2.5,
            MinPt = 1.0,
            Propagator = cms.string('hltESPSmartPropagator'),
            Pt_threshold1 = 0.0,
            Pt_threshold2 = 999999999.0,
            Quality_1 = 20.0,
            Quality_2 = 15.0,
            Quality_3 = 7.0
        ),
        MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
        MuonTrackingRegionBuilder = dict(
            DeltaEta = 0.2,
            DeltaPhi = 0.15,
            DeltaR = 0.025,
            DeltaZ = 24.2,
            EtaR_UpperLimit_Par1 = 0.25,
            EtaR_UpperLimit_Par2 = 0.15,
            Eta_fixed = True,
            Eta_min = 0.1,
            MeasurementTrackerName = ("hltESPMeasurementTracker"),
            OnDemand = -1,
            PhiR_UpperLimit_Par1 = 0.6,
            PhiR_UpperLimit_Par2 = 0.2,
            Phi_fixed = True,
            Phi_min = 0.1,
            Pt_fixed = False,
            Pt_min = 3.0,
            Rescale_Dz = 4.0,
            Rescale_eta = 3.0,
            Rescale_phi = 3.0,
            UseVertex = False,
            Z_fixed = False,
            beamSpot = ("hltOnlineBeamSpot"),
            input = ("hltL2MuonsFromL1TkMuon","UpdatedAtVtx"),
            maxRegions = 2,
            precise = True
        ),
        PCut = 2.5,
        PtCut = 1.0,
        RefitRPCHits = True,
        ScaleTECxFactor = -1.0,
        ScaleTECyFactor = -1.0,
        TrackTransformer = dict(
            DoPredictionsOnly = False,
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            RefitDirection = cms.string('insideOut'),
            RefitRPCHits = True,
            Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
            TrackerRecHitBuilder = cms.string('WithTrackAngle')
        ),
        TrackerPropagator = cms.string('SteppingHelixPropagatorAny'),
        TrackerRecHitBuilder = cms.string('WithTrackAngle'),
        tkTrajBeamSpot = ("hltOnlineBeamSpot"),
        tkTrajLabel = ("hltPhase2L3MuonMerged"),
        tkTrajMaxChi2 = 9999.0,
        tkTrajMaxDXYBeamSpot = 9999.0,
        tkTrajUseVertex = False,
        tkTrajVertex = ("Notused")
    ),
    MuonCollectionLabel = ("hltL2MuonsFromL1TkMuon","UpdatedAtVtx"),
    ServiceParameters = dict(
        Propagators = cms.untracked.vstring(
            'hltESPSmartPropagatorAny',
            'SteppingHelixPropagatorAny',
            'hltESPSmartPropagator',
            'hltESPSteppingHelixPropagatorOpposite'
        ),
        RPCLayers = True,
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    TrackLoaderParameters = dict(
        DoSmoothing = True,
        MuonSeededTracksInstance = cms.untracked.string('L2Seeded'),
        MuonUpdatorAtVertexParameters = dict(
            BeamSpotPositionErrors = [0.1, 0.1, 5.3],
            MaxChi2 = 1000000.0,
            Propagator = cms.string('hltESPSteppingHelixPropagatorOpposite')
        ),
        PutTkTrackIntoEvent = cms.untracked.bool(False),
        SmoothTkTrack = cms.untracked.bool(False),
        Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        VertexConstraint = False,
        beamSpot = ("hltOnlineBeamSpot")
    )
)
