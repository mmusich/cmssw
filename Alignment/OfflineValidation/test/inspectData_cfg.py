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
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents0.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents10.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents11.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents12.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents13.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents14.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents15.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents16.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents17.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents18.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents19.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents1.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents20.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents21.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents22.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents23.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents24.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents25.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents26.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents27.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents28.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents29.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents2.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents30.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents3.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents4.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents5.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents6.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents7.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents8.root',
    # 'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/pickevents9.root',    
    'file:/tmp/musich/CMSSW_13_1_X_2023-03-22-2300/src/output.root'
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
