import FWCore.ParameterSet.Config as cms

from RecoTracker.TransientTrackingRecHit.TkTransientTrackingRecHitBuilderESProducer import TkTransientTrackingRecHitBuilderESProducer as _TkTransientTrackingRecHitBuilderESProducer

hltESPTTRHBuilderPixelOnly = _TkTransientTrackingRecHitBuilderESProducer(
    ComponentName = cms.string('hltESPTTRHBuilderPixelOnly'),
    ComputeCoarseLocalPositionFromDisk = False,
    Matcher = cms.string('StandardMatcher'),
    Phase2StripCPE = cms.string(''),
    PixelCPE = cms.string('PixelCPEGeneric'),
    StripCPE = cms.string('Fake')
)
