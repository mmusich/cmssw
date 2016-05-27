import FWCore.ParameterSet.Config as cms

createIdealTkAlRecords = cms.EDAnalyzer("CreateIdealTkAlRecords",
                                        alignToGlobalTag  =  cms.untracked.bool(True),
                                        createReferenceRcd =  cms.untracked.bool(False)
                                        )
