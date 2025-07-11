import sys
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3
process = cms.Process("BeamMonitorLegacy", Run3)

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1

# process.MessageLogger = cms.Service("MessageLogger",
#                                     debugModules = cms.untracked.vstring('*'),
#                                     cerr = cms.untracked.PSet(
#                                         threshold = cms.untracked.string('WARNING')
#                                     ),
#                                     destinations = cms.untracked.vstring('cerr'))


readFiles = cms.untracked.vstring('/store/express/Run2025D/ExpressPhysics/FEVT/Express-v1/000/394/431/00000/2cf0304c-9892-40f1-8551-971b0e9f1014.root')

process.source = cms.Source ("PoolSource",
                             fileNames = readFiles,
                             ### As we are testing with FEVT, we don't want any unpacked collection
                             ### This makes the tests slightly more realistic (live production uses streamer files
                             inputCommands = cms.untracked.vstring(
                                 'drop *',
                                 'keep FEDRawDataCollection_rawDataCollector_*_*',
                                 'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
                                 'keep edmTriggerResults_TriggerResults_*_*'
                             ),
                             dropDescendantsOfDroppedBranches = cms.untracked.bool(True))

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(50))
process.options.numberOfThreads = 1

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag as gtCustomise
process.GlobalTag = gtCustomise(process.GlobalTag, '150X_dataRun3_HLT_v1', '')

#--------------------------------------------------------
# Swap offline <-> online BeamSpot as in Express and HLT
import RecoVertex.BeamSpotProducer.onlineBeamSpotESProducer_cfi as _mod
process.BeamSpotESProducer = _mod.onlineBeamSpotESProducer.clone()
import RecoVertex.BeamSpotProducer.BeamSpotOnline_cfi
process.offlineBeamSpot = RecoVertex.BeamSpotProducer.BeamSpotOnline_cfi.onlineBeamSpotProducer.clone()

#----------------
# Setup tracking
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load("Configuration.StandardSequences.RawToDigi_Data_cff")
process.load("RecoLocalTracker.Configuration.RecoLocalTracker_cff")
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
from RecoTracker.PixelLowPtUtilities.siPixelClusterShapeCache_cfi import *
process.siPixelClusterShapeCachePreSplitting = siPixelClusterShapeCache.clone(
  src = 'siPixelClustersPreSplitting'
)
process.load("RecoLocalTracker.SiPixelRecHits.PixelCPEGeneric_cfi")

process.pixelTracksCutClassifier = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "pixelTracks" ),
    beamspot = cms.InputTag( "offlineBeamSpot" ),
    vertices = cms.InputTag( "" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet(
      minPixelHits = cms.vint32( 0, 3, 3 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 3.40282346639E38, 60.0 ),
      dr_par = cms.PSet(
        d0err = cms.vdouble( 0.003, 0.003, 3.40282346639E38 ),
        dr_par2 = cms.vdouble( 0.3, 0.3, 3.40282346639E38 ),
        dr_par1 = cms.vdouble( 0.4, 0.4, 3.40282346639E38 ),
        dr_exp = cms.vint32( 4, 4, 4 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 3.40282346639E38 )
      ),
      maxLostLayers = cms.vint32( 99, 99, 99 ),
      min3DLayers = cms.vint32( 0, 2, 3 ),
      dz_par = cms.PSet(
        dz_par1 = cms.vdouble( 0.4, 0.4, 3.40282346639E38 ),
        dz_par2 = cms.vdouble( 0.35, 0.35, 3.40282346639E38 ),
        dz_exp = cms.vint32( 4, 4, 4 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 3.40282346639E38, 3.40282346639E38, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 9999., 9999., 30.0 ),
      maxDr = cms.vdouble( 99., 99., 1. ),
      minLayers = cms.vint32( 0, 2, 3 )
    ),
    ignoreVertices = cms.bool( True ),
)

#
process.pixelTracksHP = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "pixelTracks" ),
    originalQualVals = cms.InputTag( 'pixelTracksCutClassifier','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'pixelTracksCutClassifier','MVAValues' )
)


process.tracks2monitor = cms.EDFilter('TrackSelector',
    src = cms.InputTag('pixelTracks'),
    cut = cms.string("")
)
process.tracks2monitor.src = 'pixelTracksHP'
process.tracks2monitor.cut = 'pt > 1 & abs(eta) < 2.4' 

#process.selectedPixelTracksMonitorSequence = cms.Sequence(
#    process.pixelTracksCutClassifier
#  + process.pixelTracksHP
#  + process.tracks2monitor
#  + process.selectedPixelTracksMonitor
#)

