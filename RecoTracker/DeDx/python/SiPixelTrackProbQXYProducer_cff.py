import FWCore.ParameterSet.Config as cms

SiPixelTrackProbQXY = cms.EDProducer("SiPixelTrackProbQXYProducer",
    tracks                     = cms.InputTag("generalTracks"),
)

 
doSiPixelTrackProbQXYTask = cms.Task(SiPixelTrackProbQXY)
doSiPixelTrackProbQXY = cms.Sequence(doSiPixelTrackProbQXYTask)
