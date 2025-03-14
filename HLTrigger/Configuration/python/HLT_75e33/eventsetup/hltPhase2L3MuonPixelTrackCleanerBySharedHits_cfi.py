import FWCore.ParameterSet.Config as cms

from RecoTracker.PixelTrackFitting.PixelTrackCleanerBySharedHitsESProducer import PixelTrackCleanerBySharedHitsESProducer as _PixelTrackCleanerBySharedHitsESProducer

hltPhase2L3MuonPixelTrackCleanerBySharedHits = _PixelTrackCleanerBySharedHitsESProducer(
    ComponentName = cms.string('hltPhase2L3MuonPixelTrackCleanerBySharedHits'),
    appendToDataLabel = cms.string(''),
    useQuadrupletAlgo = cms.bool(False)
)
