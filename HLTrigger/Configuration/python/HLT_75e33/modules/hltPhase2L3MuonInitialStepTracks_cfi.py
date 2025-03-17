import FWCore.ParameterSet.Config as cms

from RecoTracker.TrackProducer.TrackProducer import TrackProducer as _TrackProducer

hltPhase2L3MuonInitialStepTracks = _TrackProducer(
    AlgorithmName = cms.string('initialStep'),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    GeometricInnerState = False,
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = ("hltMeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    TrajectoryInEvent = False,
    beamSpot = ("hltOnlineBeamSpot"),
    clusterRemovalInfo = (""),
    src = ("hltPhase2L3MuonInitialStepTrackCandidates"),
    useHitsSplitting = False,
    useSimpleMF = False
)
