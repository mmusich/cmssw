import FWCore.ParameterSet.Config as cms

from RecoTracker.TrackProducer.TrackProducer import TrackProducer as _TrackProducer

hltPhase2L3OIMuCtfWithMaterialTracks = _TrackProducer(
    AlgorithmName = cms.string('iter10'),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    GeometricInnerState = True,
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = ("hltMeasurementTrackerEvent"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    TrajectoryInEvent = False,
    beamSpot = ("hltOnlineBeamSpot"),
    clusterRemovalInfo = (""),
    src = ("hltPhase2L3OITrackCandidates"),
    useHitsSplitting = False,
    useSimpleMF = False
)
