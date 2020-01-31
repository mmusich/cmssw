from enum import Enum
import FWCore.ParameterSet.Config as cms

class RefitType(Enum):
     STANDARD = 1
     COMMON   = 2

from Configuration.Eras.Era_Phase2C9_cff import Phase2C9
process = cms.Process("PrimaryVertexValidation",Phase2C9)
#process = cms.Process("PrimaryVertexValidation")

theRefitter = RefitType.STANDARD
#theRefitter = RefitType.COMMON

###################################################################
# Event source and run selection
###################################################################
readFiles = cms.untracked.vstring()
# readFiles.extend(['/store/relval/CMSSW_11_0_0_pre13/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/7598F940-58A7-B04C-8F88-6F198E53800A.root',
#                   '/store/relval/CMSSW_11_0_0_pre13/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/F8DFC2E5-DE92-024E-AE8B-660A06FEFD8F.root',
#                   '/store/relval/CMSSW_11_0_0_pre13/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/A99D053A-C7FA-F640-9E90-3DA049C8AB82.root',
#                   '/store/relval/CMSSW_11_0_0_pre13/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/4C677F3B-7F44-754C-BC79-0F36CB13C3EF.root',
#                   '/store/relval/CMSSW_11_0_0_pre13/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/E0BF38DB-E612-1F49-9D09-CFA673A7A537.root',
#                   '/store/relval/CMSSW_11_0_0_pre13/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/B77B9AB7-ADCE-ED45-85ED-5C4C8317DB48.root',
#                   '/store/relval/CMSSW_11_0_0_pre13/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/604778C0-B5A4-5C4A-B9C6-F97387D33782.root',
#                   '/store/relval/CMSSW_11_0_0_pre13/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/30880C03-C432-224B-9018-09CAC0C34B3D.root',
#                   '/store/relval/CMSSW_11_0_0_pre13/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/086D0DCD-83E2-E649-86C5-DA4E8C6EB0D0.root',
#                   '/store/relval/CMSSW_11_0_0_pre13/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/825EC4AC-F823-0D44-9A9A-418AE00F022D.root'])


# readFiles.extend(['/store/relval/CMSSW_11_0_0_pre13/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/7598F940-58A7-B04C-8F88-6F198E53800A.root',
#                   '/store/relval/CMSSW_11_0_0_pre13/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/F8DFC2E5-DE92-024E-AE8B-660A06FEFD8F.root',
#                   '/store/relval/CMSSW_11_0_0_pre13/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/A99D053A-C7FA-F640-9E90-3DA049C8AB82.root',
#                   '/store/relval/CMSSW_11_0_0_pre13/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/4C677F3B-7F44-754C-BC79-0F36CB13C3EF.root',
#                   '/store/relval/CMSSW_11_0_0_pre13/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/E0BF38DB-E612-1F49-9D09-CFA673A7A537.root',
#                   '/store/relval/CMSSW_11_0_0_pre13/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/B77B9AB7-ADCE-ED45-85ED-5C4C8317DB48.root',
#                   '/store/relval/CMSSW_11_0_0_pre13/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/604778C0-B5A4-5C4A-B9C6-F97387D33782.root',
#                   '/store/relval/CMSSW_11_0_0_pre13/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/30880C03-C432-224B-9018-09CAC0C34B3D.root',
#                   '/store/relval/CMSSW_11_0_0_pre13/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/086D0DCD-83E2-E649-86C5-DA4E8C6EB0D0.root',
#                   '/store/relval/CMSSW_11_0_0_pre13/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/825EC4AC-F823-0D44-9A9A-418AE00F022D.root'])

