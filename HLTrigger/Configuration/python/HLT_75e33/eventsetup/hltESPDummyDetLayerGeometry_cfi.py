import FWCore.ParameterSet.Config as cms

from TrackingTools.RecoGeometry.DetLayerGeometryESProducer import DetLayerGeometryESProducer as _DetLayerGeometryESProducer

hltESPDummyDetLayerGeometry = _DetLayerGeometryESProducer(
    ComponentName = cms.string('hltESPDummyDetLayerGeometry')
)
