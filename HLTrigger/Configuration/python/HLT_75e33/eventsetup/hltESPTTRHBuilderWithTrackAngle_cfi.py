import FWCore.ParameterSet.Config as cms

from RecoTracker.TransientTrackingRecHit.TkTransientTrackingRecHitBuilderESProducer import TkTransientTrackingRecHitBuilderESProducer as _TkTransientTrackingRecHitBuilderESProducer

hltESPTTRHBuilderWithTrackAngle = _TkTransientTrackingRecHitBuilderESProducer(
    ComponentName = cms.string('hltESPTTRHBuilderWithTrackAngle'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    Phase2StripCPE = cms.string('Phase2StripCPE'),
    PixelCPE = cms.string('PixelCPEGeneric'),
    StripCPE = cms.string('FakeStripCPE')
)
