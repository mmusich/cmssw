import FWCore.ParameterSet.Config as cms

from EventFilter.HcalRawToDigi.HcalRawToDigi import HcalRawToDigi as _HcalRawToDigi

hltHcalDigis = _HcalRawToDigi(
    ComplainEmptyData = cms.untracked.bool(False),
    ElectronicsMap = cms.string(''),
    ExpectedOrbitMessageTime = cms.untracked.int32(-1),
    FEDs = cms.untracked.vint32(),
    FilterDataQuality = True,
    HcalFirstFED = cms.untracked.int32(700),
    InputLabel = ("rawDataCollector"),
    UnpackCalib = cms.untracked.bool(True),
    UnpackTTP = cms.untracked.bool(True),
    UnpackUMNio = cms.untracked.bool(True),
    UnpackZDC = cms.untracked.bool(True),
    UnpackerMode = cms.untracked.int32(0),
    firstSample = 0,
    lastSample = 9,
    mightGet = cms.optional.untracked.vstring,
    saveQIE10DataNSamples = cms.untracked.vint32(),
    saveQIE10DataTags = cms.untracked.vstring(),
    saveQIE11DataNSamples = cms.untracked.vint32(),
    saveQIE11DataTags = cms.untracked.vstring(),
    silent = cms.untracked.bool(True)
)
