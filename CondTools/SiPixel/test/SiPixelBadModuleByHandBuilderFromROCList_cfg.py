import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
process = cms.Process("ICALIB")

options = VarParsing.VarParsing("analysis")

options.register ('inputFile',
                  "SiPixelQuality_allROC0",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "input list of bad ROCs")
options.parseArguments()


process.load("Configuration.Geometry.GeometryExtended2017_cff")
process.load("Geometry.TrackerGeometryBuilder.trackerParameters_cfi")
process.TrackerTopologyEP = cms.ESProducer("TrackerTopologyEP")

process.MessageLogger = cms.Service("MessageLogger",
    cerr = cms.untracked.PSet(
        enable = cms.untracked.bool(False)
    ),
    cout = cms.untracked.PSet(
        enable = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    )
)

process.source = cms.Source("EmptyIOVSource",
    timetype = cms.string('runnumber'),
    firstValue = cms.uint64(1),
    lastValue = cms.uint64(1),
    interval = cms.uint64(1)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.PoolDBOutputService = cms.Service("PoolDBOutputService",
    BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('')
    ),
    timetype = cms.untracked.string('runnumber'),
    connect = cms.string('sqlite_file:SiPixelQuality_allSameROC.db'),
    toPut = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string(options.inputFile)
    ))
)

process.prod = cms.EDAnalyzer("SiPixelBadModuleByHandBuilder",
                              BadModuleList = cms.untracked.VPSet(),
                              Record = cms.string('SiPixelQualityFromDbRcd'),
                              SinceAppendMode = cms.bool(True),
                              IOVMode = cms.string('Run'),
                              printDebug = cms.untracked.bool(True),
                              doStoreOnDB = cms.bool(True),
                              ROCListFile = cms.untracked.string(options.inputFile+".txt"),
                              )

#process.print = cms.OutputModule("AsciiOutputModule")

process.p = cms.Path(process.prod)
#process.ep = cms.EndPath(process.print)
