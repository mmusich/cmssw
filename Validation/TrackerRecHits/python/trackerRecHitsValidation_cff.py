import FWCore.ParameterSet.Config as cms

from Validation.TrackerRecHits.SiPixelRecHitsValid_cfi import *
from Validation.TrackerRecHits.SiStripRecHitsValid_cfi import *
from DQM.SiStripMonitorSummary.SiStripMonitorCondData_cfi import CondDataMonitoring as _condDataMonitoring

condDataValidation = _condDataMonitoring.clone(
    FillConditions_PSet= _condDataMonitoring.FillConditions_PSet.clone(
        FolderName_For_QualityAndCabling_SummaryHistos=cms.string("SiStrip/SiStripMonitorSummary"),
        HistoMaps_On    = False,
        ActiveDetIds_On = False),
    MonitorSiStripPedestal     = True,
    MonitorSiStripNoise        = True,
    MonitorSiStripQuality      = True,
    MonitorSiStripCabling      = True,
    MonitorSiStripLowThreshold = True,
    MonitorSiStripHighThreshold= True,
    MonitorSiStripApvGain      = True,
    MonitorSiStripLorentzAngle = True,
    OutputMEsInRootFile        = False,
    SiStripPedestalsDQM_PSet= _condDataMonitoring.SiStripPedestalsDQM_PSet.clone(
        ActiveDetIds_On     = True,
        FillSummaryAtLayerLevel = False),
    SiStripNoisesDQM_PSet= _condDataMonitoring.SiStripNoisesDQM_PSet.clone(
        ActiveDetIds_On        = True,
        FillSummaryAtLayerLevel = False),
    SiStripQualityDQM_PSet= _condDataMonitoring.SiStripQualityDQM_PSet.clone(
        ActiveDetIds_On       = True,
        FillSummaryAtLayerLevel = False),
    SiStripCablingDQM_PSet= _condDataMonitoring.SiStripCablingDQM_PSet.clone(
        ActiveDetIds_On       = True),
    SiStripLowThresholdDQM_PSet= _condDataMonitoring.SiStripLowThresholdDQM_PSet.clone(
        ActiveDetIds_On  = True,
        FillSummaryAtLayerLevel = False),
    SiStripHighThresholdDQM_PSet= _condDataMonitoring.SiStripHighThresholdDQM_PSet.clone(
        ActiveDetIds_On = True,
        FillSummaryAtLayerLevel = False),
    SiStripApvGainsDQM_PSet= _condDataMonitoring.SiStripApvGainsDQM_PSet.clone(
        ActiveDetIds_On      = True,
        FillSummaryAtLayerLevel = False),
    SiStripLorentzAngleDQM_PSet= _condDataMonitoring.SiStripLorentzAngleDQM_PSet.clone(ActiveDetIds_On  = False,
                                                                                       FillSummaryAtLayerLevel = False,
                                                                                       CondObj_fillId = cms.string('ProfileAndCumul'))
)

trackerRecHitsValidation = cms.Sequence(pixRecHitsValid+stripRecHitsValid+condDataValidation)
trackerRecHitsStripValidation = cms.Sequence(stripRecHitsValid+condDataValidation)

from Configuration.Eras.Modifier_phase1Pixel_cff import phase1Pixel
phase1Pixel.toReplaceWith( trackerRecHitsValidation, trackerRecHitsStripValidation )
