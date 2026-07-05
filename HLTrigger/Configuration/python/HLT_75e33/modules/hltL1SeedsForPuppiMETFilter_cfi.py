import FWCore.ParameterSet.Config as cms

hltL1SeedsForPuppiMETFilter = cms.EDFilter("HLTP2GTFilter",
                                           saveTags = cms.bool(True),
                                           l1GTAlgoBlockTag = cms.InputTag('l1tGTAlgoBlockProducer'),
                                           minN = cms.uint32(1),
                                           l1GTAlgos = cms.VPSet(
                                               cms.PSet(
                                                   name = cms.string('pPuppiMET200'),
                                                   objectType = cms.string('CL2EtSum'),
                                                   minPt = cms.double(0),
                                                   maxAbsEta = cms.double(9999.)
                                               )
                                           ))