# Digitisation: produce the TCDS digis containing BST record
from EventFilter.OnlineMetaDataRawToDigi.tcdsRawToDigi_cfi import *
process.tcdsDigis = tcdsRawToDigi.clone()

rawDataInputTag = "rawDataCollector"
process.castorDigis.InputLabel           = rawDataInputTag
process.csctfDigis.producer              = rawDataInputTag 
process.dttfDigis.DTTF_FED_Source        = rawDataInputTag
process.ecalPreshowerDigis.sourceTag     = rawDataInputTag
process.gctDigis.inputLabel              = rawDataInputTag
process.gtDigis.DaqGtInputTag            = rawDataInputTag
process.hcalDigis.InputLabel             = rawDataInputTag
process.muonCSCDigis.InputObjects        = rawDataInputTag
process.muonDTDigis.inputLabel           = rawDataInputTag
process.muonRPCDigis.InputLabel          = rawDataInputTag
process.scalersRawToDigi.scalersInputTag = rawDataInputTag
process.siPixelDigis.InputLabel          = rawDataInputTag
process.siStripDigis.ProductLabel        = rawDataInputTag
process.tcdsDigis.InputLabel             = rawDataInputTag

process.load("RecoVertex.BeamSpotProducer.BeamSpot_cfi")

#----------------------------
# Pixel tracks/vertices reco
process.load("RecoVertex.Configuration.RecoPixelVertexing_cff")
from RecoVertex.PrimaryVertexProducer.OfflinePixel3DPrimaryVertices_cfi import *
process.pixelVertices = pixelVertices.clone(
  TkFilterParameters = dict( minPt = process.pixelTracksTrackingRegions.RegionPSet.ptMin)
)
#process.pixelTracksTrackingRegions.RegionPSet.ptMin = 0.1       # used in PilotBeam 2021, but not ok for standard collisions
process.pixelTracksTrackingRegions.RegionPSet.originRadius = 0.4 # used in PilotBeam 2021, to be checked again for standard collisions
# The following parameters were used in 2018 HI:
#process.pixelTracksTrackingRegions.RegionPSet.originHalfLength = 12
#process.pixelTracksTrackingRegions.RegionPSet.originXPos =  0.08
#process.pixelTracksTrackingRegions.RegionPSet.originYPos = -0.03
#process.pixelTracksTrackingRegions.RegionPSet.originZPos = 0.

process.tracking_FirstStep = cms.Sequence(
    process.siPixelDigis 
    * process.siStripDigis
    * process.striptrackerlocalreco
    * process.offlineBeamSpot
    * process.siPixelClustersPreSplitting
    * process.siPixelRecHitsPreSplitting
    * process.siPixelClusterShapeCachePreSplitting
    * process.recopixelvertexing)

#--------
# Do no run on events with pixel or strip with HV off

process.stripTrackerHVOn = cms.EDFilter( "DetectorStateFilter",
    DCSRecordLabel = cms.untracked.InputTag( "onlineMetaDataDigis" ),
    DcsStatusLabel = cms.untracked.InputTag( "scalersRawToDigi" ),
    DebugOn = cms.untracked.bool( False ),
    DetectorType = cms.untracked.string( "sistrip" )
)

process.pixelTrackerHVOn = cms.EDFilter( "DetectorStateFilter",
    DCSRecordLabel = cms.untracked.InputTag( "onlineMetaDataDigis" ),
    DcsStatusLabel = cms.untracked.InputTag( "scalersRawToDigi" ),
    DebugOn = cms.untracked.bool( False ),
    DetectorType = cms.untracked.string( "pixel" )
)

process.p = cms.Path(process.scalersRawToDigi
                     * process.tcdsDigis
                     * process.onlineMetaDataDigis
                     * process.pixelTrackerHVOn
                     * process.stripTrackerHVOn
                     * process.tracking_FirstStep)

process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('testSlimmingTest.root'),
                               outputCommands = cms.untracked.vstring(
                                   'keep *',
                                   #'keep *_trackOfThingsProducerB_*_*',
                                   #'keep *_trackOfThingsProducerI_*_*',
                                   #'keep *_thinningThingProducerB_*_*',
                                   #'keep *_thinningThingProducerCI_*_*',
                               ))

process.ep = cms.EndPath(process.out)

print("Global Tag used:", process.GlobalTag.globaltag.value())
print("Final Source settings:", process.source)
