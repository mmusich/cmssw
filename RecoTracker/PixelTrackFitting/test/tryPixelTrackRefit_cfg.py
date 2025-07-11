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
readFiles = cms.untracked.vstring('file:testSlimmingTest.root')

process.source = cms.Source("PoolSource",
                            fileNames = readFiles,
                            duplicateCheckMode = cms.untracked.string('checkAllFilesOpened')
                            )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )

####################################################################
# Get Multi-threading going
####################################################################
process.options.numberOfThreads = 1
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
process.FinalTrackRefitter.src = "pixelTracks"
process.FinalTrackRefitter.TrajectoryInEvent = True
process.FinalTrackRefitter.NavigationSchool = ''
process.FinalTrackRefitter.TTRHBuilder = "WithTrackAngle"

####################################################################
# Load and Configure Common Track Selection and refitting sequence
####################################################################
# import Alignment.CommonAlignment.tools.trackselectionRefitting as trackselRefit
# process.seqTrackselRefit = trackselRefit.getSequence(process,"ALCARECOTkAlHLTPixelZMuMuVertexTracks",
#                                                      isPVValidation=True, 
#                                                      TTRHBuilder='WithTrackAngle',
#                                                      usePixelQualityFlag=False,
#                                                      openMassWindow=False,
#                                                      cosmicsDecoMode=True,
#                                                      cosmicsZeroTesla=False,
#                                                      momentumConstraint=None,
#                                                      cosmicTrackSplitting=False,
#                                                      use_d0cut=False,
#                                                      )
     
####################################################################
# swap the bemspot
####################################################################
process.load("RecoVertex.BeamSpotProducer.BeamSpotOnline_cfi")
from RecoVertex.BeamSpotProducer.BeamSpotOnline_cfi import onlineBeamSpotProducer as _onlineBeamSpotProducer
process.offlineBeamSpot = _onlineBeamSpotProducer.clone()

####################################################################
# Set the IBC off
####################################################################
#process.PixelCPEGenericESProducer.IrradiationBiasCorrection = cms.bool(False) # set IBC off

###################################################################
# Analyzer
###################################################################
process.LhcTrackAnalyzer = cms.EDAnalyzer("LhcTrackAnalyzer",
                                          #TrackCollectionTag = cms.InputTag("ALCARECOTkAlHLTPixelZMuMuVertexTracks"),
                                          TrackCollectionTag = cms.InputTag("FinalTrackRefitter"),
                                          PVtxCollectionTag = cms.InputTag("hltPixelVertices"),
                                          acceptedBX        = cms.vuint32(), # (51,2724)
                                          OutputFileName    = cms.string("AnalyzerOutput_1_IBC_off.root"),
                                          Debug = cms.bool(False)
                                          )

process.myanalysis = cms.EDAnalyzer("GeneralPurposeTrackAnalyzer",
                                    #TkTag  = cms.InputTag('ALCARECOTkAlHLTPixelZMuMuVertexTracks'),
                                    VerticesTag = cms.InputTag("hltVerticesPFFilter"),
                                    TkTag = cms.InputTag("FinalTrackRefitter"),
                                    isCosmics = cms.bool(False)
                                    )


process.vertexanalysis = cms.EDAnalyzer('GeneralPurposeVertexAnalyzer',
                                        ndof = cms.int32(4),
                                        vertexLabel = cms.InputTag('hltPixelVertices'),
                                        beamSpotLabel = cms.InputTag('offlineBeamSpot'),
                                        distToVtx = cms.InputTag('ALCARECOTkAlHLTZMuMuVertexDistanceValueMap'),
                                        Xpos = cms.double(0.1),
                                        Ypos = cms.double(0),
                                        TkSizeBin = cms.int32(100),
                                        TkSizeMin = cms.double(499.5),
                                        TkSizeMax = cms.double(-0.5),
                                        DxyBin = cms.int32(100),
                                        DxyMin = cms.double(-2000),
                                        DxyMax = cms.double(2000),
                                        DzBin = cms.int32(100),
                                        DzMin = cms.double(-2000),
                                        DzMax = cms.double(2000),
                                        PhiBin = cms.int32(32),
                                        PhiBin2D = cms.int32(12),
                                        PhiMin = cms.double(-3.1415926535897931),
                                        PhiMax = cms.double(3.1415926535897931),
                                        EtaBin = cms.int32(26),
                                        EtaBin2D = cms.int32(8),
                                        EtaMin = cms.double(-2.7),
                                        EtaMax = cms.double(2.7))


process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("test_out_IBCon.root")
                                   )

process.p = cms.Path(process.offlineBeamSpot +
                     process.FinalTrackRefitter +
                     #process.seqTrackselRefit+                     
                     process.LhcTrackAnalyzer +
                     #process.vertexanalysis +
                     process.myanalysis)
