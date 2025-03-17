import FWCore.ParameterSet.Config as cms

from RecoTracker.PixelTrackFitting.PixelTrackProducer import PixelTrackProducer as _PixelTrackProducer

hltPhase2PixelTracks = _PixelTrackProducer(
    Cleaner = cms.string('pixelTrackCleanerBySharedHits'),
    Filter = cms.InputTag("hltPhase2PixelTrackFilterByKinematics"),
    Fitter = cms.InputTag("hltPhase2PixelFitterByHelixProjections"),
    SeedingHitSets = cms.InputTag("hltPhase2PixelTracksHitSeeds"),
    mightGet = cms.optional.untracked.vstring,
    passLabel = cms.string('hltPhase2PixelTracks')
)

from Configuration.ProcessModifiers.alpaka_cff import alpaka
_hltPhase2PixelTracks = cms.EDProducer("PixelTrackProducerFromSoAAlpakaPhase2",
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    minNumberOfHits = cms.int32(0),
    minQuality = cms.string('tight'),
    pixelRecHitLegacySrc = cms.InputTag("hltSiPixelRecHits"),
    trackSrc = cms.InputTag("hltPhase2PixelTracksSoA")
)
alpaka.toReplaceWith(hltPhase2PixelTracks, _hltPhase2PixelTracks)
