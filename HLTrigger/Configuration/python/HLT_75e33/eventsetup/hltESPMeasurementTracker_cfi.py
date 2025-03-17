import FWCore.ParameterSet.Config as cms

from RecoTracker.MeasurementDet.MeasurementTrackerESProducer import MeasurementTrackerESProducer as _MeasurementTrackerESProducer

hltESPMeasurementTracker = _MeasurementTrackerESProducer(
    ComponentName = cms.string('hltESPMeasurementTracker'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    MaskBadAPVFibers = True,
    PixelCPE = cms.string('PixelCPEGeneric'),
    SiStripQualityLabel = cms.string(''),
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle'),
    UsePixelModuleQualityDB = True,
    UsePixelROCQualityDB = True,
    UseStripAPVFiberQualityDB = True,
    UseStripModuleQualityDB = True,
    UseStripStripQualityDB = True,
    badStripCuts = dict(
        TEC = dict(
            maxBad = 4,
            maxConsecutiveBad = 2
        ),
        TIB = dict(
            maxBad = 4,
            maxConsecutiveBad = 2
        ),
        TID = dict(
            maxBad = 4,
            maxConsecutiveBad = 2
        ),
        TOB = dict(
            maxBad = 4,
            maxConsecutiveBad = 2
        )
    )
)
