#! /usr/bin/env cmsRun
# Author: Marco Musich (Feb 2022)
import FWCore.ParameterSet.Config as cms
process = cms.Process("TEST")

###################################################################
# Messages
###################################################################
process.load('FWCore.MessageService.MessageLogger_cfi')   
process.MessageLogger.cerr.enable = False
process.MessageLogger.SiPhase2BadStripChannelReader=dict()  
process.MessageLogger.SiStripBadStrip=dict()
process.MessageLogger.cout = cms.untracked.PSet(
    enable    = cms.untracked.bool(True),
    enableStatistics = cms.untracked.bool(True),
    threshold = cms.untracked.string("INFO"),
    default   = cms.untracked.PSet(limit = cms.untracked.int32(0)),                       
    FwkReport = cms.untracked.PSet(limit = cms.untracked.int32(-1),
                                   reportEvery = cms.untracked.int32(1000)
                                   ),                                                      
  SiPhase2BadStripChannelReader = cms.untracked.PSet( limit = cms.untracked.int32(-1)),
  SiStripBadStrip = cms.untracked.PSet( limit = cms.untracked.int32(-1)),
)

###################################################################
# A data source must always be defined.
# We don't need it, so here's a dummy one.
###################################################################
process.source = cms.Source("EmptyIOVSource",
    timetype = cms.string('runnumber'),
    firstValue = cms.uint64(1),
    lastValue = cms.uint64(1),
    interval = cms.uint64(1)
)

###################################################################
# Input data
###################################################################
tag = 'SiStripBadStripPhase2_T15'
suffix = 'v0'
inFile = tag+'_'+suffix+'.db'
inDB = 'sqlite_file:'+inFile

process.load("CondCore.CondDB.CondDB_cfi")
# input database (in this case the local sqlite file)
process.CondDB.connect = inDB

process.PoolDBESSource = cms.ESSource("PoolDBESSource",
                                      process.CondDB,
                                      DumpStat=cms.untracked.bool(True),
                                      toGet = cms.VPSet(cms.PSet(record = cms.string("SiStripBadStripRcd"),
                                                                 tag = cms.string(tag))
                                                       )
                                      )

###################################################################
# check the ES data getter
###################################################################
process.get = cms.EDAnalyzer("EventSetupRecordDataGetter",
    toGet = cms.VPSet(cms.PSet(
        record = cms.string(' SiStripBadStripRcd'),
        data = cms.vstring('SiStripBadStrip')
    )),
    verbose = cms.untracked.bool(True)
)

###################################################################
# Payload reader
###################################################################
import CondTools.SiPhase2Tracker.siPhase2BadStripChannelReader_cfi as _mod
process.BadStripPayloadReader = _mod.siPhase2BadStripChannelReader.clone(printDebug = 10,
                                                                   label = "")

###################################################################
# Path
###################################################################
process.p = cms.Path(process.BadStripPayloadReader)

