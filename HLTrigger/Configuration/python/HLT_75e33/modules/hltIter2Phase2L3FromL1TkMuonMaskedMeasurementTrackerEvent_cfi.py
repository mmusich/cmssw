import FWCore.ParameterSet.Config as cms

from RecoTracker.MeasurementDet.MaskedMeasurementTrackerEventProducer import MaskedMeasurementTrackerEventProducer as _MaskedMeasurementTrackerEventProducer

hltIter2Phase2L3FromL1TkMuonMaskedMeasurementTrackerEvent = _MaskedMeasurementTrackerEventProducer(
    phase2clustersToSkip = ("hltIter2Phase2L3FromL1TkMuonClustersRefRemoval"),
    src = ("hltMeasurementTrackerEvent")
)
