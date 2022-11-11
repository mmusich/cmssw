import glob
import FWCore.ParameterSet.Config as cms
from Alignment.OfflineValidation.TkAlAllInOneTool.defaultInputFiles_cff import filesDefaultData_Comissioning2022_Cosmics_string

###################################################################
# Setup 'standard' options
###################################################################
import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing()
options.register('outFileName',
                 "test.root", # default value
                 VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                 VarParsing.VarParsing.varType.string, # string, int, or float
                 "name of the output file (test.root is default)")

options.register('trackCollection',
                 "generalTracks", #ALCARECOTkAlCosmicsCTF0T
                 VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                 VarParsing.VarParsing.varType.string, # string, int, or float
                 "name of the input track collection")

options.register('globalTag',
                 "auto:run3_data_prompt", # default value
                 VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                 VarParsing.VarParsing.varType.string, # string, int, or float
                 "name of the input Global Tag")

options.register('unitTest',
                 False, # default value
                 VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                 VarParsing.VarParsing.varType.bool, # string, int, or float
                 "is it a unit test?")

options.register('maxEvents',
                 -1,
                 VarParsing.VarParsing.multiplicity.singleton, # singleton or list                 
                 VarParsing.VarParsing.varType.int, # string, int, or float
                 "num. events to run")

options.parseArguments()

process = cms.Process("RECOAnalysis")

###################################################################
# Message logger service
###################################################################
process.load("FWCore.MessageLogger.MessageLogger_cfi")

###################################################################
# Geometry producer and standard includes
###################################################################
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
process.load("Configuration.StandardSequences.Services_cff")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load("CondCore.CondDB.CondDB_cfi")

####################################################################
# Get the GlogalTag
####################################################################
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag,options.globalTag, '')

###################################################################
# Source
###################################################################
readFiles = cms.untracked.vstring([
    '/store/group/phys_exotica/dijet/Dijet13TeV/ilias/event_displays/Anomalous_events_Run3/pickevents_AOD_CHF0p99_normal_pT_event_no1.root',
    '/store/group/phys_exotica/dijet/Dijet13TeV/ilias/event_displays/Anomalous_events_Run3/pickevents_AOD_CHF0p99_normal_pT_event_no2.root',
    '/store/group/phys_exotica/dijet/Dijet13TeV/ilias/event_displays/Anomalous_events_Run3/pickevents_AOD_CHF0p99_normal_pT_event_no3.root'
])
process.source = cms.Source("PoolSource",fileNames = readFiles)
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(options.maxEvents))

###################################################################
# the pT filter
###################################################################
from CommonTools.RecoAlgos.ptMaxTrackCountFilter_cfi import ptMaxTrackCountFilter
process.myfilter = ptMaxTrackCountFilter.clone(src = cms.InputTag(options.trackCollection),
                                               ptMax = cms.double(10.))

process.preAnaSeq = cms.Sequence()
if(options.unitTest):
    print("adding the max pT filter")
    process.preAnaSeq = cms.Sequence(process.myfilter)

###################################################################
# The analysis module
###################################################################
process.myanalysis = cms.EDAnalyzer("GeneralPurposeTrackAnalyzer",
                                    TkTag  = cms.InputTag(options.trackCollection),
                                    isCosmics = cms.bool(False))

###################################################################
# Output name
###################################################################
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string(options.outFileName))

###################################################################
# Path
###################################################################
process.p1 = cms.Path(process.offlineBeamSpot
                      *process.myanalysis)

###################################################################
# preprend the filter
###################################################################
if(options.unitTest):
    process.p1.insert(0, process.preAnaSeq)
