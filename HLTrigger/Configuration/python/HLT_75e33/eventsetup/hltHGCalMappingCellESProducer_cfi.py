import FWCore.ParameterSet.Config as cms

hltHGCalMappingCellESProducer = cms.ESProducer("hgcal::HGCalMappingCellESProducer@alpaka",
                                               cellindexer = cms.ESInputTag("",""),
                                               filelist = cms.vstring(
                                                   'Geometry/HGCalMapping/data/CellMaps/WaferCellMapTraces.txt',
                                                   'Geometry/HGCalMapping/data/CellMaps/channels_sipmontile.hgcal.txt'
                                               ),
                                               offsetfile = cms.FileInPath('Geometry/HGCalMapping/data/CellMaps/calibration_to_surrounding_offsetMap.txt')
                                               )
