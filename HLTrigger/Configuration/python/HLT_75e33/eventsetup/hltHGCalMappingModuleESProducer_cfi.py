import FWCore.ParameterSet.Config as cms

hltHGCalMappingModuleESProducer = cms.ESProducer("hgcal::HGCalMappingModuleESProducer@alpaka",
                                                 filename = cms.FileInPath('Geometry/HGCalMapping/data/ModuleMaps/modulelocator_P5v1.txt'),
                                                 moduleindexer = cms.ESInputTag("","")
                                                 )
