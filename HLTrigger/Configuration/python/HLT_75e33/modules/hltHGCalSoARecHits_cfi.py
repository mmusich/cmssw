import FWCore.ParameterSet.Config as cms

hltHGCalSoARecHits = cms.EDProducer('HGCalRecHitsProducer@alpaka',
                                    digis = cms.InputTag('hltHgcalDigis', ''),
                                    calibSource = cms.ESInputTag('hltHGCalCalibParamESProducer', ''),
                                    n_hits_scale = cms.int32(1),
                                    n_blocks = cms.int32(1024),
                                    n_threads = cms.int32(1024),
                                    k_noise = cms.double(5.)
                                    )
