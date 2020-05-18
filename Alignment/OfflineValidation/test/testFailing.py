
import FWCore.ParameterSet.Config as cms

process = cms.Process("PrimaryVertexValidation")

#process.load("Alignment.OfflineValidation.Dataset_HLTPhysics_Run2018C_PromptReco_319347to319657_cff")
readFiles = cms.untracked.vstring()
readFiles.extend(['/store/express/Run2018C/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/319/347/00000/E230C5AB-1383-E811-BB27-FA163EA114BD.root'])
process.source = cms.Source("PoolSource",
                            fileNames = readFiles ,
                            duplicateCheckMode = cms.untracked.string('checkAllFilesOpened')
                            )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000 / 1)
)
process.source.skipEvents=cms.untracked.uint32(0*100000/1)

process.options = cms.untracked.PSet(
   wantSummary = cms.untracked.bool(False),
   Rethrow = cms.untracked.vstring("ProductNotFound"), # make this exception fatal
   fileMode  =  cms.untracked.string('NOMERGE') # no ordering needed, but calls endRun/beginRun etc. at file boundaries
)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.MessageLogger.statistics.append('cout')


process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
process.load("Configuration.Geometry.GeometryRecoDB_cff")
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
#process.GlobalTag = GlobalTag(process.GlobalTag,"106X_dataRun3_Express_v2")
process.GlobalTag = GlobalTag(process.GlobalTag,"102X_dataRun2_Prompt_v7")

import CalibTracker.Configuration.Common.PoolDBESSource_cfi

# process.conditionsInBeamSpotObjectsRcd = CalibTracker.Configuration.Common.PoolDBESSource_cfi.poolDBESSource.clone(
#      connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
#      toGet = cms.VPSet(cms.PSet(record = cms.string('BeamSpotObjectsRcd'),
#                                tag = cms.string('BeamSpotObjects_PCL_byLumi_v0_prompt')
#                                )
#                       )
#     )
# process.prefer_conditionsInBeamSpotObjectsRcd = cms.ESPrefer("PoolDBESSource", "conditionsInBeamSpotObjectsRcd")



isDA = True
isMC = True

###################################################################
#  Runs and events
###################################################################
runboundary = 1
isMultipleRuns=False
if(isinstance(runboundary, (list, tuple))):
     isMultipleRuns=True
     print "Multiple Runs are selected"
       
if(isMultipleRuns):
     process.source.firstRun = cms.untracked.uint32(int(runboundary[0]))
else:
     process.source.firstRun = cms.untracked.uint32(int(runboundary)) 

###################################################################
# JSON Filtering
###################################################################
if isMC:
     print ">>>>>>>>>> testPVValidation_cfg.py: msg%-i: This is simulation!"
     runboundary = 1
