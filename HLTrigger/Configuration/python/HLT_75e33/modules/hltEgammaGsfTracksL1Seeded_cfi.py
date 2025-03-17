import FWCore.ParameterSet.Config as cms

from RecoTracker.TrackProducer.GsfTrackProducer import GsfTrackProducer as _GsfTrackProducer

hltEgammaGsfTracksL1Seeded = _GsfTrackProducer(
    AlgorithmName = cms.string('gsf'),
    Fitter = cms.string('GsfElectronFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("hltMeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('fwdGsfElectronPropagator'),
    TTRHBuilder = cms.string('WithTrackAngle'),
    TrajectoryInEvent = cms.bool(False),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    src = cms.InputTag("hltEgammaCkfTrackCandidatesForGSFL1Seeded"),
    useHitsSplitting = cms.bool(False)
)
