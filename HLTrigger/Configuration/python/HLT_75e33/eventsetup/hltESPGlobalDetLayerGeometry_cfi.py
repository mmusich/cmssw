import FWCore.ParameterSet.Config as cms

from TrackingTools.RecoGeometry.GlobalDetLayerGeometryESProducer import GlobalDetLayerGeometryESProducer as _GlobalDetLayerGeometryESProducer

hltESPGlobalDetLayerGeometry = _GlobalDetLayerGeometryESProducer(
    ComponentName = cms.string('hltESPGlobalDetLayerGeometry')
)
