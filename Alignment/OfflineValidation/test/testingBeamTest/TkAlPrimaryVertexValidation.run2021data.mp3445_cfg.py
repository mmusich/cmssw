
import FWCore.ParameterSet.Config as cms

process = cms.Process("PrimaryVertexValidation")

import FWCore.PythonUtilities.LumiList as LumiList

readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
process.source = cms.Source("PoolSource",
                            secondaryFileNames =secFiles,
                            fileNames = readFiles
)

readFiles.extend( [
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/389/00000/0bc2f80c-8059-41f5-a1f7-f62d04b85951.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/389/00000/0e0359a4-f3ec-4cce-a8fd-293413b3ae62.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/389/00000/1223920c-31b6-4abe-bff5-ac93b288eb7e.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/389/00000/30e2919e-3e6c-482d-8f53-147776a2ec04.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/389/00000/45b16915-76e8-49c1-a74c-099aebdab7b8.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/389/00000/91f539ce-af05-443b-b39d-36e4270fe18f.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/389/00000/9f538edb-640d-40cd-a594-3223db4bfaa7.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/389/00000/ac004bd1-3298-4497-9ba8-1cc845d3e772.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/389/00000/f426d556-9380-4eb3-8ebd-1e46df791d08.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/390/00000/3ab3f398-2ab3-42bf-afe0-380bd9180f33.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/390/00000/ba4aafc9-25a0-4c8d-965e-110516934ef0.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/390/00000/ffcc727c-d493-4b52-a082-7a2195af3481.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/394/00000/d4665a6b-4e23-4de3-9172-66bb2312c52d.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/395/00000/1f9e2f81-3a3a-4007-a6f4-10e7b8f4f2a2.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/395/00000/4921e162-96ec-46ab-a1b9-e787e65f64f3.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/395/00000/62dba840-f4b1-4d60-9760-de1eb365229a.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/395/00000/a9c32853-b769-4809-bdd5-b887f103c1c5.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/395/00000/c1d9cc6c-c702-4b09-bc60-4c05fc2ef9f0.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/395/00000/ce21b4a6-1de4-4e8f-b1a4-df36b266c316.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/395/00000/d388101e-37ce-4dbe-8dea-999169eb720e.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/19a17a4c-f4c2-4f53-856d-b631df804777.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/1af0a581-50ca-415b-95e2-09a242993938.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/380c6182-3f14-4748-b6fe-12c295df9fad.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/389c77f8-17a7-4a1c-8ea5-3c320f9e4711.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/7a147400-500d-4eed-bd1f-a274bb1cebe8.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/7f3c8fec-59b1-43a8-82a2-84cdce8adb8f.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/86f21a9b-4b77-4629-8081-abdedcd5cb1c.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/8d88eab6-7b52-4bbc-b450-d263800936d1.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/955adb46-3a62-4486-be74-1fa609f111d6.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/a2b00e8d-4cf3-4a08-b317-cc6f6f11744e.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/a441e34d-a506-4e67-8a79-a34d5fac3af7.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/a849abb6-37d1-4f1c-979a-1a55193fe918.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/ac192233-f347-43b7-8263-34f74da03751.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/bf06fc08-6afc-4899-af43-5006a9a497c5.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/bfa02fe2-bd9c-45b6-9a48-5267377a8909.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/c058fb7b-c23f-47e6-83f8-8080b5de54c8.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/ce599639-ce06-485f-ac70-d32992fbe613.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/ceff9b5c-0dfc-44a4-9d5e-3912034c46fc.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/dd074505-45f3-42f9-8f50-14c012767a45.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/ea43c9a3-f1e1-441d-ae27-22286535e6b1.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/398/00000/5a5897bb-66f5-4756-8d7f-85fba5689f80.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/398/00000/6a9ed916-b190-401d-ab64-b2cdbeb5cedd.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/398/00000/a8272baa-3e60-473b-b5ff-a91d7c429f05.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/398/00000/b724f4d1-b906-46c8-a7cd-a09d04b28e5f.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/398/00000/bfc435ab-0579-4995-98c6-808b79593da2.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/398/00000/d4e9a1d7-6b64-4bac-b201-cc518d21fde7.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/398/00000/dcef1def-a8ce-44ed-8d3b-8bf95d50c875.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/398/00000/f43f8bd4-c7d3-4b4b-a1ce-54ad9e649544.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/412/00000/0c4c02fe-fbe4-4e70-b535-a55e2f8199d5.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/412/00000/1a6f0101-747c-4cc4-a5ed-9f8f48f4bc3b.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/412/00000/93e6a872-8f9a-4e88-8f78-877aa02e3a2e.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/412/00000/96c4ecf2-3a62-479d-9fd8-ffd17e232375.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/412/00000/cc9ebe40-6c58-4c3f-8d74-671386e750da.root',
'root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/412/00000/d90c800c-f98c-4c1c-a4d8-684c7bd363cb.root'
] )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(int(-1 / 1)) )
process.source.skipEvents=cms.untracked.uint32(int(0*-1/1))

