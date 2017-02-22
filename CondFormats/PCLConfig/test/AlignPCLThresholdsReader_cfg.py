import FWCore.ParameterSet.Config as cms

process = cms.Process("ProcessOne")

process.source = cms.Source("EmptyIOVSource",
                            timetype = cms.string('runnumber'),
                            firstValue = cms.uint64(1),
                            lastValue = cms.uint64(1),
                            interval = cms.uint64(1)
                            )

from CondCore.CondDB.CondDB_cfi import *
CondDBThresholds = CondDB.clone(connect = cms.string("sqlite_file:mythresholds.db"))

process.dbInput = cms.ESSource("PoolDBESSource",
                               CondDBThresholds,
                               toGet = cms.VPSet(cms.PSet(record = cms.string('AlignPCLThresholdsRcd'),
                                                          tag = cms.string('PCLThresholds_express_v0') # choose tag you want
                                                          )
                                                 )
                               )

process.ReadDB = cms.EDAnalyzer("AlignPCLThresholdsReader")

process.p = cms.Path(process.ReadDB)
