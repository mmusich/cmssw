from __future__ import print_function
import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("Demo")

#prepare options

options = VarParsing.VarParsing("analysis")

options.register ('globalTag',
                  "auto:run2_data",VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "GlobalTag")

options.register ('threshold',
                  3.,VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.float,          # string, int, or float
                  "threshold")

options.parseArguments()


##
## MessageLogger
##
process.load('FWCore.MessageService.MessageLogger_cfi')   
process.MessageLogger.categories.append("SiStripChannelGainMultiIOVFixer")  
process.MessageLogger.destinations = cms.untracked.vstring("cout")
process.MessageLogger.cout = cms.untracked.PSet(
    threshold = cms.untracked.string("WARNING"),
    default   = cms.untracked.PSet(limit = cms.untracked.int32(0)),                       
    FwkReport = cms.untracked.PSet(limit = cms.untracked.int32(-1),
                                   reportEvery = cms.untracked.int32(1000)
                                   ),                                                      
    SiStripChannelGainMultiIOVFixer  = cms.untracked.PSet( limit = cms.untracked.int32(-1))
    )
process.MessageLogger.statistics.append('cout') 

process.load("Configuration.Geometry.GeometryRecoDB_cff") # Ideal geometry and interface 
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag,options.globalTag, '')

print("Using Global Tag:", process.GlobalTag.globaltag._value)

##
## Empty Source
##
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(400000) )      
####################################################################
# Empty source 
####################################################################

process.source = cms.Source("EmptySource",
                            firstRun = cms.untracked.uint32(1),
                            numberEventsInRun = cms.untracked.uint32(1),           # a number of events in single run 
                            )

process.demo = cms.EDAnalyzer('SiStripChannelGainMultiIOVFixer',
                              record = cms.untracked.string("SiStripApvGainRcd"),
                              gainType = cms.untracked.uint32(1), #0 for G1, 1 for G2
                              threshold = cms.untracked.double(options.threshold)
                              )
                        
##
## Database output service
##
process.load("CondCore.CondDB.CondDB_cfi")

##
## Output database (in this case local sqlite file)
##
process.CondDB.connect = 'sqlite_file:modifiedGains_threshold_'+str(options.threshold)+"_"+process.GlobalTag.globaltag._value+".db"
process.PoolDBOutputService = cms.Service("PoolDBOutputService",
                                          process.CondDB,
                                          timetype = cms.untracked.string('runnumber'),
                                          toPut = cms.VPSet(cms.PSet(record = cms.string('SiStripApvGainRcd'),
                                                                     tag = cms.string('cleanGains')
                                                                     )
                                                            )
                                          )

process.p = cms.Path(process.demo)
