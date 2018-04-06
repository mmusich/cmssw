import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1) 
    )

process.source = cms.Source("EmptyIOVSource",
                            #firstValue = cms.uint64(313280),
                            #lastValue = cms.uint64(313280),
                            #firstValue = cms.uint64(1),
                            #lastValue = cms.uint64(1),   
                            firstValue = cms.uint64(306054),  
                            lastValue = cms.uint64(306054),   
                            timetype = cms.string('runnumber'),
                            interval = cms.uint64(1)
                            )

process.load('Configuration.StandardSequences.GeometryRecoDB_cff') 
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = '100X_dataRun2_Express_v3'
process.GlobalTag.toGet = cms.VPSet(
    cms.PSet(
        record  = cms.string("SiStripNoisesRcd"),
        #tag     = cms.string("SiStripNoise_test"),
        #connect = cms.string("sqlite_file:/afs/cern.ch/user/m/musich/2018DataAnalysis/CMSSW_10_1_X_2018-03-29-2300/src/CondTools/SiStrip/test/dbfile.db")
        tag     = cms.string("modifiedNoise"),
        connect = cms.string("sqlite_file:/afs/cern.ch/user/m/musich/2018DataAnalysis/CMSSW_10_1_X_2018-03-29-2300/src/CondTools/SiStrip/test/modifiedNoise_100X_dataRun2_Express_v2_IOV_306054.db")
        )
    )

process.TFileService = cms.Service(
    "TFileService",
    #fileName = cms.string("noiseDump_mods.root")
    fileName = cms.string("noiseDump.root")
    )

process.demo = cms.EDAnalyzer('SiStripNoiseVisualizer')
process.p = cms.Path(process.demo)
