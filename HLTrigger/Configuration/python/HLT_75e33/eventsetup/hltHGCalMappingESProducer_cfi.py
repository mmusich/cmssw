import FWCore.ParameterSet.Config as cms

hltHGCalMappingESProducer = cms.ESSource("HGCalMappingESProducer",
                                         appendToDataLabel = cms.string(''),
                                         modules = cms.FileInPath('Geometry/HGCalMapping/data/ModuleMaps/modulelocator_P5v1.txt'),
                                         si = cms.FileInPath('Geometry/HGCalMapping/data/CellMaps/WaferCellMapTraces.txt'),
                                         sipm = cms.FileInPath('Geometry/HGCalMapping/data/CellMaps/channels_sipmontile.hgcal.txt')
                                         )