readFiles.extend(['/store/relval/CMSSW_11_1_0_pre1/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/8C2E6662-D26E-9544-9B96-A22E8C15D020.root',
                  '/store/relval/CMSSW_11_1_0_pre1/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/C161BDE6-01A2-1B41-973A-BBB6B6574FDE.root',
                  '/store/relval/CMSSW_11_1_0_pre1/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/E59B8148-3EFF-F745-91AA-CFAADA49EA67.root',
                  '/store/relval/CMSSW_11_1_0_pre1/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/DBBBEEB5-B5E2-1C41-89A3-E45E1710E7AC.root',
                  '/store/relval/CMSSW_11_1_0_pre1/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/9A0A2939-44FA-8740-A2F2-AEDF212B4A1D.root',
                  '/store/relval/CMSSW_11_1_0_pre1/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/10F7876E-3DC4-054E-AD80-4F4C8D1B9DF8.root',
                  '/store/relval/CMSSW_11_1_0_pre1/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/9D048C4F-37E5-9E4C-ACF4-D24311CA63C2.root',
                  '/store/relval/CMSSW_11_1_0_pre1/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/8D150376-899F-4F40-85A3-C1AD8C14E59F.root',
                  '/store/relval/CMSSW_11_1_0_pre1/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/AC13E089-65FB-A14D-A99F-762393467158.root',
                  '/store/relval/CMSSW_11_1_0_pre1/RelValTTbar_14TeV/GEN-SIM-RECO/110X_mcRun4_realistic_v2_2026D49noPU-v1/20000/D83CF99B-CE0A-124D-B838-0CA39A6E78D8.root'])

process.source = cms.Source("PoolSource",
                            fileNames = readFiles ,
                            duplicateCheckMode = cms.untracked.string('checkAllFilesOpened')
                            )

process.maxEvents = cms.untracked.PSet(
     input = cms.untracked.int32(10000)
)
#process.source.skipEvents=cms.untracked.uint32(0*250000/40)

process.options = cms.untracked.PSet(
   wantSummary = cms.untracked.bool(False),
   Rethrow = cms.untracked.vstring("ProductNotFound"), # make this exception fatal
   fileMode  =  cms.untracked.string('NOMERGE') # no ordering needed, but calls endRun/beginRun etc. at file boundaries
)

###################################################################
# Messages
###################################################################
process.load('FWCore.MessageService.MessageLogger_cfi')   
process.MessageLogger.categories.append("PrimaryVertexValidation")  
process.MessageLogger.categories.append("FilterOutLowPt")  
process.MessageLogger.destinations = cms.untracked.vstring("cout")
process.MessageLogger.cout = cms.untracked.PSet(
    threshold = cms.untracked.string("INFO"),
    default   = cms.untracked.PSet(limit = cms.untracked.int32(0)),                       
    FwkReport = cms.untracked.PSet(limit = cms.untracked.int32(-1),
                                   reportEvery = cms.untracked.int32(100)
                                   ),                                                      
     PrimaryVertexValidation = cms.untracked.PSet( limit = cms.untracked.int32(-1)),
     FilterOutLowPt          = cms.untracked.PSet( limit = cms.untracked.int32(-1)),
    )
process.MessageLogger.statistics.append('cout') 

process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
#process.load("Configuration.Geometry.GeometryDB_cff")
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2026D49_cff')

