import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils
import FWCore.ParameterSet.VarParsing as VarParsing
import sys

from Configuration.StandardSequences.Eras import eras

options = VarParsing.VarParsing ()
options.register ('era',
                  '2017', # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,         # string, int, or float
                  "CMS running era")

options.register ('FileList',
                  'files.txt', # default value
                  VarParsing.VarParsing.multiplicity.singleton, 
                  VarParsing.VarParsing.varType.string,
                  "FileList in DAS format")

options.register ('outputFile',
                  'myAnaTree.root', # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,         # string, int, or float
                  "output file")

options.parseArguments()
print "inputFile: ", options.FileList
print "outputFile: ", options.outputFile
print "era: ", options.era

if   options.era=='2016':
    print "running era 2016"
    process = cms.Process('Analysis',eras.Run2_2016)
elif options.era=='2017':
    print "running era 2017"
    process = cms.Process('Analysis',eras.Run2_2017)
elif options.era=='2018':
    print "running era 2018"
    process = cms.Process('Analysis',eras.Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '113X_mc2017_realistic_v4', '')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

filelist = FileUtils.loadListFromFile (options.FileList)
readFiles = cms.untracked.vstring( *filelist)

process.source = cms.Source("PoolSource",
                            #fileNames = cms.untracked.vstring('/store/relval/CMSSW_10_6_1/RelValZMM_13/GEN-SIM-RECO/PU25ns_106X_mc2017_realistic_v6_HS-v1/10000/7A8BCA04-DEEF-A048-90FF-BFA2BD1A891F.root',
                            fileNames = readFiles)

# TransientTrack from https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideTransientTracks
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorOpposite_cfi')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi')
process.load('TrackingTools.TrackAssociator.DetIdAssociatorESProducer_cff')

####################################################################
# Output file
####################################################################
process.TFileService = cms.Service("TFileService",fileName=cms.string("plots.root"))

# Additional output definition
process.analysis = cms.EDAnalyzer("DiMuonVertexValidator",
                                  muons  = cms.InputTag('muons'),
                                  tracks = cms.InputTag('generalTracks'))

process.p = cms.Path(process.analysis)
