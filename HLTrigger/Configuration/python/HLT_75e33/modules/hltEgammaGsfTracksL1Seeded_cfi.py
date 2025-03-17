import FWCore.ParameterSet.Config as cms

from RecoTracker.TrackProducer.GsfTrackProducer import GsfTrackProducer as _GsfTrackProducer

hltEgammaGsfTracksL1Seeded = _GsfTrackProducer(
    AlgorithmName = cms.string('gsf'),
    Fitter = cms.string('GsfElectronFittingSmoother'),
    GeometricInnerState = False,
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = ("hltMeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('fwdGsfElectronPropagator'),
    TTRHBuilder = cms.string('WithTrackAngle'),
    TrajectoryInEvent = False,
    beamSpot = ("hltOnlineBeamSpot"),
    src = ("hltEgammaCkfTrackCandidatesForGSFL1Seeded"),
    useHitsSplitting = False
)
