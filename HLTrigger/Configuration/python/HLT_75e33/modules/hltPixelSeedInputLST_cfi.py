import FWCore.ParameterSet.Config as cms

from RecoTracker.LST.LSTPixelSeedInputProducer import LSTPixelSeedInputProducer as _LSTPixelSeedInputProducer

hltPixelSeedInputLST = _LSTPixelSeedInputProducer(
    beamSpot = cms.InputTag('hltOnlineBeamSpot'),
    seedTracks = cms.VInputTag(
        'hltInitialStepSeedTracksLST',
        'hltHighPtTripletStepSeedTracksLST'
    )
)

_hltPixelSeedInputLSTSingleIterPatatrack = hltPixelSeedInputLST.clone(
    seedTracks = ['hltInitialStepSeedTracksLST']
)

from Configuration.ProcessModifiers.singleIterPatatrack_cff import singleIterPatatrack
singleIterPatatrack.toReplaceWith(hltPixelSeedInputLST, _hltPixelSeedInputLSTSingleIterPatatrack)
