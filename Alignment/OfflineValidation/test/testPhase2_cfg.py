from enum import Enum
import FWCore.ParameterSet.Config as cms

class RefitType(Enum):
     STANDARD = 1
     COMMON   = 2

from Configuration.Eras.Era_Phase2C9_cff import Phase2C9
process = cms.Process("PrimaryVertexValidation",Phase2C9)
#process = cms.Process("PrimaryVertexValidation")

#theRefitter = RefitType.STANDARD
theRefitter = RefitType.COMMON

###################################################################
# Event source and run selection
###################################################################
readFiles = cms.untracked.vstring()
readFiles.extend(['/store/relval/CMSSW_11_2_0_pre5/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-RECO/110X_mcRun4_realistic_v3_2026D49noPU-v1/20000/2D54D09A-1F7D-174F-A6B8-1D36D90417EA.root',
                  '/store/relval/CMSSW_11_2_0_pre5/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-RECO/110X_mcRun4_realistic_v3_2026D49noPU-v1/20000/6E18F6D1-ECF7-4247-8982-25E7A2C4CE23.root',
                  '/store/relval/CMSSW_11_2_0_pre5/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-RECO/110X_mcRun4_realistic_v3_2026D49noPU-v1/20000/37EBFAD1-FF1E-E34F-8B85-1520EA03572A.root',
                  '/store/relval/CMSSW_11_2_0_pre5/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-RECO/110X_mcRun4_realistic_v3_2026D49noPU-v1/20000/0D72110D-0423-A146-9FFD-9D2F0A73B729.root',
                  '/store/relval/CMSSW_11_2_0_pre5/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-RECO/110X_mcRun4_realistic_v3_2026D49noPU-v1/20000/505A878C-550F-A74B-8BCE-B18B541B8DED.root',
                  '/store/relval/CMSSW_11_2_0_pre5/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-RECO/110X_mcRun4_realistic_v3_2026D49noPU-v1/20000/F2F81439-3C2A-224E-811C-910F5EB05349.root',
                  '/store/relval/CMSSW_11_2_0_pre5/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-RECO/110X_mcRun4_realistic_v3_2026D49noPU-v1/20000/94763211-A769-E84A-8AC7-FD5E0F343CDD.root',
                  '/store/relval/CMSSW_11_2_0_pre5/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-RECO/110X_mcRun4_realistic_v3_2026D49noPU-v1/20000/7F47B723-D059-9A4A-AD99-90A9942F7C60.root',
                  '/store/relval/CMSSW_11_2_0_pre5/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-RECO/110X_mcRun4_realistic_v3_2026D49noPU-v1/20000/42BB1BF8-873F-904A-AA9A-B0851A91BA55.root',
                  '/store/relval/CMSSW_11_2_0_pre5/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-RECO/110X_mcRun4_realistic_v3_2026D49noPU-v1/20000/BB70EF0E-56A5-844B-AEFF-9CD47F601EFD.root',
                  '/store/relval/CMSSW_11_2_0_pre5/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-RECO/110X_mcRun4_realistic_v3_2026D49noPU-v1/20000/2744F65E-16B7-074A-B7FB-4EA7D195BCCF.root',
                  '/store/relval/CMSSW_11_2_0_pre5/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-RECO/110X_mcRun4_realistic_v3_2026D49noPU-v1/20000/F7B0D59E-9979-1B4A-A1CA-A335EF488DB6.root',
                  '/store/relval/CMSSW_11_2_0_pre5/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-RECO/110X_mcRun4_realistic_v3_2026D49noPU-v1/20000/4CE9EBF5-32B0-8048-AE5D-C503433CC002.root',
                  '/store/relval/CMSSW_11_2_0_pre5/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-RECO/110X_mcRun4_realistic_v3_2026D49noPU-v1/20000/24BA6BF8-46AE-504B-BA50-829E0DD4CD0A.root',
                  '/store/relval/CMSSW_11_2_0_pre5/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-RECO/110X_mcRun4_realistic_v3_2026D49noPU-v1/20000/34E8A54C-2CF0-8143-9357-7ACA76A3B9B7.root',
                  '/store/relval/CMSSW_11_2_0_pre5/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-RECO/110X_mcRun4_realistic_v3_2026D49noPU-v1/20000/3D21BD60-0158-3E4A-B1D4-B8E960E19EFB.root',
                  '/store/relval/CMSSW_11_2_0_pre5/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-RECO/110X_mcRun4_realistic_v3_2026D49noPU-v1/20000/8182BE81-FA26-3C45-AFAB-82BD07CCA246.root',
                  '/store/relval/CMSSW_11_2_0_pre5/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-RECO/110X_mcRun4_realistic_v3_2026D49noPU-v1/20000/23265A0C-12B6-2145-9E88-AD67187C8DEF.root',
                  '/store/relval/CMSSW_11_2_0_pre5/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-RECO/110X_mcRun4_realistic_v3_2026D49noPU-v1/20000/6D75DE6E-25EE-554C-9DD9-FBCC354DE3E0.root'])

