import FWCore.ParameterSet.Config as cms

def _addProcessTTRHBuilderWithoutRefit(process):
    from RecoTracker.TransientTrackingRecHit.TkTransientTrackingRecHitBuilderESProducer import TkTransientTrackingRecHitBuilderESProducer as _TkTransientTrackingRecHitBuilderESProducer

    hltESPTTRHBuilderWithoutRefit = _TkTransientTrackingRecHitBuilderESProducer(
        ComponentName = cms.string('hltESPTTRHBuilderWithoutRefit'),
        ComputeCoarseLocalPositionFromDisk = False,
        Matcher = cms.string('Fake'),
        Phase2StripCPE = cms.string(''),
        PixelCPE = cms.string('Fake'),
        StripCPE = cms.string('Fake')
    )

from Configuration.ProcessModifiers.trackingLST_cff import trackingLST
modifyConfigurationForTrackingLSTTTRHBuilderWithoutRefit_ = trackingLST.makeProcessModifier(_addProcessTTRHBuilderWithoutRefit)
