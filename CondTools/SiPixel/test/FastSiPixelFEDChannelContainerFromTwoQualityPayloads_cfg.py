import FWCore.ParameterSet.Config as cms
import os

process = cms.Process("summary")

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing()
options.register('outputDB',
                 'sqlite_file:SiPixelStatusScenarios_StuckTBM_2023_v3_mc.db', #default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "output conditions DB")
options.register('outputTag',
                 'SiPixelStatusScenarios_StuckTBM_2023_v3_mc', #default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "output conditions tag")
#options.register('inputTag',
#                 'SiPixelQualityOffline_2017_threshold1percent_stuckTBM', #default value
#                 VarParsing.VarParsing.multiplicity.singleton,
#                 VarParsing.VarParsing.varType.string,
#                 "input conditions tag")
options.register('firstIOV',
                 #1318907147190984, #default value
                 #1592470794141697,
                 #1570437611913217,
                 #1573688902156364, //test
                 #1570437611913217,
                 1607082272882691,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "first IOV")
options.register('lastIOV',
                 #1318907147190984, #default value
                 #1592470794141697,
                 #1573688902156497,
                 #1570901468381185,
                 #1573714671960065,
                 #1594407824392193,
                 1614147494085179,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "last IOV")
options.parseArguments()

##
## MessageLogger
##
process.load('FWCore.MessageService.MessageLogger_cfi')   
process.MessageLogger.cout.enable = True
process.MessageLogger.FastSiPixelFEDChannelContainerFromQuality=dict()  
process.MessageLogger.SiPixelFEDChannelContainer=dict()  
process.MessageLogger.cout = cms.untracked.PSet(
    threshold = cms.untracked.string("INFO"),
    enableStatistics = cms.untracked.bool(True),
    default   = cms.untracked.PSet(limit = cms.untracked.int32(0)),
    FwkReport = cms.untracked.PSet(limit = cms.untracked.int32(-1),
                                   reportEvery = cms.untracked.int32(1000)
                               ),
    FastSiPixelFEDChannelContainerFromQuality = cms.untracked.PSet( limit = cms.untracked.int32(-1)),
    SiPixelFEDChannelContainer           = cms.untracked.PSet( limit = cms.untracked.int32(-1))
)
  
##
## Empty Source
##                                      
process.source = cms.Source(
"EmptySource",
    numberEventsInRun = cms.untracked.uint32(1),
    firstRun = cms.untracked.uint32(1)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

##
## Output database (in this case local sqlite file)
##
process.load("CondCore.CondDB.CondDB_cfi")
process.CondDB.connect = options.outputDB

process.PoolDBOutputService = cms.Service(
    "PoolDBOutputService",
    process.CondDB,
    timetype = cms.untracked.string('runnumber'),
    toPut = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelStatusScenariosRcd'),
            tag = cms.string(options.outputTag)
        )
    )
)
##
## Configuration of the module
##

#print("Processing %s from %s to %s " % (options.inputTag,options.firstIOV,options.lastIOV) )

#process.load("CondTools.SiPixel.FastSiPixelFEDChannelContainerFromTwoQualityPayloads_cfi")
process.load("SiPixelAnalysis/PixelMaskedChannels.FastSiPixelFEDChannelContainerFromTwoQualityPayloads_cfi")
process.FastSiPixelFEDChannelContainerFromTwoQualityPayloads.startIOV = options.firstIOV
process.FastSiPixelFEDChannelContainerFromTwoQualityPayloads.endIOV   = options.lastIOV

process.p = cms.Path(process.FastSiPixelFEDChannelContainerFromTwoQualityPayloads)
