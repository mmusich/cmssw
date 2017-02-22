import FWCore.ParameterSet.Config as cms

process = cms.Process("ProcessOne")

process.source = cms.Source("EmptyIOVSource",
    timetype = cms.string('runnumber'),
                            firstValue = cms.uint64(1),
                            lastValue = cms.uint64(1),
                            interval = cms.uint64(1)
                            )
#Database output service

process.load("CondCore.CondDB.CondDB_cfi")
# output database (in this case local sqlite file)
process.CondDB.connect = 'sqlite_file:mythresholds.db'


process.PoolDBOutputService = cms.Service("PoolDBOutputService",
                                          process.CondDB,
                                          timetype = cms.untracked.string('runnumber'),
                                          toPut = cms.VPSet(cms.PSet(record = cms.string('AlignPCLThresholdsRcd'),
                                                                     tag = cms.string('PCLThresholds_express_v0')
                                                                     )
                                                            )
                                          )

process.WriteInDB = cms.EDAnalyzer("AlignPCLThresholdsWriter",
                                   record= cms.string('AlignPCLThresholdsRcd'),
                                   AlignableIDVec = cms.vuint32(1,2)
                                   )

process.p = cms.Path(process.WriteInDB)
