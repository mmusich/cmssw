import FWCore.ParameterSet.Config as cms

hltSingleTkMuon22L1TkMuonFilter =  cms.EDFilter("HLTP2GTFilter",
                                                saveTags = cms.bool(True),
                                                l1GTAlgoBlockTag = cms.InputTag('l1tGTAlgoBlockProducer'),
                                                minN = cms.uint32(1),
                                                l1GTAlgos = cms.VPSet(
                                                    cms.PSet(
                                                        name = cms.string('pSingleTkMuon22'),
                                                        objectType = cms.string('GMTTkMuons'),
                                                        minPt = cms.double(0),
                                                        maxAbsEta = cms.double(9999.)
                                                    )
                                                ))
