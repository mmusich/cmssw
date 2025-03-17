import FWCore.ParameterSet.Config as cms

from RecoTracker.PixelTrackFitting.PixelTrackCleanerBySharedHitsESProducer import PixelTrackCleanerBySharedHitsESProducer as _PixelTrackCleanerBySharedHitsESProducer

hltPixelTracksCleanerBySharedHits = _PixelTrackCleanerBySharedHitsESProducer(
    ComponentName = cms.string('hltPixelTracksCleanerBySharedHits'),
    appendToDataLabel = cms.string(''),
    useQuadrupletAlgo = cms.bool(False)
)
