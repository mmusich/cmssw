import FWCore.ParameterSet.Config as cms
process = cms.Process("ProcessOne")

##
## MessageLogger
##
process.load('FWCore.MessageService.MessageLogger_cfi')   
process.MessageLogger.categories.append("SiPixelQualityHistoricAnalyzer")  
process.MessageLogger.categories.append("SiPixelFEDChannelContainer")  
process.MessageLogger.destinations = cms.untracked.vstring("cout")
process.MessageLogger.cout = cms.untracked.PSet(
    threshold = cms.untracked.string("INFO"),
    default   = cms.untracked.PSet(limit = cms.untracked.int32(0)),                       
    FwkReport = cms.untracked.PSet(limit = cms.untracked.int32(-1),
                                   reportEvery = cms.untracked.int32(1000)
                                   ),                                                      
    SiPixelQualityHistoricAnalyzer = cms.untracked.PSet( limit = cms.untracked.int32(-1)),
    SiPixelFEDChannelContainer           = cms.untracked.PSet( limit = cms.untracked.int32(-1))
    )
process.MessageLogger.statistics.append('cout')  

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag,"106X_mc2017_realistic_v6")
process.GlobalTag.toGet = cms.VPSet(
    cms.PSet(record = cms.string("SiPixelQualityFromDbRcd"),
             tag = cms.string("SiPixelQualityFromDbRcd_prompt_Ultralegacy2017_v0_mc"),
             connect = cms.string('frontier://FrontierPrep/CMS_CONDITIONS')
         ),
    cms.PSet(record = cms.string("SiPixelStatusScenarioProbabilityRcd"),
             tag = cms.string("SiPixelQualityProbabilities_UltraLegacy2017_v1_mc"),
             connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS')
         )
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('SiPixelBadFEDChannelSimulationAnalysis.root')
                                   )

##
## Empty source
##
process.source = cms.Source("EmptySource",
                            #firstRun = cms.untracked.uint32(295316),
                            firstRun = cms.untracked.uint32(297050),
                            numberEventsInRun    = cms.untracked.uint32(2500),
                            firstLuminosityBlock = cms.untracked.uint32(1),
                            numberEventsInLuminosityBlock = cms.untracked.uint32(1),
                            )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(25000000))
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000))

process.analyzeDB = cms.EDAnalyzer("SiPixelQualityHistoricAnalyzer")

process.p = cms.Path(process.analyzeDB)