process.options = cms.untracked.PSet(
   wantSummary = cms.untracked.bool(False),
   Rethrow = cms.untracked.vstring("ProductNotFound"), # make this exception fatal
   fileMode  =  cms.untracked.string('NOMERGE') # no ordering needed, but calls endRun/beginRun etc. at file boundaries
)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.MessageLogger.cout.enableStatistics = cms.untracked.bool(True)


process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
process.load("Configuration.Geometry.GeometryDB_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")


import Alignment.CommonAlignment.tools.trackselectionRefitting as trackselRefit
process.seqTrackselRefit = trackselRefit.getSequence(process, 'ALCARECOTkAlMinBias',
                                                     isPVValidation=True, 
                                                     TTRHBuilder='WithAngleAndTemplate',
                                                     usePixelQualityFlag=True,
                                                     openMassWindow=False,
                                                     cosmicsDecoMode=True,
                                                     cosmicsZeroTesla=False,
                                                     momentumConstraint=None,
                                                     cosmicTrackSplitting=False,
                                                     use_d0cut=False,
                                                    )




#Global tag
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag,"120X_dataRun3_Express_v2")
process.GlobalTag.toGet = cms.VPSet(cms.PSet(record = cms.string('BeamSpotObjectsRcd'),
                                             connect = cms.string('sqlite_file:/tmp/musich/CMSSW_12_0_3_patch1/src/BeamSpotObjects_2009_v1_express.db'),
                                             tag = cms.string('BeamSpotObjects_2009_v1_express')
                                            )
                                    )

process.GlobalTag.DumpStat = cms.untracked.bool(True)

import CalibTracker.Configuration.Common.PoolDBESSource_cfi

process.conditionsInTrackerAlignmentRcd = CalibTracker.Configuration.Common.PoolDBESSource_cfi.poolDBESSource.clone(
     connect = cms.string('sqlite_file:/afs/cern.ch/user/a/avagneri/MPproduction/mp3445/jobData/jobm/alignments_MP.db'),
     toGet = cms.VPSet(cms.PSet(record = cms.string('TrackerAlignmentRcd'),
                               tag = cms.string('Alignments')
                               )
                      )
    )
process.prefer_conditionsInTrackerAlignmentRcd = cms.ESPrefer("PoolDBESSource", "conditionsInTrackerAlignmentRcd")

isDA = True
isMC = False

###################################################################
#  Runs and events
###################################################################
runboundary = 10
isMultipleRuns=False
if(isinstance(runboundary, (list, tuple))):
     isMultipleRuns=True
     print("Multiple Runs are selected")
       
if(isMultipleRuns):
     process.source.firstRun = cms.untracked.uint32(int(runboundary[0]))
else:
     process.source.firstRun = cms.untracked.uint32(int(runboundary)) 

###################################################################
# JSON Filtering
###################################################################
if isMC:
     print(">>>>>>>>>> testPVValidation_cfg.py: msg%-i: This is simulation!")
     runboundary = 1
else:
     print(">>>>>>>>>> testPVValidation_cfg.py: msg%-i: This is real DATA!")
     #if ('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/DCSOnly/json_DCSONLY.txt'):
     #     print(">>>>>>>>>> testPVValidation_cfg.py: msg%-i: JSON filtering with: /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/DCSOnly/json_DCSONLY.txt ")
     #     import FWCore.PythonUtilities.LumiList as LumiList
     #     process.source.lumisToProcess = LumiList.LumiList(filename ='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/DCSOnly/json_DCSONLY.txt').getVLuminosityBlockRange()

####################################################################
# Produce the Transient Track Record in the event
####################################################################
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")

####################################################################
# Load and Configure event selection
####################################################################
process.primaryVertexFilter = cms.EDFilter("VertexSelector",
                                           src = cms.InputTag("offlinePrimaryVertices"),
                                           cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2"),
                                           filter = cms.bool(True)
                                           )

