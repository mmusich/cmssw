import FWCore.ParameterSet.Config as cms

from RecoTracker.TkTrackingRegions.globalTrackingRegionFromBeamSpot_cfi import globalTrackingRegionFromBeamSpot as _globalTrackingRegionFromBeamSpot

hltPhase2PixelTracksAndHighPtStepTrackingRegions = _globalTrackingRegionFromBeamSpot.clone(
    RegionPSet = dict(
        beamSpot = ("hltOnlineBeamSpot"),
        nSigmaZ = 4.0,
        originRadius = 0.02,
        precise = True,
        ptMin = 0.9
    )
)
