import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("Demo")

#prepare options

options = VarParsing.VarParsing("analysis")

options.register ('globalTag',
                  "92X_dataRun2_Prompt_v8",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "GlobalTag")

options.register ('scaleFactor',
                  1.,
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.float,          # string, int, or float
                  "scaleFactor")

options.register ('smearFactor',
                  0.,
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.float,          # string, int, or float
                  "smearFactor")


options.register ('runNumber',
                  303014,
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,           # string, int, or float
                  "run number")

options.parseArguments()


##
## MessageLogger
##
process.load('FWCore.MessageService.MessageLogger_cfi')   
process.MessageLogger.categories.append("CreateSiStripChannelGain")  
process.MessageLogger.destinations = cms.untracked.vstring("cout")
process.MessageLogger.cout = cms.untracked.PSet(
    threshold = cms.untracked.string("WARNING"),
    default   = cms.untracked.PSet(limit = cms.untracked.int32(0)),                       
    FwkReport = cms.untracked.PSet(limit = cms.untracked.int32(-1),
                                   reportEvery = cms.untracked.int32(1000)
                                   ),                                                      
    CreateSiStripChannelGain  = cms.untracked.PSet( limit = cms.untracked.int32(-1))
    )
process.MessageLogger.statistics.append('cout') 

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag,options.globalTag, '')

process.source = cms.Source("EmptySource",
                            firstRun = cms.untracked.uint32(options.runNumber),
                            numberEventsInRun = cms.untracked.uint32(1),
                            )


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.demo = cms.EDAnalyzer('CreateSiStripChannelGain',
                              Record = cms.untracked.string("SiStripApvGainRcd"),
                              gainType = cms.untracked.uint32(1), #0 for G1, 1 for G2
                              doScale     = cms.untracked.bool(True),
                              doSmear     = cms.untracked.bool(True), 
                              scaleFactor = cms.untracked.double(options.scaleFactor), # 0. will keep everything the same
                              smearFactor = cms.untracked.double(options.smearFactor)   # 0. will keep everything the same
                              )

##
## Database output service
##
process.load("CondCore.CondDB.CondDB_cfi")

##
## Output database (in this case local sqlite file)
##
process.CondDB.connect = 'sqlite_file:modifiedGains_'+options.globalTag+'_IOV_'+str(options.runNumber)+'_scale_'+str(options.scaleFactor)+'_smear_'+str(options.smearFactor)+'.db'
process.PoolDBOutputService = cms.Service("PoolDBOutputService",
                                          process.CondDB,
                                          timetype = cms.untracked.string('runnumber'),
                                          toPut = cms.VPSet(cms.PSet(record = cms.string('SiStripApvGainRcd'),
                                                                     tag = cms.string('modifiedGains')
                                                                     )
                                                            )
                                          )

process.p = cms.Path(process.demo)
