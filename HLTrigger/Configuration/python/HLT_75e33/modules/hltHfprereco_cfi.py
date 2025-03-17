import FWCore.ParameterSet.Config as cms

from RecoLocalCalo.HcalRecProducers.HFPreReconstructor import HFPreReconstructor as _HFPreReconstructor

hltHfprereco = _HFPreReconstructor(
    digiLabel = cms.InputTag("hltHcalDigis"),
    dropZSmarkedPassed = cms.bool(True),
    forceSOI = cms.int32(-1),
    soiShift = cms.int32(0),
    sumAllTimeSlices = cms.bool(False),
    tsFromDB = cms.bool(False)
)
