import FWCore.ParameterSet.Config as cms

hltEGL1SeedsForDoublePhotonIsolatedFilter = cms.EDFilter("HLTP2GTFilter",
                                                         saveTags = cms.bool(True),
                                                         l1GTAlgoBlockTag = cms.InputTag('l1tGTAlgoBlockProducer'),
                                                         minN = cms.uint32(2),
                                                         l1GTAlgos = cms.VPSet(
                                                             cms.PSet(
                                                                 name = cms.string('pDoubleEGEle37_24'),
                                                                 objectType = cms.string('CL2Photons'),
                                                                 minPt = cms.double(0),
                                                                 maxAbsEta = cms.double(9999.)
                                                             ),
                                                             cms.PSet(
                                                                 name = cms.string('pDoubleIsoTkPho22_12'),
                                                                 objectType = cms.string('CL2Photons'),
                                                                 minPt = cms.double(0),
                                                                 maxAbsEta = cms.double(9999.)
                                                             ),
                                                         ))
