import FWCore.ParameterSet.Config as cms

from RecoTracker.MeasurementDet.MeasurementTrackerEventProducer import MeasurementTrackerEventProducer as _MeasurementTrackerEventProducer

hltMeasurementTrackerEvent = _MeasurementTrackerEventProducer(
    Phase2TrackerCluster1DProducer = cms.string('hltSiPhase2Clusters'),
    badPixelFEDChannelCollectionLabels = cms.VInputTag(),
    inactivePixelDetectorLabels = cms.VInputTag(),
    inactiveStripDetectorLabels = cms.VInputTag("siStripDigis"),
    measurementTracker = cms.string(''),
    mightGet = cms.optional.untracked.vstring,
    pixelCablingMapLabel = cms.string(''),
    pixelClusterProducer = cms.string('hltSiPixelClusters'),
    skipClusters = cms.InputTag(""),
    stripClusterProducer = cms.string(''),
    switchOffPixelsIfEmpty = cms.bool(True)
)
