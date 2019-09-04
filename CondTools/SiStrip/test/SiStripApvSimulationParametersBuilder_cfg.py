import FWCore.ParameterSet.Config as cms
process = cms.Process("ProcessOne")

##
## MessageLogger
##
process.load('FWCore.MessageService.MessageLogger_cfi')   
process.MessageLogger.categories.append("SiStripApvSimulationParametersBuilder")  
process.MessageLogger.categories.append("SiStripApvSimulationParameters")  
process.MessageLogger.destinations = cms.untracked.vstring("cout")
process.MessageLogger.cout = cms.untracked.PSet(
    threshold = cms.untracked.string("INFO"),
    default   = cms.untracked.PSet(limit = cms.untracked.int32(0)),                       
    FwkReport = cms.untracked.PSet(limit = cms.untracked.int32(-1),
                                   reportEvery = cms.untracked.int32(1000)
                                   ),                                                      
    SiStripApvSimulationParametersBuilder = cms.untracked.PSet( limit = cms.untracked.int32(-1)),
    SiStripApvSimulationParameters        = cms.untracked.PSet( limit = cms.untracked.int32(-1))
    )
process.MessageLogger.statistics.append('cout')  

##
## Empty source
##
process.source = cms.Source("EmptySource",
                            firstRun = cms.untracked.uint32(1),
                            numberEventsInRun    = cms.untracked.uint32(1),
                            firstLuminosityBlock = cms.untracked.uint32(1),
                            numberEventsInLuminosityBlock = cms.untracked.uint32(1),
                            )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1))

##
## Database output service
##
process.load("CondCore.CondDB.CondDB_cfi")

##
## Output database (in this case local sqlite file)
##
process.CondDB.connect = 'sqlite_file:SiStripApvSimulationParameters.db'
process.PoolDBOutputService = cms.Service("PoolDBOutputService",
                                          process.CondDB,
                                          timetype = cms.untracked.string('runnumber'),
                                          toPut = cms.VPSet(cms.PSet(record = cms.string('SiStripApvSimulationParametersRcd'),
                                                                     tag = cms.string('SiStripApvSimulationParameter_v0_mc')
                                                                     )
                                                            )
                                          )


process.WriteInDB = cms.EDAnalyzer("SiStripApvSimulationParametersBuilder",
                                   apvBaselines_nBinsPerBaseline=cms.uint32(82),
                                   apvBaselines_minBaseline=cms.double(0.),
                                   apvBaselines_maxBaseline=cms.double(738.),
                                   apvBaselines_puBinEdges=cms.vdouble(0.,  2.,  4.,  6.,  8., 10., 12., 14., 16., 18., 20., 22., 24., 26., 28., 30., 32., 34., 36., 38., 40., 42., 44., 46., 48., 50.),
                                   apvBaselines_zBinEdges=cms.vdouble(0., 25., 50., 75.),
                                   apvBaselinesFile_tib1=cms.FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TIB1_12us.txt"),
                                   apvBaselinesFile_tib2=cms.FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TIB2_15us.txt"),
                                   apvBaselinesFile_tib3=cms.FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TIB3_16us.txt"),
                                   apvBaselinesFile_tib4=cms.FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TIB4_17us.txt"),
                                   apvBaselinesFile_tob1=cms.FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TOB1_10us.txt"),
                                   apvBaselinesFile_tob2=cms.FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TOB2_13us.txt"),
                                   apvBaselinesFile_tob3=cms.FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TOB3_16us.txt"),
                                   apvBaselinesFile_tob4=cms.FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TOB4_17us.txt"),
                                   apvBaselinesFile_tob5=cms.FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TOB5_17us.txt"),
                                   apvBaselinesFile_tob6=cms.FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TOB6_18us.txt")
                                   )

process.p = cms.Path(process.WriteInDB)
