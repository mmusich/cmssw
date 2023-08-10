from __future__ import print_function
import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
import copy 

process = cms.Process("Demo")

#prepare options

options = VarParsing.VarParsing("analysis")

options.register ('globalTag',
                  "auto:run2_data_promptlike_hi",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,         # string, int, or float
                  "GlobalTag")

options.register ('runNumber',
                  326479,
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,            # string, int, or float
                  "run number")

options.parseArguments()


##
## MessageLogger
##
process.load('FWCore.MessageService.MessageLogger_cfi')   
process.MessageLogger.cerr.enable = False
process.MessageLogger.SiStripNoisesBoundaryChecker=dict()  
process.MessageLogger.cout = cms.untracked.PSet(
    enable    = cms.untracked.bool(True),
    enableStatistics = cms.untracked.bool(True),
    threshold = cms.untracked.string("INFO"),
    default   = cms.untracked.PSet(limit = cms.untracked.int32(0)),                       
    FwkReport = cms.untracked.PSet(limit = cms.untracked.int32(-1),
                                   reportEvery = cms.untracked.int32(1000)
                                   ),                                                      
    SiStripNoisesBoundaryChecker = cms.untracked.PSet( limit = cms.untracked.int32(-1))
    )

##
## Conditions
##
process.load("Configuration.Geometry.GeometryRecoDB_cff") # Ideal geometry and interface 
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag,options.globalTag, '')

print("Using Global Tag:", process.GlobalTag.globaltag._value)

##
## Empty Source
##
process.source = cms.Source("EmptySource",
                            firstRun = cms.untracked.uint32(options.runNumber),
                            numberEventsInRun = cms.untracked.uint32(1),
                            )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

##
## Analyzer
##
process.demo = cms.EDAnalyzer('SiStripNoisesBoundaryChecker',
                              printDebug = cms.untracked.uint32(100),
                              stripToTest = cms.untracked.int32(-1),
                              file = cms.untracked.FileInPath('CalibTracker/SiStripCommon/data/SiStripDetInfo.dat'))

##
## Parh
##
process.p = cms.Path(process.demo)