else:
     print ">>>>>>>>>> testPVValidation_cfg.py: msg%-i: This is real DATA!"
     if ('None'):
          print ">>>>>>>>>> testPVValidation_cfg.py: msg%-i: JSON filtering with: None "
          import FWCore.PythonUtilities.LumiList as LumiList
          process.source.lumisToProcess = LumiList.LumiList(filename ='None').getVLuminosityBlockRange()

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
process.filterOutLowPt.ptmin = 3.
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
# Deterministic annealing clustering
####################################################################
if isDA:
     print ">>>>>>>>>> testPVValidation_cfg.py: msg%-i: Running DA Algorithm!"
     process.PVValidation = cms.EDAnalyzer("PrimaryVertexValidation",
                                           TrackCollectionTag = cms.InputTag("FinalTrackRefitter"),
                                           VertexCollectionTag = cms.InputTag("offlinePrimaryVertices"),
                                           Debug = cms.bool(False),
                                           storeNtuple = cms.bool(False),
                                           useTracksFromRecoVtx = cms.bool(False),
                                           isLightNtuple = cms.bool(True),
                                           askFirstLayerHit = cms.bool(False),
                                           forceBeamSpot = cms.untracked.bool(False),
                                           probePt  = cms.untracked.double(3.),
                                           probeEta = cms.untracked.double(2.5),
                                           doBPix   = cms.untracked.bool(True),
                                           doFPix   = cms.untracked.bool(True),
                                           numberOfBins = cms.untracked.int32(48),
                                           runControl = cms.untracked.bool(False),
                                           runControlNumber = cms.untracked.vuint32(runboundary),
                                           
                                           TkFilterParameters = cms.PSet(algorithm=cms.string('filter'),                           
                                                                         maxNormalizedChi2 = cms.double(5.0),                        # chi2ndof < 5                  
                                                                         minPixelLayersWithHits = cms.int32(2),                      # PX hits > 2                       
                                                                         minSiliconLayersWithHits = cms.int32(5),                    # TK hits > 5  
                                                                         maxD0Significance = cms.double(5.0),                        # fake cut (requiring 1 PXB hit)     
                                                                         minPt = cms.double(0.0),                                    # better for softish events                        
                                                                         maxEta = cms.double(5.0),                                   # as per recommendation in PR #18330
                                                                         trackQuality = cms.string("any")
                                                                         ),

                                           ## MM 04.05.2017 (use settings as in: https://github.com/cms-sw/cmssw/pull/18330)
                                           TkClusParameters=cms.PSet(algorithm=cms.string('DA_vect'),
                                                                     TkDAClusParameters = cms.PSet(coolingFactor = cms.double(0.6),  # moderate annealing speed
                                                                                                   Tmin = cms.double(2.0),           # end of vertex splitting
                                                                                                   Tpurge = cms.double(2.0),         # cleaning
                                                                                                   Tstop = cms.double(0.5),          # end of annealing
                                                                                                   vertexSize = cms.double(0.006),   # added in quadrature to track-z resolutions
                                                                                                   d0CutOff = cms.double(3.),        # downweight high IP tracks
                                                                                                   dzCutOff = cms.double(3.),        # outlier rejection after freeze-out (T<Tmin)
                                                                                                   zmerge = cms.double(1e-2),        # merge intermediat clusters separated by less than zmerge
                                                                                                   uniquetrkweight = cms.double(0.8) # require at least two tracks with this weight at T=Tpurge
                                                                                                   )
                                                                     )
                                           )

####################################################################
# GAP clustering
####################################################################
else:
     print ">>>>>>>>>> testPVValidation_cfg.py: msg%-i: Running GAP Algorithm!"
     process.PVValidation = cms.EDAnalyzer("PrimaryVertexValidation",
                                           TrackCollectionTag = cms.InputTag("FinalTrackRefitter"),
                                           VertexCollectionTag = cms.InputTag("offlinePrimaryVertices"),
                                           Debug = cms.bool(False),
                                           isLightNtuple = cms.bool(True),
                                           storeNtuple = cms.bool(False),
                                           useTracksFromRecoVtx = cms.bool(False),
                                           askFirstLayerHit = cms.bool(False),
                                           forceBeamSpot = cms.untracked.bool(False),
                                           probePt = cms.untracked.double(3.),
                                           probeEta = cms.untracked.double(2.5),
                                           doBPix   = cms.untracked.bool(True),
                                           doFPix   = cms.untracked.bool(True),
                                           numberOfBins = cms.untracked.int32(48),
                                           runControl = cms.untracked.bool(False),
                                           runControlNumber = cms.untracked.vuint32(int(1)),

                                           TkFilterParameters = cms.PSet(algorithm=cms.string('filter'),
                                                                         maxNormalizedChi2 = cms.double(5.0),                        # chi2ndof < 20
                                                                         minPixelLayersWithHits=cms.int32(2),                        # PX hits > 2
                                                                         minSiliconLayersWithHits = cms.int32(5),                    # TK hits > 5
                                                                         maxD0Significance = cms.double(5.0),                        # fake cut (requiring 1 PXB hit)
                                                                         minPt = cms.double(0.0),                                    # better for softish events
                                                                         maxEta = cms.double(5.0),                                   # as per recommendation in PR #18330
                                                                         trackQuality = cms.string("any")
                                                                         ),

                                           TkClusParameters = cms.PSet(algorithm   = cms.string('gap'),
                                                                       TkGapClusParameters = cms.PSet(zSeparation = cms.double(0.2)  # 0.2 cm max separation betw. clusters
                                                                                                      )
                                                                       )
                                           )



process.TFileService = cms.Service("TFileService",
    fileName = cms.string('test.root')
)



process.p = cms.Path(process.goodvertexSkim*
                     process.seqTrackselRefit*
                     process.PVValidation)


print("Done")
