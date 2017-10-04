import FWCore.ParameterSet.Config as cms

process = cms.Process("SiStripApvGainReader")

process.MessageLogger = cms.Service(
    "MessageLogger",
    debugModules = cms.untracked.vstring(''),
    threshold = cms.untracked.string('INFO'),
    destinations = cms.untracked.vstring('SiStripApvGainReader.log')
    )

##
## Empty events source
## (specify the run number to pick correct IOV) 
##
process.source = cms.Source("EmptySource",
                            numberEventsInRun = cms.untracked.uint32(1),
                            firstRun = cms.untracked.uint32(294000)
                            )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
    )

##
## To Correctly build the SiStripGainRcd in the ES
## we need all the dependent records => specify a Global Tag  
##
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '92X_dataRun2_Prompt_v8', '')

##
## Prefer the SiStripApvGainRcd or SiStripApvGain2Rcd
## under test  
##
process.poolDBESSource = cms.ESSource("PoolDBESSource",
                                      connect = cms.string('sqlite_file:/tmp/musich/CMSSW_9_4_X_2017-10-03-0000/src/SiStripMiscellanea/SiStripChannelGain/test/modified_gains_x2.db'), 
                                      toGet = cms.VPSet(cms.PSet(record = cms.string('SiStripApvGain2Rcd'),
                                                                 tag = cms.string('modifiedGains')
                                                                 )
                                                        )
                                      )

process.prefer_poolDBESSource = cms.ESPrefer("PoolDBESSource","poolDBESSource")

##
## Dump the Gain payload. It will be in the format
## DetId APV1 APV2 APV3 APV4 (APV5) (APV6) 
##
process.gainreader = cms.EDAnalyzer("SiStripApvGainReader",
                                    printDebug = cms.untracked.bool(True),
                                    outputFile = cms.untracked.string("SiStripApvGains_Mods_x2.txt"),
                                    gainType   = cms.untracked.uint32(1)    #0 for G1, 1 for G2
                                    )

process.p1 = cms.Path(process.gainreader)


