from __future__ import print_function
import FWCore.ParameterSet.Config as cms

process = cms.Process("TBDtest")

# Messages
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000

process.load("Alignment.CommonAlignmentProducer.AlignmentTrackSelector_cfi")
process.load("RecoTracker.FinalTrackSelectors.TrackerTrackHitFilter_cff")
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
process.load("RecoTracker.Configuration.RecoTracker_cff")
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.Services_cff")
process.load('Configuration.Geometry.GeometryRecoDB_cff')
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

#Tracker
from RecoTracker.GeometryESProducer.TrackerRecoGeometryESProducer_cfi import *

#Muon
from Geometry.MuonNumbering.muonNumberingInitialization_cfi import *
from RecoMuon.DetLayers.muonDetLayerGeometry_cfi import *

#  Alignment
from Geometry.TrackerGeometryBuilder.idealForDigiTrackerGeometry_cff import *
from Geometry.CSCGeometryBuilder.idealForDigiCscGeometry_cff import *
from Geometry.DTGeometryBuilder.idealForDigiDtGeometry_cff import *

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, "140X_dataRun3_Prompt_v4", '')

########### DATA FILES  ####################################
import FWCore.PythonUtilities.LumiList as LumiList
## Some example files to test ##
lumiSecs = cms.untracked.VLuminosityBlockRange()
#goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/DCSOnly/json_DCSONLY.txt').getCMSSWString().split(',')
#lumiSecs.extend(goodLumiSecs)
readFiles = cms.untracked.vstring()
readFiles.extend(['/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/213/00000/5338abbf-0a9d-4532-8238-2e2f65cc728b.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/216/00000/b1e496db-1aad-4e27-bcd8-cc4a4c95df05.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/229/00000/6ec97061-5aff-4174-b28c-6a04f1047bc2.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/251/00000/c0ab7733-868a-4ec7-bdc1-36ca020bfb84.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/255/00000/e1e5e6af-08ef-412f-a15a-6769e2378c5b.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/261/00000/d096947d-bd23-4e8f-97be-a18cc8d58bd4.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/259/00000/2fb5ef80-366b-4736-ada4-2158c3252a32.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/256/00000/ff97cd81-e229-453e-afb7-8835900b448b.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/260/00000/14b67abf-4548-4910-87d9-4556830f13fa.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/250/00000/686b2329-73b1-4f2e-8474-ae3af7bd9e1f.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/257/00000/9551bc59-68d9-4f9f-a90b-6e6d51e00f6b.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/258/00000/a2670bcb-deb2-4ced-9588-8ab57638c2b4.root', 
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/298/00000/beac4912-b420-4aac-9238-1ef73b0bdd93.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/258/00000/54a0f35f-7147-4edd-9d99-ca518602b8f8.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/262/00000/454f797d-59bc-488c-a076-373c2a66ced3.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/300/00000/d823455e-992f-4f5d-bbe2-d0625f6e4cc6.root', 
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/299/00000/98d4f22f-de11-4a28-9c65-1fc434c0d1fb.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/328/00000/8aaf5fb0-7dc3-4339-9fb2-192f179e65f8.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/343/00000/745db319-637a-486b-a5d2-ed44083065c0.root', 
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/329/00000/34bedb44-4673-49ac-8683-a7677d789197.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/381/00000/3e3df096-4807-46e2-a02d-17359ef4d146.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/393/00000/61a40d14-55d2-4933-97f5-b883d4924154.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/392/00000/40ea22f5-c189-46fb-818d-2005bba5b3cb.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/313/00000/9c8d35a7-f90b-4dbc-a211-1903ce1a455c.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/344/00000/69cc3004-c552-4139-ac0e-d5ed1b0910ea.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/313/00000/0c72fa6e-52a5-4855-84cd-496ae48e90e5.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/314/00000/760b4b9e-c0cf-4ce7-8613-c65a2a8371cd.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/329/00000/6d4d5e62-b974-452b-9f9b-5c8914a836a5.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/314/00000/880c31db-60f4-42d1-ae1a-49484de372b0.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/343/00000/43910df8-1d73-4b5e-b841-f6775540481a.root',
                  '/store/data/Run2024F/Muon0/ALCARECO/TkAlZMuMu-PromptReco-v1/000/382/434/00000/539cc2df-79ac-4977-888e-878a2900fb8c.root']
)
process.source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles
                    )
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(15500))
#process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
#process.source.skipEvents=cms.untracked.uint32(0*-1/1)
process.options = cms.untracked.PSet()

strflag="ZMuMu"
strflaglower=strflag.lower()
#strflagopts="TBDconstraint:momconstr"
strflagopts="TBDconstraint:fullconstr"
#strflagopts="NOOPTS"

from Alignment.HIPAlignmentAlgorithm.OptionParser.HipPyOptionParser import HipPyOptionParser
from Alignment.HIPAlignmentAlgorithm.OptionParser.HipPyOptionParser import matchPSetsByRecord
from Alignment.HIPAlignmentAlgorithm.OptionParser.HipPyOptionParser import mergeVPSets
optpy=HipPyOptionParser(strflag,strflagopts)

# Track collection name is now interpreted from the flag and may be replaced if an option is specified
# optpy.trkcoll is guaranteed to exist, else python should have already given an error.
strtrackcollname=optpy.trkcoll

# Replace GT specifics if a custom option is specified
if hasattr(optpy, "GlobalTag"):
   process.GlobalTag.globaltag = optpy.GlobalTag
if hasattr(optpy, "GTtoGet"):
   process.GlobalTag.toGet = mergeVPSets(process.GlobalTag.toGet, optpy.GTtoGet, matchPSetsByRecord)

