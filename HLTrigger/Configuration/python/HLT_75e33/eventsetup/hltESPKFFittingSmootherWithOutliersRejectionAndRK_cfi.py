import FWCore.ParameterSet.Config as cms

from TrackingTools.TrackFitters.KFFittingSmootherESProducer import KFFittingSmootherESProducer as _KFFittingSmootherESProducer

hltESPKFFittingSmootherWithOutliersRejectionAndRK = _KFFittingSmootherESProducer(
    BreakTrajWith2ConsecutiveMissing = True,
    ComponentName = cms.string('hltESPKFFittingSmootherWithOutliersRejectionAndRK'),
    EstimateCut = 20.0,
    Fitter = cms.string('hltESPRKTrajectoryFitter'),
    LogPixelProbabilityCut = -14.0,
    MaxFractionOutliers = 0.3,
    MaxNumberOfOutliers = 3,
    MinDof = 2,
    MinNumberOfHits = 3,
    NoInvalidHitsBeginEnd = True,
    NoOutliersBeginEnd = False,
    RejectTracks = True,
    Smoother = cms.string('hltESPRKTrajectorySmoother'),
    appendToDataLabel = cms.string('')
)