process.source = cms.Source("PoolSource",
                            fileNames = readFiles ,
                            duplicateCheckMode = cms.untracked.string('checkAllFilesOpened')
                            )

process.maxEvents = cms.untracked.PSet(
     input = cms.untracked.int32(1000)
)

process.options = cms.untracked.PSet(
   wantSummary = cms.untracked.bool(False),
   Rethrow = cms.untracked.vstring("ProductNotFound"), # make this exception fatal
   fileMode  =  cms.untracked.string('NOMERGE') # no ordering needed, but calls endRun/beginRun etc. at file boundaries
)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.MessageLogger.statistics.append('cout')

process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
#process.load("Configuration.Geometry.GeometryDB_cff")
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')

process.load('Configuration.StandardSequences.Services_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")
#process.load('RecoLocalTracker.Phase2TrackerRecHits.Phase2StripCPEESProducer_cfi')

if(theRefitter == RefitType.COMMON):

     print(">>>>>>>>>> testPVValidation_cfg.py: msg%-i: using the common track selection and refit sequence!")          
     ####################################################################
     # Load and Configure Common Track Selection and refitting sequence
     ####################################################################
     import Alignment.CommonAlignment.tools.trackselectionRefitting as trackselRefit
     process.seqTrackselRefit = trackselRefit.getSequence(process, 'generalTracks',
                                                          isPVValidation=True, 
                                                          #TTRHBuilder='WithTrackAngle',
                                                          TTRHBuilder='WithAngleAndTemplate',
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
process.GlobalTag = GlobalTag(process.GlobalTag,"auto:phase2_realistic_T15")

'''
process.GlobalTag.toGet = cms.VPSet(
     cms.PSet(record = cms.string("TrackerAlignmentRcd"),
              tag = cms.string("Alignments"),
              connect = cms.string('sqlite_file:/afs/cern.ch/user/m/musich/public/phase2alignment/tracker_alignment_phase2106X_upgrade2023_realistic_v5.db')
         ),
     cms.PSet(record = cms.string("TrackerAlignmentErrorExtendedRcd"),
              tag = cms.string("AlignmentErrorsExtended"),
              connect = cms.string('sqlite_file:/afs/cern.ch/user/m/musich/public/phase2alignment/tracker_alignment_phase2106X_upgrade2023_realistic_v5.db')
         ),
     cms.PSet(record = cms.string("TrackerSurfaceDeformationRcd"),
             tag = cms.string("AlignmentSurfaceDeformations"),
             connect = cms.string('sqlite_file:/afs/cern.ch/user/m/musich/public/phase2alignment/tracker_alignment_phase2106X_upgrade2023_realistic_v5.db')
         )
)
'''
isDA = True
isMC = True

#process.PixelCPEGenericESProducer.UseErrorsFromTemplates = cms.bool(False) 
process.PixelCPEGenericESProducer.NoTemplateErrorsWhenNoTrkAngles = cms.bool(False)

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
                                   fileName  = cms.string('justAtest_Template_GenErrors.root')
)



process.p = cms.Path(process.goodvertexSkim*
                     process.seqTrackselRefit*
                     process.PVValidation)


print("Final process path:",process.p)

print("Done")
