import glob
import math
import FWCore.ParameterSet.Config as cms

process = cms.Process("AlCaRECOAnalysis")

###################################################################
# Set the process to run multi-threaded
###################################################################
process.options.numberOfThreads = 8

###################################################################
# Message logger service
###################################################################
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.enable = False
process.MessageLogger.ZtoMMNtupler=dict()  
process.MessageLogger.cout = cms.untracked.PSet(
    enable = cms.untracked.bool(True),
    threshold = cms.untracked.string("INFO"),
    default   = cms.untracked.PSet(limit = cms.untracked.int32(0)),                       
    FwkReport = cms.untracked.PSet(limit = cms.untracked.int32(-1),
                                   reportEvery = cms.untracked.int32(1000)
                                   ),                                                      
    ZtoMMNtupler = cms.untracked.PSet( limit = cms.untracked.int32(-1)),
    enableStatistics = cms.untracked.bool(True)
    )

###################################################################
# Geometry producer and standard includes
###################################################################
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
process.load("Configuration.StandardSequences.Services_cff")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load("CondCore.CondDB.CondDB_cfi")

####################################################################
# Get the GlogalTag
####################################################################
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag,"130X_dataRun3_Prompt_v2", '')
process.GlobalTag.toGet = cms.VPSet(cms.PSet(
    record = cms.string('TrackerAlignmentRcd'),
    tag = cms.string("Alignments"),
    #connect = cms.string('sqlite_file:/tmp/musich/CMSSW_13_1_X_2023-04-17-2300/src/Alignment/TrackerAlignment/test/outputfile.db')))
    #connect = cms.string('sqlite_file:/tmp/musich/CMSSW_13_1_X_2023-04-17-2300/src/Alignment/TrackerAlignment/test/outputfile_layerRot.db')))
    #connect = cms.string('sqlite_file:/tmp/musich/CMSSW_13_1_X_2023-04-17-2300/src/Alignment/TrackerAlignment/test/outputfile_twist.db')))
    #connect = cms.string('sqlite_file:/tmp/musich/CMSSW_13_1_X_2023-04-17-2300/src/Alignment/TrackerAlignment/test/outputfile_sagitta.db')))
    connect = cms.string('sqlite_file:/tmp/musich/CMSSW_13_1_X_2023-04-17-2300/src/Alignment/TrackerAlignment/test/TrackerAlignment_PCL_byRun_v2_express.db')))    

###################################################################
# Source
###################################################################
readFiles = cms.untracked.vstring()
process.source = cms.Source("PoolSource",fileNames = readFiles)
readFiles.extend([
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/362/00000/d6641b44-f4e4-4054-b5b0-f038e567c61e.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/433/00000/1f93221e-23ce-4731-906a-48c9fe405515.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/438/00000/5812613b-751a-42e6-b030-4f85747c58da.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/435/00000/df6e27d1-5367-4192-83ed-2be9303d7837.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/503/00000/10d1e4d2-3675-422d-94f2-9feb049ca754.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/437/00000/ea6b065d-1912-491e-9cce-732eaf6fa038.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/437/00000/7ce5bac8-0b29-40f3-a63b-fd0813d5678d.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/613/00000/5f7649f0-b8db-43cf-aefb-39c79f7c8b07.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/439/00000/13e86424-5658-4398-b48c-1cb9c3789b4d.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/439/00000/82e85ac6-b5c8-434a-a756-8ea9252dfc96.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/439/00000/a83b5f31-7784-46ae-9fcf-2b4e56f476c8.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/452/00000/744e93d3-9671-45dc-807a-37c29a470617.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/457/00000/a3e82144-0529-4dda-a884-a874578bbe75.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/459/00000/b79052f0-9bbc-4f8c-b16a-3111baa5a46b.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/596/00000/32e53389-c938-4248-8ee4-bb0a809b5ccd.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/616/00000/69b1d192-4042-4fcf-9f3b-30ee66213a46.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/617/00000/fa190ab2-126d-45e7-a182-97956436dc04.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/673/00000/ae1a453c-4ef5-4a68-a6ce-2066aea9870d.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/618/00000/a1d1fbb8-c759-448e-b3a2-1794ea13adb5.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/439/00000/3fa232e6-a6b3-40ec-91ff-8a7452ce8f75.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/597/00000/7617bc16-1956-4aa3-b6e2-3efc8f350174.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/654/00000/ba7aa4ec-5fbb-452c-a3c7-4fc5265e6dff.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/695/00000/590026f0-525e-4f30-a85e-32c6a3139183.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/615/00000/276bb1d9-32ce-4d1d-a5c8-ac695029abd5.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/614/00000/d89e6bb1-7029-4d6a-bb2e-49439271e553.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/622/00000/f5c84943-d409-4f5f-8507-dfa301dcde58.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/726/00000/ffd48ba0-7467-4ead-a982-38373a6e8625.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/696/00000/416f30df-6679-4d64-9ca9-9a76fbd895d0.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/653/00000/d62587f8-1fc6-477e-b013-a6027907cc67.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/720/00000/a243f207-8fbe-46a3-8556-9694c56ab155.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/720/00000/e76f304c-e978-478a-813d-494ce1174d8a.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/727/00000/9de95d39-eadd-40a2-a7f6-ecc098e07b5e.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/653/00000/eda5169c-15b4-48ec-97f4-d54886a26446.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/757/00000/5a6c734f-badd-431d-81bf-36a463cac0b0.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/760/00000/265e98cc-6552-4101-8585-be229ea7e848.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/657/00000/f7e6da76-2b20-41c0-952f-9986dfa47c22.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/653/00000/f0013a71-ae57-4101-b75e-0661c09058c9.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/655/00000/263713f0-fbd9-4a7d-83ea-30d80240b70f.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/760/00000/9ab8ae7b-9318-48be-afab-b64c3bd23e27.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/696/00000/74910078-ad7c-416b-9209-f349bf877510.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/696/00000/e4da78cc-12e8-44ab-9c55-7fdb328a0336.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/758/00000/f723bd8f-2102-4606-ae20-ef56ffb46c0c.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/698/00000/420b8e8f-a521-4023-9ef4-010ee4befa2b.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/696/00000/03208ea5-d512-47b4-bae6-00db746d936e.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/728/00000/e9e0e12f-cdb7-45aa-a2b3-18138d4d7044.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/720/00000/3176145f-e51b-4b02-abc3-a84242c8a5c8.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/720/00000/fa138d74-22e2-428d-9acf-00f8282fd242.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/759/00000/3bfccdb4-26ae-4316-b281-30365ab85ec6.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/695/00000/e6d27cbf-d198-4bd8-9f70-799e6ca80c8f.root',
    '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/696/00000/2585968f-8523-4a8d-a269-bbd186d14bb0.root'])

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

