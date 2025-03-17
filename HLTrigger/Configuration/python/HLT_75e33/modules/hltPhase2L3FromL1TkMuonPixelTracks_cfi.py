import FWCore.ParameterSet.Config as cms

from RecoTracker.PixelTrackFitting.PixelTrackProducer import PixelTrackProducer as _PixelTrackProducer

hltPhase2L3FromL1TkMuonPixelTracks = _PixelTrackProducer(
    Cleaner = cms.string('hltPixelTracksCleanerBySharedHits'),
    Filter = cms.InputTag("hltPhase2PixelTrackFilterByKinematics"),
    Fitter = cms.InputTag("hltPhase2PixelFitterByHelixProjections"),
    SeedingHitSets = cms.InputTag("hltPhase2L3FromL1TkMuonPixelTracksHitQuadruplets"),
    passLabel = cms.string('')
)
