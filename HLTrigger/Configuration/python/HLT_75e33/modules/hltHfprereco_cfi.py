import FWCore.ParameterSet.Config as cms

from RecoLocalCalo.HcalRecProducers.HFPreReconstructor import HFPreReconstructor as _HFPreReconstructor

hltHfprereco = _HFPreReconstructor(
    digiLabel = ("hltHcalDigis"),
    dropZSmarkedPassed = True,
    forceSOI = -1,
    soiShift = 0,
    sumAllTimeSlices = False,
    tsFromDB = False
)
