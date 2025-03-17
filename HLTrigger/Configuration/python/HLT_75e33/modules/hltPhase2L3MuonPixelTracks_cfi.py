import FWCore.ParameterSet.Config as cms

from RecoTracker.PixelTrackFitting.PixelTrackProducer import PixelTrackProducer as _PixelTrackProducer

hltPhase2L3MuonPixelTracks = _PixelTrackProducer(
    Cleaner = cms.string('hltPhase2L3MuonPixelTrackCleanerBySharedHits'),
    Filter = cms.InputTag("hltPhase2PixelTrackFilterByKinematics"),
    Fitter = cms.InputTag("hltPhase2PixelFitterByHelixProjections"),
    SeedingHitSets = cms.InputTag("hltPhase2L3MuonPixelTracksHitQuadruplets"),
    mightGet = cms.optional.untracked.vstring,
    passLabel = cms.string('hltPhase2L3MuonPixelTracks')
)
