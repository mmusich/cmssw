import glob
import math
import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils

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
process.GlobalTag = GlobalTag(process.GlobalTag,"112X_mcRun3_2021_realistic_v16", '')
# process.GlobalTag.toGet = cms.VPSet(cms.PSet(record = cms.string('TrackerAlignmentRcd'),
#                                             tag = cms.string("TrackerAlignment_Upgrade2017_design_v4")),
#                                    cms.PSet(record =  cms.string('TrackerSurfaceDeformationRcd'),
#                                             tag = cms.string("TrackerSurfaceDeformations_zero")),
#                                    cms.PSet(record =  cms.string('TrackerAlignmentErrorExtendedRcd'),
#                                             tag = cms.string("TrackerAlignmentErrorsExtended_Upgrade2017_design_v0")))

###################################################################
# Source
###################################################################
filelist = FileUtils.loadListFromFile("listOfFiles_idealMC.txt")
readFiles = cms.untracked.vstring( *filelist)
process.source = cms.Source("PoolSource",fileNames = readFiles)

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
                                    #tracks = cms.InputTag('TrackRefitter1'))
                                    tracks = cms.InputTag('ALCARECOTkAlZMuMu'))

from Alignment.OfflineValidation.diMuonValidation_cfi import diMuonValidation as _diMuonValidation
process.DiMuonMassValidation = _diMuonValidation.clone(
    TkTag = 'ALCARECOTkAlZMuMu',
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
                                   fileName = cms.string("ZmmNtuple_idealMC.root"))

###################################################################
# Path
###################################################################
process.p1 = cms.Path(process.offlineBeamSpot
                      #* process.TrackRefitter1
                      * process.myanalysis
                      * process.DiMuonMassValidation)
