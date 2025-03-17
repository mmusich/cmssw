import FWCore.ParameterSet.Config as cms

from RecoLocalCalo.HcalRecProducers.HcalHitReconstructor import HcalHitReconstructor as _HcalHitReconstructor

hltHoreco = _HcalHitReconstructor(
    HFInWindowStat = dict(),
    PETstat = dict(),
    S8S1stat = dict(),
    S9S1stat = dict(),
    Subdetector = cms.string('HO'),
    correctForPhaseContainment = True,
    correctForTimeslew = True,
    correctTiming = False,
    correctionPhaseNS = 13.0,
    dataOOTCorrectionCategory = cms.string('Data'),
    dataOOTCorrectionName = cms.string(''),
    digiLabel = ("hltHcalDigis"),
    digiTimeFromDB = True,
    digistat = dict(),
    dropZSmarkedPassed = True,
    firstAuxTS = 4,
    firstSample = 4,
    hfTimingTrustParameters = dict(),
    mcOOTCorrectionCategory = cms.string('MC'),
    mcOOTCorrectionName = cms.string(''),
    recoParamsFromDB = True,
    samplesToAdd = 4,
    saturationParameters = dict(
        maxADCvalue = 127
    ),
    setNegativeFlags = False,
    setNoiseFlags = False,
    setSaturationFlags = False,
    setTimingTrustFlags = False,
    tsFromDB = True,
    useLeakCorrection = False
)
