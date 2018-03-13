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
process.MessageLogger.categories.append("SiStripNoisesFromDBMiscalibrator")  
process.MessageLogger.destinations = cms.untracked.vstring("cout")
process.MessageLogger.cout = cms.untracked.PSet(
    threshold = cms.untracked.string("INFO"),
    default   = cms.untracked.PSet(limit = cms.untracked.int32(0)),                       
    FwkReport = cms.untracked.PSet(limit = cms.untracked.int32(-1),
                                   reportEvery = cms.untracked.int32(1000)
                                   ),                                                      
    SiStripNoisesFromDBMiscalibrator = cms.untracked.PSet( limit = cms.untracked.int32(-1))
    )
process.MessageLogger.statistics.append('cout') 

process.load("Configuration.Geometry.GeometryRecoDB_cff") # Ideal geometry and interface 
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag,options.globalTag, '')

process.source = cms.Source("EmptySource",
                            firstRun = cms.untracked.uint32(options.runNumber),
                            numberEventsInRun = cms.untracked.uint32(1),
                            )


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

##
## Example smearing configurations
##

##
## separately partition by partition
##
byPartition = cms.VPSet(
    cms.PSet(partition = cms.string("TIB"),
             doScale   = cms.bool(True),
             doSmear   = cms.bool(True),
             scaleFactor = cms.double(1.0),
             smearFactor = cms.double(0.07)
             ),
    cms.PSet(partition = cms.string("TOB"),
             doScale   = cms.bool(True),
             doSmear   = cms.bool(True),
             scaleFactor = cms.double(0.91),
             smearFactor = cms.double(0.06)
             ),
    cms.PSet(partition = cms.string("TID"),
             doScale   = cms.bool(True),
             doSmear   = cms.bool(True),
             scaleFactor = cms.double(1.05),
             smearFactor = cms.double(0.07)
             ),
    cms.PSet(partition = cms.string("TEC"),
             doScale   = cms.bool(True),
             doSmear   = cms.bool(True),
             scaleFactor = cms.double(0.93),
             smearFactor = cms.double(0.06)
             )
    )

##
## whole Strip tracker
##

wholeTracker = cms.VPSet(
    cms.PSet(partition = cms.string("Tracker"),
             doScale   = cms.bool(True),
             doSmear   = cms.bool(True),
             scaleFactor = cms.double(1.00),
             smearFactor = cms.double(0.00)
             )
    )


##
## down the hierarchy (Tracker,Subdetector,Side,Layer(Wheel)
##

subsets =  cms.VPSet(
    cms.PSet(partition = cms.string("Tracker"),
             doScale   = cms.bool(True),
             doSmear   = cms.bool(True),
             scaleFactor = cms.double(0.65),
             smearFactor = cms.double(0.05)
             ),
    cms.PSet(partition = cms.string("TEC"),
             doScale   = cms.bool(True),
             doSmear   = cms.bool(True),
             scaleFactor = cms.double(1.15),
             smearFactor = cms.double(0.02)
             ),
    cms.PSet(partition = cms.string("TECP"),
             doScale   = cms.bool(True),
             doSmear   = cms.bool(True),
             scaleFactor = cms.double(1.35),
             smearFactor = cms.double(0.02)
             ),
    cms.PSet(partition = cms.string("TECP_9"),
             doScale   = cms.bool(True),
             doSmear   = cms.bool(True),
             scaleFactor = cms.double(1.55),
             smearFactor = cms.double(0.02)
             )
    )


# process.demo = cms.EDAnalyzer('SiStripChannelGainFromDBMiscalibrator',
#                               record = cms.untracked.string("SiStripApvGainRcd"),
#                               gainType = cms.untracked.uint32(1), #0 for G1, 1 for G2
#                               params = subsets # as a cms.VPset
#                               )

process.load("CondTools.SiStrip.scaleAndSmearSiStripNoises_cfi")
process.scaleAndSmearSiStripNoises.params   = wholeTracker  # as a cms.VPset

##
## Database output service
##
process.load("CondCore.CondDB.CondDB_cfi")

##
## Output database (in this case local sqlite file)
##
process.CondDB.connect = 'sqlite_file:modifiedNoise_'+options.globalTag+'_IOV_'+str(options.runNumber)+".db"
process.PoolDBOutputService = cms.Service("PoolDBOutputService",
                                          process.CondDB,
                                          timetype = cms.untracked.string('runnumber'),
                                          toPut = cms.VPSet(cms.PSet(record = cms.string('SiStripNoisesRcd'),
                                                                     tag = cms.string('modifiedNoise')
                                                                     )
                                                            )
                                          )

process.p = cms.Path(process.scaleAndSmearSiStripNoises)