###############################################################################
# Setup common options
strTTRHBuilder = "WithAngleAndTemplate"
if "generic" in optpy.CPEtype: # CPE type is defaulted to "template" in HipPyOptionParser
  strTTRHBuilder = "WithTrackAngle"
###############################################################################

import Alignment.CommonAlignment.tools.trackselectionRefitting as TrackRefitterSequencer

strTBDConstrainer=None
if hasattr(optpy, "TBDconstraint"):
   strtbdconstr=optpy.TBDconstraint
   if "momconstr" in strtbdconstr:
      process.load("RecoTracker.TrackProducer.TwoBodyDecayMomConstraintProducer_cff")
      process.TwoBodyDecayMomConstraint.src = "AlignmentTrackSelector"
      process.TwoBodyDecayMomConstraint.primaryMass = cms.double(91.1876)
      process.TwoBodyDecayMomConstraint.primaryWidth = cms.double(1.4)
      #process.TwoBodyDecayMomConstraint.primaryWidth = cms.double(2.4952)
      #process.TwoBodyDecayMomConstraint.sigmaPositionCut = cms.double(0.07)
      process.TwoBodyDecayMomConstraint.rescaleError = cms.double(1.0)
      process.TwoBodyDecayMomConstraint.chi2Cut = cms.double(99999.)
      #process.TwoBodyDecayMomConstraint.EstimatorParameters.RobustificationConstant = cms.double(1.0)
      strTBDConstrainer="TwoBodyDecayMomConstraint,momentum"

   elif "fullconstr" in strtbdconstr:
      process.load("RecoTracker.TrackProducer.TwoBodyDecayConstraintProducer_cff")
      process.TwoBodyDecayConstraint.src = "AlignmentTrackSelector"
      process.TwoBodyDecayConstraint.primaryMass = cms.double(91.1876)
      process.TwoBodyDecayConstraint.primaryWidth = cms.double(1.4)
      #process.TwoBodyDecayConstraint.primaryWidth = cms.double(2.4952)
      process.TwoBodyDecayConstraint.sigmaPositionCut = cms.double(0.5)
      process.TwoBodyDecayConstraint.rescaleError = cms.double(1.0)
      process.TwoBodyDecayConstraint.chi2Cut = cms.double(99999.)
      #process.TwoBodyDecayConstraint.EstimatorParameters.RobustificationConstant = cms.double(1.0)
      strTBDConstrainer="TwoBodyDecayConstraint,trackParameters"

if strTBDConstrainer is not None:
   print("strTBDConstrainer=",strTBDConstrainer)

process.TrackRefitterSequence = TrackRefitterSequencer.getSequence(
   process,
   strtrackcollname,
   TTRHBuilder = strTTRHBuilder,
   usePixelQualityFlag = None, # Keep default behavior ("WithAngleAndTemplate" -> True, "WithTrackAngle" -> False)
   openMassWindow = False,
   cosmicsDecoMode = False,
   cosmicsZeroTesla = False,
   #momentumConstraint = None, # Should be a momentum constraint object name or None
   momentumConstraint = strTBDConstrainer, # Should be a momentum constraint object name or None
   cosmicTrackSplitting = False,
   use_d0cut = True
   )

# Override TrackRefitterSequencer defaults
process.HighPurityTrackSelector.pMin   = 0.0
process.AlignmentTrackSelector.pMin    = 0.0
process.AlignmentTrackSelector.ptMin   = 15.0
process.AlignmentTrackSelector.etaMin  = -3.0
process.AlignmentTrackSelector.etaMax  = 3.0
process.AlignmentTrackSelector.nHitMin  = 15
process.AlignmentTrackSelector.minHitsPerSubDet.inPIXEL = cms.int32(1)
process.AlignmentTrackSelector.TwoBodyDecaySelector.daughterMass = 0.105658
process.AlignmentTrackSelector.TwoBodyDecaySelector.minXMass = 80.0
process.AlignmentTrackSelector.TwoBodyDecaySelector.maxXMass = 100.0


print(process.TrackRefitterSequence)
subproc=[
   "offlineBeamSpot",
   "HighPurityTrackSelector",
   "FirstTrackRefitter",
   "TrackerTrackHitFilter",
   "HitFilteredTracksTrackFitter",
   "AlignmentTrackSelector",
   "TwoBodyDecayConstraint",
   "TwoBodyDecayMomConstraint",
   "FinalTrackRefitter"
   ]
moduleSum=None
for sp in subproc:
   if hasattr(process, sp):
      print("\n\tAttributes for process.{}".format(sp))
      if moduleSum is None:
         moduleSum=getattr(process,sp)
      else:
         moduleSum+=getattr(process,sp)
      for v in vars(getattr(process,sp)):
         print(v,":",getattr(getattr(process,sp),v))

process.TrackRefitterSequence = cms.Sequence(moduleSum)
print("Final process path:",process.TrackRefitterSequence)
process.p = cms.Path(process.TrackRefitterSequence)


TAG = strflag
if strflagopts:
   TAG = TAG + "_" + strflagopts
TAG = TAG.replace(':','_')
TAG = TAG.strip()
print("Output file:","analyzed_{0}.root".format(TAG))
process.Analyzer = cms.EDAnalyzer("TwoBodyDecayAnalyzer",
                                  alcarecotracks = cms.InputTag(strtrackcollname),
                                  refit1tracks = cms.InputTag("FirstTrackRefitter"),
                                  refit2tracks = cms.InputTag("HitFilteredTracksTrackFitter"),
                                  finaltracks = cms.InputTag("FinalTrackRefitter")
                                  )

process.options = cms.untracked.PSet()
process.TFileService = cms.Service('TFileService',
   fileName=cms.string("analyzed_{0}.root".format(TAG))
)
process.outpath = cms.EndPath(process.Analyzer)
