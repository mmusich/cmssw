import FWCore.ParameterSet.Config as cms

from RecoTracker.TrackProducer.TrackProducer import TrackProducer as _TrackProducer

hltIter2Phase2L3FromL1TkMuonCtfWithMaterialTracks = _TrackProducer(
    AlgorithmName = cms.string('hltIter2'),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    GeometricInnerState = True,
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = ("hltIter2Phase2L3FromL1TkMuonMaskedMeasurementTrackerEvent"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    TrajectoryInEvent = False,
    beamSpot = ("hltOnlineBeamSpot"),
    clusterRemovalInfo = (""),
    src = ("hltIter2Phase2L3FromL1TkMuonCkfTrackCandidates"),
    useHitsSplitting = False,
    useSimpleMF = False
)
