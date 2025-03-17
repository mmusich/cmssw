import FWCore.ParameterSet.Config as cms

from EventFilter.CSCRawToDigi.CSCDCCUnpacker import CSCDCCUnpacker as _CSCDCCUnpacker

hltMuonCSCDigis = _CSCDCCUnpacker(
    Debug = cms.untracked.bool(False),
    ErrorMask = 0,
    ExaminerMask = 535558134,
    FormatedEventDump = cms.untracked.bool(False),
    InputObjects = ("rawDataCollector"),
    PrintEventNumber = cms.untracked.bool(False),
    SuppressZeroLCT = cms.untracked.bool(True),
    UnpackStatusDigis = False,
    UseExaminer = True,
    UseFormatStatus = True,
    UseSelectiveUnpacking = True,
    VisualFEDInspect = cms.untracked.bool(False),
    VisualFEDShort = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring,
    runDQM = cms.untracked.bool(False)
)
