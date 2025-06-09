import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras
process = cms.Process("Demo",eras.Run3_2025)

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

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )

####################################################################
# Get Multi-threading going
####################################################################
process.options.numberOfThreads = 8
process.options.numberOfStreams = 0

####################################################################
# Get the Magnetic Field
####################################################################
process.load('Configuration.StandardSequences.MagneticField_cff')

###################################################################
# Standard loads
###################################################################
process.load("Configuration.Geometry.GeometryRecoDB_cff")

####################################################################
# Load and Configure TrackRefitter
####################################################################
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
import RecoTracker.TrackProducer.TrackRefitters_cff
process.FinalTrackRefitter = RecoTracker.TrackProducer.TrackRefitter_cfi.TrackRefitter.clone()
process.FinalTrackRefitter.src = "ALCARECOTkAlHLTTracks"
process.FinalTrackRefitter.TrajectoryInEvent = True
process.FinalTrackRefitter.NavigationSchool = ''
process.FinalTrackRefitter.TTRHBuilder = "WithTrackAngle"

####################################################################
# Load and Configure Common Track Selection and refitting sequence
####################################################################
import Alignment.CommonAlignment.tools.trackselectionRefitting as trackselRefit
process.seqTrackselRefit = trackselRefit.getSequence(process,"ALCARECOTkAlHLTTracks",
                                                     isPVValidation=True, 
                                                     TTRHBuilder='WithTrackAngle',
                                                     usePixelQualityFlag=False,
                                                     openMassWindow=False,
                                                     cosmicsDecoMode=True,
                                                     cosmicsZeroTesla=False,
                                                     momentumConstraint=None,
                                                     cosmicTrackSplitting=False,
                                                     use_d0cut=False,
                                                     )
     
####################################################################
# swap the bemspot
####################################################################
process.load("RecoVertex.BeamSpotProducer.BeamSpotOnline_cfi")
from RecoVertex.BeamSpotProducer.BeamSpotOnline_cfi import onlineBeamSpotProducer as _onlineBeamSpotProducer
process.offlineBeamSpot = _onlineBeamSpotProducer.clone()

###################################################################
# Analyzer
###################################################################
process.LhcTrackAnalyzer = cms.EDAnalyzer("LhcTrackAnalyzer",
                                          #TrackCollectionTag = cms.InputTag("ALCARECOTkAlHLTTracks"),
                                          TrackCollectionTag = cms.InputTag("FinalTrackRefitter"),
                                          PVtxCollectionTag = cms.InputTag("hltVerticesPFFilter"),
                                          acceptedBX        = cms.vuint32(), # (51,2724)
                                          OutputFileName    = cms.string("AnalyzerOutput_1.root"),
                                          Debug = cms.bool(False)
                                          )

process.myanalysis = cms.EDAnalyzer("GeneralPurposeTrackAnalyzer",
                                    #TkTag  = cms.InputTag('ALCARECOTkAlHLTTracks'),
                                    TkTag = cms.InputTag("FinalTrackRefitter"),
                                    isCosmics = cms.bool(False)
                                    )

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("test_out.root")
                                   )

process.p = cms.Path(process.offlineBeamSpot+
                     #process.FinalTrackRefitter+
                     process.seqTrackselRefit+
                     #process.LhcTrackAnalyzer+
                     process.myanalysis    
)
