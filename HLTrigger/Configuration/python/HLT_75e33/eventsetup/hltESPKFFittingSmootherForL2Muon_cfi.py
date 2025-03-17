import FWCore.ParameterSet.Config as cms

from TrackingTools.TrackFitters.KFFittingSmootherESProducer import KFFittingSmootherESProducer as _KFFittingSmootherESProducer

hltESPKFFittingSmootherForL2Muon = _KFFittingSmootherESProducer(
    BreakTrajWith2ConsecutiveMissing = False,
    ComponentName = cms.string('hltESPKFFittingSmootherForL2Muon'),
    EstimateCut = -1.0,
    Fitter = cms.string('hltESPKFTrajectoryFitterForL2Muon'),
    LogPixelProbabilityCut = -16.0,
    MaxFractionOutliers = 0.3,
    MaxNumberOfOutliers = 3,
    MinDof = 2,
    MinNumberOfHits = 5,
    NoInvalidHitsBeginEnd = False,
    NoOutliersBeginEnd = False,
    RejectTracks = True,
    Smoother = cms.string('hltESPKFTrajectorySmootherForL2Muon'),
    appendToDataLabel = cms.string('')
)
