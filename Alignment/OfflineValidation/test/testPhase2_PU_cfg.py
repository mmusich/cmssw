from enum import Enum
import FWCore.ParameterSet.Config as cms

class RefitType(Enum):
     STANDARD = 1
     COMMON   = 2

from Configuration.Eras.Era_Phase2C8_timing_layer_bar_cff import Phase2C8_timing_layer_bar
process = cms.Process("PrimaryVertexValidation",Phase2C8_timing_layer_bar)
#process = cms.Process("PrimaryVertexValidation")

#theRefitter = RefitType.STANDARD
theRefitter = RefitType.COMMON

###################################################################
# Event source and run selection
###################################################################
readFiles = cms.untracked.vstring()
# readFiles.extend(['/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/106X_upgrade2023_realistic_v2_2023D41noPU-v1/10000/86C0A7EC-51CB-EE48-9C0B-B91670154650.root',
#                   '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/106X_upgrade2023_realistic_v2_2023D41noPU-v1/10000/8B2CBEA2-F5AF-E049-9402-53DE3B6D3F1F.root',
#                   '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/106X_upgrade2023_realistic_v2_2023D41noPU-v1/10000/E83C6143-BD6E-7549-8978-1EE67A84AA16.root',
#                   '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/106X_upgrade2023_realistic_v2_2023D41noPU-v1/10000/9845F48C-8EF6-BB4C-BCED-0D1652F29746.root',
#                   '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/106X_upgrade2023_realistic_v2_2023D41noPU-v1/10000/D7D82C49-A142-7844-ABBA-40A959F62EC0.root',
#                   '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/106X_upgrade2023_realistic_v2_2023D41noPU-v1/10000/76F2841B-ABA9-974A-B072-30A5593E673A.root',
#                   '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/106X_upgrade2023_realistic_v2_2023D41noPU-v1/10000/4C3A88B5-93CE-A841-829A-EEF8ED5D4830.root',
#                   '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/106X_upgrade2023_realistic_v2_2023D41noPU-v1/10000/A6B527CA-0A02-D445-853F-D19284C56F07.root',
#                   '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/106X_upgrade2023_realistic_v2_2023D41noPU-v1/10000/95406C81-3C2F-BC4A-9022-6C463A164F25.root',
#                   '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/106X_upgrade2023_realistic_v2_2023D41noPU-v1/10000/48EE1FA4-B32A-804B-BC23-576269B04D2F.root'])


readFiles.extend(['/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/555C0759-09FE-0046-8085-D545868BF33E.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/62ACFD1E-53AA-EA40-974E-F23946D3A334.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/50F72458-F36A-5B48-9DF9-DE5CECD79A9C.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/3842BDAA-2F7C-F147-ABC7-518F24BBAE8E.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/F73AAC10-43D4-8944-AA79-62A52F09D873.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/6F229504-807B-FF43-A2C9-BA4EC96D6AFF.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/2C17A33B-ED11-2642-A51B-94726EDB653A.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/95B10E60-1620-A549-A565-B8B7D927D439.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/53F1F4B2-F997-6747-ABA2-0E978BED35CC.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/30F70274-207A-6746-B41D-6D7F56717A3D.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/F8487FC0-55FB-784F-A6F7-5C2524882BB9.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/7AA63EE0-B4CD-DB48-8E83-ACB5F796A0DE.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/3339E49A-1625-4A4D-B4E1-D98DAEFC16D3.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/D0147BE3-B976-9B46-8F99-BDAAB737BCB2.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/A794C730-E260-3A43-91A1-0153621B343E.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/59532262-BF00-1541-B1D9-4712F03D135E.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/3DF00831-4F84-E747-AA17-7B6B529B0CAA.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/76D4C367-08F6-3A46-AC29-35F881B0F2CB.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/F28DAFD7-2680-1347-B74A-28A34FA13C2A.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/7F4EBBB1-4FEF-C348-B3CB-8F11A4AB2920.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/1A7C6898-C1BE-894B-B16A-F77B6DCF9B36.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/026E2F7B-7C24-4549-9A7E-F79284F2476E.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/CF580862-D478-A04B-9F0D-2D61717D67EE.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/5B4C64CA-DBDF-0741-AAA2-ED2399960038.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/A9460131-BF74-1F4C-A72B-4919B950F1C0.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/B1617A96-168E-5345-9387-B4106FB21A35.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/71031544-6693-774E-AEF7-2182A67BCAE8.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/C2AFBBFC-78C4-9B4F-9D01-50881850E0E5.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/93B3C631-3618-FC49-85DB-7A8D56953D70.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/39C966DF-D800-1B40-8F3E-3B72F1809D4A.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/2F9574D3-230B-5D40-B7E2-02B187D2BB5D.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/CB128082-8580-5A4F-9E35-6928E9633F3A.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/8672C46C-4A54-2A4F-A49B-7D483992B601.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/5AB3B09D-1C52-E347-99D3-89ED655F5461.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/21964C59-4F51-D547-9954-FBB1039BDE45.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/CD944D0D-FC94-0144-8DDF-45010AA548DE.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/A325D5A8-26DC-7B44-91E4-40A3830E99AD.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/DAEE95FC-9A88-9744-AB72-F30CB0C49883.root',
                  '/store/relval/CMSSW_10_6_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/10000/D9E2D9DB-9F71-A841-8546-0CFCE8DA0246.root'])

process.source = cms.Source("PoolSource",
                            fileNames = readFiles ,
                            duplicateCheckMode = cms.untracked.string('checkAllFilesOpened')
                            )

process.maxEvents = cms.untracked.PSet(
     input = cms.untracked.int32(1000)
)
#process.source.skipEvents=cms.untracked.uint32(0*250000/40)

process.options = cms.untracked.PSet(
   wantSummary = cms.untracked.bool(False),
   Rethrow = cms.untracked.vstring("ProductNotFound"), # make this exception fatal
   fileMode  =  cms.untracked.string('NOMERGE') # no ordering needed, but calls endRun/beginRun etc. at file boundaries
)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 10
process.MessageLogger.statistics.append('cout')


process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
#process.load("Configuration.Geometry.GeometryDB_cff")
process.load('Configuration.Geometry.GeometryExtended2023D41Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2023D41_cff')

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
process.GlobalTag = GlobalTag(process.GlobalTag,"auto:phase2_realistic")
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
        ),
     cms.PSet(record = cms.string("SiPixelLorentzAngleRcd"),
              tag = cms.string("SiPixelLorentzAngle_phase2_test"),
              connect = cms.string('sqlite_file:/afs/cern.ch/work/t/tsusacms/public/testIBC/CMSSW_11_0_0_pre2/src/DPGAnalysis-SiPixelTools/PixelDBTools/phase2/SiPixelLorentzAngle_phase2_test.db')
         ),
)

isDA = True
isMC = True

process.PixelCPEGenericESProducer.UseErrorsFromTemplates = cms.bool(False) 

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
                                   fileName  = cms.string('justAtestPU.root')
                                   )



process.p = cms.Path(process.goodvertexSkim*
                     process.seqTrackselRefit*
                     process.PVValidation)


print("Final process path:",process.p)

print("Done")
