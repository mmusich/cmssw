import FWCore.ParameterSet.Config as cms

from RecoVertex.BeamSpotProducer.BeamSpotOnlineProducer import BeamSpotOnlineProducer as _BeamSpotOnlineProducer

hltOnlineBeamSpot = _BeamSpotOnlineProducer(
    changeToCMSCoordinates = False,
    gtEvmLabel = (""),
    maxRadius = 2.0,
    maxZ = 40.0,
    setSigmaZ = 0.0,
    useBSOnlineRecords = True,
    timeThreshold = 48,
    sigmaZThreshold =  2.0 ,
    sigmaXYThreshold =  4.0 
)
