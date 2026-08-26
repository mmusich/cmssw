import FWCore.ParameterSet.Config as cms

hltHGCalMappingTriggerESProducer = cms.ESSource("HGCalMappingTriggerESProducer",
    appendToDataLabel = cms.string(''),
    modules = cms.FileInPath('Geometry/HGCalMapping/data/ModuleMaps/modulelocator_trigger_test.txt'),
    si = cms.FileInPath('Geometry/HGCalMapping/data/CellMaps/WaferCellMapTraces.txt'),
    sipm = cms.FileInPath('Geometry/HGCalMapping/data/CellMaps/channels_sipmontile.hgcal.txt')
)
