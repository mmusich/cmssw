import FWCore.ParameterSet.Config as cms

from RecoTracker.PixelTrackFitting.PixelTrackFilterByKinematicsProducer import PixelTrackFilterByKinematicsProducer as _PixelTrackFilterByKinematicsProducer

hltPhase2PixelTrackFilterByKinematics = _PixelTrackFilterByKinematicsProducer(
    chi2 = 1000.0,
    nSigmaInvPtTolerance = 0.0,
    nSigmaTipMaxTolerance = 0.0,
    ptMin = 0.9,
    tipMax = 1.0
)
