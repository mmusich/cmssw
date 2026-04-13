from builtins import range
import os, sys
import FWCore.ParameterSet.Config as cms

# Parameters for runType
import FWCore.ParameterSet.VarParsing as VarParsing
from .dqmPythonTypes import *

'''
check that the input directory exists and there are files in it
'''
def checkInputFolder(streamer_folder):
    if not (os.path.exists(streamer_folder) and os.path.isdir(os.path.join(streamer_folder))):
        raise IOError("Input folder '%s' does not exist in CMSSW_SEARCH_PATH" % streamer_folder)

    items = os.listdir(dqm_streamer_folder)
    if not items:
        raise IOError("Input folder '%s' does not contain any file" % streamer_folder)


options = VarParsing.VarParsing('analysis')

options.register('runNumber',
                 111,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Run number.")

options.register('datafnPosition',
                 3, # default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Data filename position in the positional arguments array 'data' in json file.")

options.register('runInputDir',
                 '/tmp',
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "Directory where the DQM files will appear.")

options.register('scanOnce',
                 True, # default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.bool,
                 "Don't repeat file scans: use what was found during the initial scan. EOR file is ignored and the state is set to 'past end of run'.")

options.register('skipFirstLumis',
                 False, # default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.bool,
                 "Skip (and ignore the minEventsPerLumi parameter) for the files which have been available at the beginning of the processing.")

options.register('BeamSplashRun',
                 False, # default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.bool,
                 "Set client source settings for beam SPLASH run")

# Parameters for runType

options.register('runkey',
                 'pp_run',
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "Run Keys of CMS")

# Parameter for frontierKey

options.register('runUniqueKey',
                 'InValid',
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "Unique run key from RCMS for Frontier")

# Parameter for output directory of the event display clients
# visualization-live and visualization-live-secondInstance
# this additional input argument was added in the hltd framework
# only for the visualization clients 
# Note, the other clients do not use this input parameter

options.register('outputBaseDir',
                 '/fff/BU0/output',
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "Directory where the visualization output files will appear.")

# This is used only by the online clients themselves. 
# We need to register it here because otherwise an error occurs saying that there is an unidentified option.
options.register('unitTest',
                 True,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.bool,
                 "Required to avoid the error.")

options.parseArguments()

# Read streamer files from https://github.com/cms-data/DQM-Integration
dqm_integration_data = [os.path.join(dir,'DQM/Integration/data') for dir in os.getenv('CMSSW_SEARCH_PATH','').split(":") if os.path.exists(os.path.join(dir,'DQM/Integration/data'))][0]
dqm_streamer_folder = os.path.join(dqm_integration_data,'run'+str(options.runNumber))
print("Reading streamer files from:\n ",dqm_streamer_folder)
checkInputFolder(dqm_streamer_folder)

# Fix to allow scram to compile
#if len(sys.argv) > 1:
#  options.parseArguments()

runType = RunType()
if not options.runkey.strip():
  options.runkey = 'pp_run'

runType.setRunType(options.runkey.strip())

# Input source
nextLumiTimeoutMillis = 120000
endOfRunKills = True

if options.scanOnce:
    endOfRunKills = False
    nextLumiTimeoutMillis = 0

source = cms.Source("DQMProtobufReader",
    runNumber = cms.untracked.uint32(options.runNumber),
    runInputDir = cms.untracked.string(dqm_integration_data),
    streamLabel = cms.untracked.string('streamDQMHistograms'),
    scanOnce = cms.untracked.bool(options.scanOnce),
    datafnPosition = cms.untracked.uint32(options.datafnPosition),
    delayMillis = cms.untracked.uint32(500),
    nextLumiTimeoutMillis = cms.untracked.int32(nextLumiTimeoutMillis),
    skipFirstLumis = cms.untracked.bool(options.skipFirstLumis),
    deleteDatFiles = cms.untracked.bool(False),
    loadFiles = cms.untracked.bool(True),
    endOfRunKills  = cms.untracked.bool(endOfRunKills),
)

# https://twiki.cern.ch/twiki/bin/viewauth/CMS/CMSBeamSplash2017
def set_BeamSplashRun_settings( source ):
  # source.minEventsPerLumi      = 1000000
  source.nextLumiTimeoutMillis = 15000

if options.BeamSplashRun : set_BeamSplashRun_settings( source )

print("Initial Source settings:", source)
    
