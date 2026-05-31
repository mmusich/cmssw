import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing('analysis')

options.register('globalTag',
                 '160X_dataRun3_HLT_v1',  # adjust to your run era
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.string,
                 'Global tag')
options.parseArguments()

from Configuration.Eras.Era_Run3_2025_cff import Run3_2025
process = cms.Process('DZDEBUG',Run3_2025)

# ---- number of events -------------------------------------------------------
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

# ---- message logger (keep it quiet) -----------------------------------------
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

# ---- global tag -------------------------------------------------------------
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, options.globalTag, '')

# ---- geometry & magnetic field (needed to build reco::Track properly) -------
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')

# ---- input ------------------------------------------------------------------
#process.source = cms.Source('PoolSource',
#    fileNames = cms.untracked.vstring(options.inputFiles),
#)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'file:file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job0_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job10_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job11_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job12_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job13_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job14_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job15_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job16_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job17_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job18_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job19_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job1_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job20_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job21_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job22_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job23_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job24_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job25_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job26_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job27_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job28_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job29_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job2_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job30_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job31_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job32_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job33_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job34_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job35_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job36_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job37_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job38_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job39_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job3_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job40_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job41_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job42_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job43_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job44_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job45_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job46_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job47_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job48_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job49_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job4_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job50_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job51_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job52_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job53_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job54_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job55_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job56_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job57_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job58_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job59_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job5_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job60_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job6_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job7_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job8_Scouting.root',
        'file:/eos/cms/store/group/tsg-phase2/user/jprendi/NERD25/MoreStats/Muons/HLT//HLT_MuList_Submission_HLT_job9_Scouting.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

# ---- TFileService (output TTree goes here) ----------------------------------
process.TFileService = cms.Service('TFileService',
    fileName = cms.string(options.outputFile),
    closeFileFast = cms.untracked.bool(True)
)

# ---- the debugger module ----------------------------------------------------
process.scoutingTrackDzDebugger = cms.EDAnalyzer('ScoutingTrackDzDebugger',
    tracks        = cms.InputTag('hltScoutingTrackPacker'),
    vertices      = cms.InputTag('hltScoutingPrimaryVertexPacker', 'primaryVtx'),
    beamSpotLabel = cms.InputTag('hltOnlineBeamSpot'),
)

# ---- the beamspot module ----------------------------------------------------
from RecoVertex.BeamSpotProducer.BeamSpotOnline_cfi import onlineBeamSpotProducer as _onlineBeamSpotProducer
process.hltOnlineBeamSpot = _onlineBeamSpotProducer.clone()

# ---- path -------------------------------------------------------------------
process.p = cms.Path(process.hltOnlineBeamSpot+process.scoutingTrackDzDebugger)
process.schedule = cms.Schedule(process.p)
