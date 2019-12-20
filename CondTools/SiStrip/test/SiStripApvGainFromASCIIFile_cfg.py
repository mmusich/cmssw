import FWCore.ParameterSet.Config as cms


process = cms.Process("ICALIB")
process.source = cms.Source("EmptyIOVSource",
    firstValue = cms.uint64(325642),
    lastValue = cms.uint64(325642),
    timetype = cms.string('runnumber'),
    interval = cms.uint64(1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.threshold = cms.untracked.string('DEBUG')
process.MessageLogger.cout.threshold = cms.untracked.string('DEBUG')
process.MessageLogger.debugModules = cms.untracked.vstring("*")
process.MessageLogger.destinations = cms.untracked.vstring('cout')
process.MessageLogger.cout = cms.untracked.PSet( threshold = cms.untracked.string('DEBUG'))

#process.load('Configuration.Geometry.GeometryDB_cff')
#process.load('Configuration.Geometry.GeometryIdeal_cff')

process.load("Configuration.Geometry.GeometryExtended2017_cff")
process.load("Geometry.TrackerGeometryBuilder.trackerParameters_cfi")
process.TrackerTopologyEP = cms.ESProducer("TrackerTopologyEP")

#Setup the SiSTripFedCabling and the SiStripDetCabling
process.load("CondCore.CondDB.CondDB_cfi")
process.CondDB.connect='frontier://FrontierProd/CMS_CONDITIONS'

process.poolDBESSource = cms.ESSource('PoolDBESSource',
                                      process.CondDB,
                                      BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
                                      toGet = cms.VPSet( cms.PSet(record = cms.string('SiStripFedCablingRcd'),
                                                                  tag    = cms.string('SiStripFedCabling_GR10_v1_hlt')
                                                                  )
                                                        )
                                     )
                                                                    
process.load("CalibTracker.SiStripESProducers.SiStripConnectivity_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

process.PoolDBOutputService = cms.Service("PoolDBOutputService",
    BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('/afs/cern.ch/cms/DB/conddb')
    ),
    timetype = cms.untracked.string('runnumber'),
    connect = cms.string('sqlite_file:dbfile.db'),
    toPut = cms.VPSet(cms.PSet(
        record = cms.string('SiStripApvGainRcd'),
        tag = cms.string('SiStripApvGainRcd_v1')
    ))
)

process.prod = cms.EDAnalyzer("SiStripApvGainFromFileBuilder",
    outputMaps    = cms.untracked.bool(True),
    outputSummary = cms.untracked.bool(True),
)

process.p = cms.Path(process.prod)