process.load('Configuration.StandardSequences.Services_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('RecoLocalTracker.Phase2TrackerRecHits.Phase2StripCPEESProducer_cfi')

if(theRefitter == RefitType.COMMON):

     print(">>>>>>>>>> testPVValidation_cfg.py: msg%-i: using the common track selection and refit sequence!")          
     ####################################################################
     # Load and Configure Common Track Selection and refitting sequence
     ####################################################################
     import Alignment.CommonAlignment.tools.trackselectionRefitting as trackselRefit
     process.seqTrackselRefit = trackselRefit.getSequence(process, 'generalTracks',
                                                          isPVValidation=True, 
                                                          #TTRHBuilder='WithAngleAndTemplate',
                                                          TTRHBuilder='WithTrackAngle',
                                                          usePixelQualityFlag=False,
                                                          openMassWindow=False,
                                                          cosmicsDecoMode=True,
                                                          cosmicsZeroTesla=False,
                                                          momentumConstraint=None,
                                                          cosmicTrackSplitting=False,
                                                          use_d0cut=False,
                                                          )


     process.AlignmentTrackSelector.etaMin  = -4.0
     process.AlignmentTrackSelector.etaMax  =  4.0
     process.HighPurityTrackSelector.etaMin  = -4.0
     process.HighPurityTrackSelector.etaMax  =  4.0


elif (theRefitter == RefitType.STANDARD):

     print(">>>>>>>>>> testPVValidation_cfg.py: msg%-i: using the standard single refit sequence!")          
     ####################################################################
     # Load and Configure Measurement Tracker Event
     # (needed in case NavigationSchool is set != '')
     ####################################################################
     # process.load("RecoTracker.MeasurementDet.MeasurementTrackerEventProducer_cfi") 
     # process.MeasurementTrackerEvent.pixelClusterProducer = 'generalTracks'
     # process.MeasurementTrackerEvent.stripClusterProducer = 'generalTracks'
     # process.MeasurementTrackerEvent.inactivePixelDetectorLabels = cms.VInputTag()
     # process.MeasurementTrackerEvent.inactiveStripDetectorLabels = cms.VInputTag()

     ####################################################################
     # Load and Configure TrackRefitter
     ####################################################################
     process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
     import RecoTracker.TrackProducer.TrackRefitters_cff
     process.FinalTrackRefitter = RecoTracker.TrackProducer.TrackRefitter_cfi.TrackRefitter.clone()
     process.FinalTrackRefitter.src = "generalTracks"
     process.FinalTrackRefitter.TrajectoryInEvent = True
     process.FinalTrackRefitter.NavigationSchool = ''
     #process.FinalTrackRefitter.TTRHBuilder = "WithAngleAndTemplate"
     process.FinalTrackRefitter.TTRHBuilder = "WithTrackAngle"

     ####################################################################
     # Sequence
     ####################################################################
     process.seqTrackselRefit = cms.Sequence(process.offlineBeamSpot*
                                             # in case NavigatioSchool is set !='' 
                                             #process.MeasurementTrackerEvent*
                                             process.FinalTrackRefitter) 

#Global tag
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '110X_mcRun4_realistic_Candidate_2020_01_30_18_18_07', '')

process.GlobalTag.toGet = cms.VPSet(
     cms.PSet(record = cms.string("TrackerAlignmentRcd"),
              tag = cms.string("Alignments"),
              connect = cms.string('sqlite_file:/tmp/musich/phase2Checks/CMSSW_11_1_X_2020-01-30-1100/src/Alignment/OfflineValidation/test/tracker_alignment_phase2_D49110X_mcRun4_realistic_v3.db')
         ),
     cms.PSet(record = cms.string("TrackerAlignmentErrorExtendedRcd"),
              tag = cms.string("AlignmentErrorsExtended"),
              connect = cms.string('sqlite_file:/tmp/musich/phase2Checks/CMSSW_11_1_X_2020-01-30-1100/src/Alignment/OfflineValidation/test/tracker_alignment_phase2_D49110X_mcRun4_realistic_v3.db')
         ),
     cms.PSet(record = cms.string("TrackerSurfaceDeformationRcd"),
             tag = cms.string("AlignmentSurfaceDeformations"),
              connect = cms.string('sqlite_file:/tmp/musich/phase2Checks/CMSSW_11_1_X_2020-01-30-1100/src/Alignment/OfflineValidation/test/tracker_alignment_phase2_D49110X_mcRun4_realistic_v3.db')
         )
)

#process.GlobalTag.DumpStat = cms.untracked.bool(True)

isDA = True
isMC = True

#process.PixelCPEGenericESProducer.UseErrorsFromTemplates = cms.bool(False) 

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
                                  src =  cms.untracked.InputTag("generalTracks"),
                                  debugOn = cms.untracked.bool(False),
                                  numtrack = cms.untracked.uint32(10),
                                  thresh = cms.untracked.double(0.25)
                                  )


process.load("Alignment.CommonAlignment.filterOutLowPt_cfi")
process.filterOutLowPt.src = "generalTracks"
process.filterOutLowPt.ptmin = 1.5
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
                                           probePt  = cms.untracked.double(1.5),
                                           probeEta = cms.untracked.double(4.0),
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
                                   #fileName = cms.string('PrimaryVertexValidation_phase2_test1.root')
                                   #fileName = cms.string('PrimaryVertexValidation_phase2_test1NoPU.root')
                                   #fileName = cms.string('PrimaryVertexValidation_phase2_commonRefit.root')
                                   fileName  = cms.string('PrimaryVertexValidation_phase2_D49_generic.root')
                                   )



process.p = cms.Path(process.goodvertexSkim
                     *process.seqTrackselRefit
                     *process.PVValidation
                     )


print("Final process path:",process.p)

print("Done")
