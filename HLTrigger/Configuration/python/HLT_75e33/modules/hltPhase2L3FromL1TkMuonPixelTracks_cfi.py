import FWCore.ParameterSet.Config as cms

from RecoTracker.PixelTrackFitting.PixelTrackProducer import PixelTrackProducer as _PixelTrackProducer

hltPhase2L3FromL1TkMuonPixelTracks = _PixelTrackProducer(
    Cleaner = cms.string('hltPixelTracksCleanerBySharedHits'),
    Filter = ("hltPhase2PixelTrackFilterByKinematics"),
    Fitter = ("hltPhase2PixelFitterByHelixProjections"),
    SeedingHitSets = ("hltPhase2L3FromL1TkMuonPixelTracksHitQuadruplets"),
    passLabel = cms.string('')
)
