import FWCore.ParameterSet.Config as cms

hltHGCalMappingModuleTriggerESProducer = cms.ESProducer("hgcal::HGCalMappingTriggerModuleESProducer@alpaka",
                                                        filename = cms.FileInPath('Geometry/HGCalMapping/data/ModuleMaps/modulelocator_trigger_test.txt'),
                                                        moduleindexer = cms.ESInputTag("","")
                                                        )
