import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

# Load standard sequences
process.load("FWCore.MessageService.MessageLogger_cfi")

# Random number generator service
process.load("IOMC.RandomEngine.IOMC_cff")

process.maxEvents = cms.untracked.PSet(
    input=cms.untracked.int32(1000)
)

process.source = cms.Source("EmptySource",
                            numberEventsInRun = cms.untracked.uint32(1000),
                            firstRun = cms.untracked.uint32(380649),
                            firstLuminosityBlock = cms.untracked.uint32(522)
                            )
## create the errors
process.hltSiPixelDigiErrorsSerialSync = cms.EDProducer(
    "RandomSiPixelErrorProducer",
    numErrors=cms.uint32(1000)  # Number of errors to generate
)

process.hltSiPixelDigiErrors = cms.EDProducer(
    "RandomSiPixelErrorProducer",
    numErrors=cms.uint32(1000)  # Number of errors to generate
)

## now the DAQ part
process.FastMonitoringService = cms.Service( "FastMonitoringService",
    tbbMonitoringMode = cms.untracked.bool( True ),
    tbbConcurrencyTracker = cms.untracked.bool( True ),
    sleepTime = cms.untracked.int32( 1 ),
    fastMonIntervals = cms.untracked.uint32( 2 ),
    filePerFwkStream = cms.untracked.bool( False ),
    verbose = cms.untracked.bool( False )
)

process.EvFDaqDirector = cms.Service( "EvFDaqDirector",
    baseDir = cms.untracked.string( "." ),
    buBaseDir = cms.untracked.string( "." ),
    buBaseDirsAll = cms.untracked.vstring(  ),
    buBaseDirsNumStreams = cms.untracked.vint32(  ),
    runNumber = cms.untracked.uint32( 380649 ),
    useFileBroker = cms.untracked.bool( False ),
    fileBrokerHostFromCfg = cms.untracked.bool( True ),
    fileBrokerHost = cms.untracked.string( "InValid" ),
    fileBrokerPort = cms.untracked.string( "8080" ),
    fileBrokerKeepAlive = cms.untracked.bool( True ),
    fileBrokerUseLocalLock = cms.untracked.bool( True ),
    fuLockPollInterval = cms.untracked.uint32( 2000 ),
    outputAdler32Recheck = cms.untracked.bool( False ),
    directorIsBU = cms.untracked.bool( False ),
    hltSourceDirectory = cms.untracked.string( "" ),
    mergingPset = cms.untracked.string( "" )
)

process.hltPSetMap = cms.EDProducer( "ParameterSetBlobProducer" )

# process.hltOutputDQMGPUvsCPU = cms.OutputModule( "GlobalEvFOutputModule",
#                                                  use_compression = cms.untracked.bool( True ),
#                                                  compression_algorithm = cms.untracked.string( "ZSTD" ),
#                                                  compression_level = cms.untracked.int32( 3 ),
#                                                  lumiSection_interval = cms.untracked.int32( 0 ),
#                                                  SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'Dataset_DQMGPUvsCPU' ) ),
#                                                  outputCommands = cms.untracked.vstring( 'drop *',
#                                                                                          'keep *_hltEcalDigisCPUSerial_*_*',
#                                                                                          'keep *_hltEcalDigis_*_*',
#                                                                                          'keep *_hltEcalUncalibRecHitCPUSerial_*_*',
#                                                                                          'keep *_hltEcalUncalibRecHit_*_*',
#                                                                                          'keep *_hltHbherecoFromGPU_*_*',
#                                                                                          'keep *_hltHbherecoLegacy_*_*',
#                                                                                          'keep *_hltParticleFlowClusterHBHESoACPUSerial_*_*',
#                                                                                          'keep *_hltParticleFlowClusterHBHESoA_*_*',
#                                                                                          'keep SiPixelRawDataErroredmDetSetVector_hltSiPixelDigisFromSoA_*_*',
#                                                                                          'keep SiPixelRawDataErroredmDetSetVector_hltSiPixelDigisLegacy_*_*' ),
#                                                  psetMap = cms.untracked.InputTag( "hltPSetMap" )
#                                                 )

process.hltOutputDQMGPUvsCPU = cms.OutputModule( "GlobalEvFOutputModule",
                                                 use_compression = cms.untracked.bool( True ),
                                                 compression_algorithm = cms.untracked.string( "ZSTD" ),
                                                 compression_level = cms.untracked.int32( 3 ),
                                                 lumiSection_interval = cms.untracked.int32( 0 ),
                                                 SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( '*' ) ),
                                                 outputCommands = cms.untracked.vstring( "drop *",
                                                                                         "keep *_*_*_TEST"),    
                                                 psetMap = cms.untracked.InputTag( "hltPSetMap" )
                                                )


process.Dataset_DQMGPUvsCPU = cms.Path(process.hltSiPixelDigiErrorsSerialSync + process.hltSiPixelDigiErrors  + process.hltPSetMap)
process.DQMGPUvsCPUOutput = cms.FinalPath( process.hltOutputDQMGPUvsCPU )

# process.out = cms.OutputModule("PoolOutputModule",
#                                fileName=cms.untracked.string("file:output.root"),
#                                outputCommands=cms.untracked.vstring("drop *", 
#                                                                     "keep *_*_*_TEST")
#                                )
# process.e = cms.EndPath(process.out)

