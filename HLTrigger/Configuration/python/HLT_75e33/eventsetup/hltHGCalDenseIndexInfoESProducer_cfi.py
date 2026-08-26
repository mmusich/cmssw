import FWCore.ParameterSet.Config as cms

hltHGCalDenseIndexInfoESProducer = cms.ESProducer("hgcal::HGCalDenseIndexInfoESProducer@alpaka",
                                                  moduleindexer = cms.ESInputTag("","")
                                                  )