###################################################################
# Alignment Track Selector
###################################################################
import Alignment.CommonAlignmentProducer.AlignmentTrackSelector_cfi
process.MuSkimSelector = Alignment.CommonAlignmentProducer.AlignmentTrackSelector_cfi.AlignmentTrackSelector.clone(
    applyBasicCuts = True,                                                                            
    filter = True,
    src = "ALCARECOTkAlZMuMu",
    ptMin = 17.,
    pMin = 17.,
    etaMin = -2.5,
    etaMax = 2.5,
    d0Min = -2.,
    d0Max = 2.,
    dzMin = -25.,
    dzMax = 25.,
    nHitMin = 6,
    nHitMin2D = 0)

###################################################################
# The TrackRefitter
###################################################################
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
import RecoTracker.TrackProducer.TrackRefitters_cff
process.TrackRefitter1 = RecoTracker.TrackProducer.TrackRefitter_cfi.TrackRefitter.clone(
    src = "ALCARECOTkAlZMuMu",
    TrajectoryInEvent = True,
    TTRHBuilder = "WithAngleAndTemplate",
    NavigationSchool = "")

###################################################################
# The analysis module
###################################################################
process.myanalysis = cms.EDAnalyzer("ZtoMMNtupler",
                                    tracks = cms.InputTag('TrackRefitter1'))
                                    #tracks = cms.InputTag('ALCARECOTkAlZMuMu'))

from Alignment.OfflineValidation.diMuonValidation_cfi import diMuonValidation as _diMuonValidation
process.DiMuonMassValidation = _diMuonValidation.clone(
    #TkTag = 'ALCARECOTkAlZMuMu',
    TkTag = 'TrackRefitter1',
    # mu mu mass
    Pair_mass_min   = 80.,
    Pair_mass_max   = 120.,
    Pair_mass_nbins = 80,
    Pair_etaminpos  = -1,
    Pair_etamaxpos  = 1,
    Pair_etaminneg  = -1,
    Pair_etamaxneg  = 1,
    # cosTheta CS
    Variable_CosThetaCS_xmin  = -1.,
    Variable_CosThetaCS_xmax  =  1.,
    Variable_CosThetaCS_nbins = 20,
    # DeltaEta
    Variable_DeltaEta_xmin  = -4.8,
    Variable_DeltaEta_xmax  = 4.8,
    Variable_DeltaEta_nbins = 20,
    # EtaMinus
    Variable_EtaMinus_xmin  = -2.4,
    Variable_EtaMinus_xmax  =  2.4,
    Variable_EtaMinus_nbins = 12,
    # EtaPlus
    Variable_EtaPlus_xmin  = -2.4,
    Variable_EtaPlus_xmax  =  2.4,
    Variable_EtaPlus_nbins = 12,
    # Phi CS
    Variable_PhiCS_xmin  = -math.pi/2.,
    Variable_PhiCS_xmax  =  math.pi/2.,
    Variable_PhiCS_nbins = 20,
    # Phi Minus
    Variable_PhiMinus_xmin  = -math.pi,
    Variable_PhiMinus_xmax  =  math.pi,
    Variable_PhiMinus_nbins = 16,
    # Phi Plus
    Variable_PhiPlus_xmin  = -math.pi,
    Variable_PhiPlus_xmax  =  math.pi,
    Variable_PhiPlus_nbins = 16,
    # mu mu pT
    Variable_PairPt_xmin  = 0.,
    Variable_PairPt_xmax  = 100.,
    Variable_PairPt_nbins = 100)

###################################################################
# Output name
###################################################################
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("ZmmNtuple_2022G_1IoV.root"))

###################################################################
# Path
###################################################################
process.p1 = cms.Path(process.offlineBeamSpot
                      * process.TrackRefitter1
                      * process.myanalysis
                      * process.DiMuonMassValidation)