process.noscraping = cms.EDFilter("FilterOutScraping",
                                  applyfilter = cms.untracked.bool(True),
                                  src =  cms.untracked.InputTag("ALCARECOTkAlMinBias"),
                                  debugOn = cms.untracked.bool(False),
                                  numtrack = cms.untracked.uint32(10),
                                  thresh = cms.untracked.double(0.25)
                                  )


process.load("Alignment.CommonAlignment.filterOutLowPt_cfi")
process.filterOutLowPt.src = "ALCARECOTkAlMinBias"
process.filterOutLowPt.ptmin = 0.5
process.filterOutLowPt.runControl = False
if(isMultipleRuns):
     process.filterOutLowPt.runControlNumber.extend((runboundary))
else:
     process.filterOutLowPt.runControlNumber = [runboundary]
                                
if isMC:
     process.goodvertexSkim = cms.Sequence(process.noscraping + process.filterOutLowPt)
else:
     process.goodvertexSkim = cms.Sequence(process.primaryVertexFilter + process.noscraping + process.filterOutLowPt)

####################################################################
# Imports of parameters
####################################################################
from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import offlinePrimaryVertices
## modify the parameters which differ
FilteringParams = offlinePrimaryVertices.TkFilterParameters.clone(
     maxNormalizedChi2 = 5.0,  # chi2ndof < 5
     maxD0Significance = 5.0,  # fake cut (requiring 1 PXB hit)
     maxEta = 5.0,             # as per recommendation in PR #18330
)

## MM 04.05.2017 (use settings as in: https://github.com/cms-sw/cmssw/pull/18330)
from RecoVertex.PrimaryVertexProducer.TkClusParameters_cff import DA_vectParameters
DAClusterizationParams = DA_vectParameters.clone()

GapClusterizationParams = cms.PSet(algorithm   = cms.string('gap'),
                                   TkGapClusParameters = cms.PSet(zSeparation = cms.double(0.2))  # 0.2 cm max separation betw. clusters
                                   )

####################################################################
# Deterministic annealing clustering or Gap clustering
####################################################################
def switchClusterizerParameters(da):
     if da:
          print(">>>>>>>>>> testPVValidation_cfg.py: msg%-i: Running DA Algorithm!")
          return DAClusterizationParams
     else:
          print(">>>>>>>>>> testPVValidation_cfg.py: msg%-i: Running GAP Algorithm!")
          return GapClusterizationParams

# Use compressions settings of TFile
# see https://root.cern.ch/root/html534/TFile.html#TFile:SetCompressionSettings
# settings = 100 * algorithm + level
# level is from 1 (small) to 9 (large compression)
# algo: 1 (ZLIB), 2 (LMZA)
# see more about compression & performance: https://root.cern.ch/root/html534/guides/users-guide/InputOutput.html#compression-and-performance
compressionSettings = 207

####################################################################
# Configure the PVValidation Analyzer module
####################################################################
process.PVValidation = cms.EDAnalyzer("PrimaryVertexValidation",
                                      compressionSettings = cms.untracked.int32(compressionSettings),
                                      TrackCollectionTag = cms.InputTag("FinalTrackRefitter"),
                                      VertexCollectionTag = cms.InputTag("offlinePrimaryVertices"),
                                      Debug = cms.bool(False),
                                      storeNtuple = cms.bool(False),
                                      useTracksFromRecoVtx = cms.bool(False),
                                      isLightNtuple = cms.bool(True),
                                      askFirstLayerHit = cms.bool(False),
                                      forceBeamSpot = cms.untracked.bool(False),
                                      probePt  = cms.untracked.double(0.5),
                                      probeEta = cms.untracked.double(2.5),
                                      doBPix   = cms.untracked.bool(True),
                                      doFPix   = cms.untracked.bool(True),
                                      numberOfBins = cms.untracked.int32(48),
                                      runControl = cms.untracked.bool(False),
                                      runControlNumber = cms.untracked.vuint32(runboundary),
                                      TkFilterParameters = FilteringParams,
                                      TkClusParameters = switchClusterizerParameters(isDA)
                                      )


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('PrimaryVertexValidation_run2021data_mp3445.root')
)



process.p = cms.Path(#process.goodvertexSkim*
                     process.seqTrackselRefit*
                     process.PVValidation)


print("Done")
