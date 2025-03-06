import FWCore.ParameterSet.Config as cms

process = cms.Process("TrackingRecHitErrorAnalyzer")

# Load standard sequences and configuration
process.load("Configuration.StandardSequences.Services_cff")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.EndOfProcess_cff")

# Global tag
process.GlobalTag.globaltag = 'auto:run2_mc'

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/relval/CMSSW_10_6_0_pre2/RelValTTbar_13/GEN-SIM-RECO/PU25ns_106X_mcRun2_asymptotic_v3-v1/10000/011A8DA6-3C55-BC4C-A014-0A1AC5DD1A7C.root'
    )
)

# Max events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Analyzer
process.trackingRecHitErrorAnalyzer = cms.EDAnalyzer('TrackingRecHitErrorAnalyzer',
    trackCollection = cms.InputTag('generalTracks')
                                                     )

# Path and EndPath definitions
process.analysis_step = cms.Path(process.trackingRecHitErrorAnalyzer)
process.endjob_step = cms.EndPath(process.endOfProcess)

# Schedule definition
process.schedule = cms.Schedule(process.analysis_step, process.endjob_step)

# MessageLogger
process.MessageLogger.cerr.FwkReport.reportEvery = 100
