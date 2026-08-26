import FWCore.ParameterSet.Config as cms

hltHGCalDenseIndexTriggerInfoESProducer = cms.ESProducer("hgcal::HGCalDenseIndexTriggerInfoESProducer@alpaka",
                                                         moduleindexer = cms.ESInputTag("","")
                                                         )
