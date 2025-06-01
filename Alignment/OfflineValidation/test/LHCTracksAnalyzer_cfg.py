import FWCore.ParameterSet.Config as cms
process = cms.Process("Demo")

###################################################################
# Messages
###################################################################
process.load("FWCore.MessageService.MessageLogger_cfi")
MessageLogger = cms.Service("MessageLogger",
                            cout = cms.untracked.PSet(
                                threshold = cms.untracked.string('WARNING')
                            ),
                            destinations = cms.untracked.vstring('cout')
                            )
process.MessageLogger.cerr.FwkReport.reportEvery = 100

###################################################################
# Conditions
###################################################################
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '150X_dataRun3_HLT_v1', '')

###################################################################
# Event source
###################################################################
print('Loading file list from ASCII file')
import FWCore.Utilities.FileUtils as FileUtils
filelist = FileUtils.loadListFromFile ('listOfFiles_392732.txt')
readFiles = cms.untracked.vstring( *filelist)

process.source = cms.Source("PoolSource",
                            fileNames = readFiles,
                            duplicateCheckMode = cms.untracked.string('checkAllFilesOpened')
                            )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

####################################################################
# Get the Magnetic Field
####################################################################
process.load('Configuration.StandardSequences.MagneticField_cff')

###################################################################
# Standard loads
###################################################################
process.load("Configuration.Geometry.GeometryRecoDB_cff")

###################################################################
# Analyzer
###################################################################
process.LhcTrackAnalyzer = cms.EDAnalyzer("LhcTrackAnalyzer",
                                          TrackCollectionTag = cms.InputTag("ALCARECOTkAlHLTTracks"),
                                          PVtxCollectionTag = cms.InputTag("hltVerticesPFFilter"),
                                          acceptedBX        = cms.vuint32(), # (51,2724)
                                          OutputFileName    = cms.string("AnalyzerOutput_1.root"),
                                          Debug = cms.bool(False)
                                          )

process.myanalysis = cms.EDAnalyzer("GeneralPurposeTrackAnalyzer",
                                    TkTag  = cms.InputTag('ALCARECOTkAlHLTTracks'),
                                    isCosmics = cms.bool(False)
                                    )

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("test_out.root")
                                   )

process.p = cms.Path(#process.LhcTrackAnalyzer
    process.myanalysis    
)
