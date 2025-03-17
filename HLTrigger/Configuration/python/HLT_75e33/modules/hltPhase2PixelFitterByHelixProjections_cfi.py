import FWCore.ParameterSet.Config as cms

from RecoTracker.PixelTrackFitting.PixelFitterByHelixProjectionsProducer import PixelFitterByHelixProjectionsProducer as _PixelFitterByHelixProjectionsProducer

hltPhase2PixelFitterByHelixProjections = _PixelFitterByHelixProjectionsProducer(
    scaleErrorsForBPix1 = False,
    scaleFactor = 0.65
)
