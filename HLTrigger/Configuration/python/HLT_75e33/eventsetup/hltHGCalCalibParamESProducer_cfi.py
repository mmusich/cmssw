import FWCore.ParameterSet.Config as cms

hltHGCalCalibParamESProducer = cms.ESProducer('hgcalrechit::HGCalCalibrationESProducer@alpaka',
                                              filename = cms.FileInPath('RecoLocalCalo/HGCalRecProducers/data/testbeam/level0_calib_params_test.json'),
                                              filenameEnergyLoss = cms.FileInPath('RecoLocalCalo/HGCalRecProducers/data/testbeam/hgcal_energyloss_v16.json'),
                                              indexSource = cms.ESInputTag('hltHGCalMappingESProducer', ''),
                                              mapSource = cms.ESInputTag('hltHGCalMappingModuleESProducer', '')
                                              )
