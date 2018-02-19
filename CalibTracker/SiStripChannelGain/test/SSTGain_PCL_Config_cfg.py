import FWCore.ParameterSet.Config as cms
import Utilities.General.cmssw_das_client as das_client

###################################################################
def getFileNames_das_client():
###################################################################
    """Return files for given DAS query via das_client"""
    files = []

    query = "dataset dataset=/ZeroBias/Run2*SiStripCalMinBias-*/ALCARECO site=T2_CH_CERN" 
    jsondict = das_client.get_data(query)
    status = jsondict['status']
    if status != 'ok':
        print "DAS query status: %s"%(status)
        return files

    data =  jsondict['data']
    viableDS = []
    for element in data:
        viableDS.append(element['dataset'][0]['name'])

    print "Using Dataset:",viableDS[-1]

    query = "file dataset=%s site=T2_CH_CERN | grep file.name" % viableDS[-1]
    jsondict = das_client.get_data(query)
    status = jsondict['status']
    if status != 'ok':
        print "DAS query status: %s"%(status)
        return files

    mongo_query = jsondict['mongo_query']
    filters = mongo_query['filters']
    data = jsondict['data']

    files = []
    for row in data:
        the_file = [r for r in das_client.get_value(row, filters['grep'])][0]
        if len(the_file) > 0 and not the_file in files:
            files.append(the_file)

    return files

process = cms.Process("APVGAIN")

process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("DQM.SiStripCommon.TkHistoMap_cff")

process.SiStripDetInfoFileReader = cms.Service("SiStripDetInfoFileReader")

#process.MessageLogger = cms.Service("MessageLogger",
#    cout = cms.untracked.PSet( threshold = cms.untracked.string('ERROR')  ),
#    destinations = cms.untracked.vstring('cout')
#)

INPUTFILES=getFileNames_das_client()

if len(INPUTFILES)==0: 
    print "** WARNING: ** According to a DAS query no suitable data for test is available. Skipping test"
    os._exit(0)

myFiles = cms.untracked.vstring()
myFiles.extend([INPUTFILES[0][0].replace("\"","")])

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )
process.source = cms.Source (
    "PoolSource",
    fileNames = cms.untracked.vstring(myFiles)
    )

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')

process.SiStripCalib = cms.EDAnalyzer("SiStripGainFromCalibTree",
                                      OutputGains         = cms.string('Gains_ASCII.txt'),
                                      AlgoMode            = cms.untracked.string('CalibTree'),

                                      minTrackMomentum    = cms.untracked.double(2),
                                      minNrEntries        = cms.untracked.double(25),
                                      maxChi2OverNDF      = cms.untracked.double(9999999.0),
                                      maxMPVError         = cms.untracked.double(25.0),
                                      maxNrStrips         = cms.untracked.uint32(8),
                                      
                                      harvestingMode      = cms.untracked.bool(False),
                                      calibrationMode     = cms.untracked.string('StdBunch'),
                                      DQMdir              = cms.untracked.string('AlCaReco/SiStripGains'),
                                      
                                      Validation          = cms.untracked.bool(False),
                                      OldGainRemoving     = cms.untracked.bool(False),
                                      FirstSetOfConstants = cms.untracked.bool(True),
                                      
                                      CalibrationLevel    = cms.untracked.int32(0), # 0==APV, 1==Laser, 2==module
                                      ChargeHisto = cms.untracked.vstring('TIB','TIB_layer_1','TOB','TOB_layer_1','TIDminus','TIDplus','TECminus','TECplus'),
                                      
                                      InputFiles          = cms.untracked.vstring(),

                                      UseCalibration     = cms.untracked.bool(False),
                                      calibrationPath    = cms.untracked.string(""),
                                      
                                      saveSummary         = cms.untracked.bool(False),

                                      GoodFracForTagProd  = cms.untracked.double(0.98),
                                      NClustersForTagProd = cms.untracked.double(1E8),
    
                                      
                                      SinceAppendMode         = cms.bool(True),
                                      TimeFromEndRun          = cms.untracked.bool(False),
                                      TimeFromStartOfRunRange = cms.untracked.bool(True),
                                      IOVMode                 = cms.string('AlgoDriven'),
                                      Record                  = cms.string('SiStripApvGainRcd'),
                                      doStoreOnDB             = cms.bool(True),

                                      treePath            = cms.untracked.string('gainCalibrationTree/tree'),
                                      gain                = cms.untracked.PSet(label = cms.untracked.string('shallowGainCalibration'), prefix = cms.untracked.string("GainCalibration"), suffix = cms.untracked.string('')),
                                      evtinfo             = cms.untracked.PSet(label = cms.untracked.string('shallowEventRun'), prefix = cms.untracked.string(""), suffix = cms.untracked.string('')),
                                      tracks = cms.untracked.PSet(label = cms.untracked.string('shallowTracks'), prefix = cms.untracked.string("track"), suffix = cms.untracked.string('')),                                      
                                      )

process.SiStripCalib.FirstSetOfConstants = cms.untracked.bool(False)
process.SiStripCalib.CalibrationLevel    = cms.untracked.int32(0) # 0==APV, 1==Laser, 2==module

process.PoolDBOutputService = cms.Service("PoolDBOutputService",
    BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
    DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(2),
        authenticationPath = cms.untracked.string('/afs/cern.ch/cms/DB/conddb')
    ),
    timetype = cms.untracked.string('runnumber'),
    connect = cms.string('sqlite_file:Gains_Sqlite.db'),
    toPut = cms.VPSet(cms.PSet(
        record = cms.string('SiStripApvGainRcd'),
        tag = cms.string('IdealGainTag')
        )
                      )
)

process.TFileService = cms.Service("TFileService",
        fileName = cms.string('Gains_Tree.root')  
)

process.load('CalibTracker.Configuration.setupCalibrationTree_cff')
#definition of input collection
process.CalibrationTracks.src = cms.InputTag('ALCARECOSiStripCalMinBias')
process.shallowTracks.Tracks = cms.InputTag('ALCARECOSiStripCalMinBias')
process.TkCalPath_StdBunch = cms.Path(process.TkCalSeq_StdBunch+process.SiStripCalib)

process.schedule = cms.Schedule( process.TkCalPath_StdBunch)

# process.load('Alignment.CommonAlignmentProducer.AlignmentTrackSelector_cfi')
# process.load('RecoVertex.BeamSpotProducer.BeamSpot_cff')
# process.load('RecoTracker.TrackProducer.TrackRefitters_cff')

# process.CalibrationTracksRefit = process.TrackRefitter.clone(src = cms.InputTag("CalibrationTracks"),
#                                                              NavigationSchool = cms.string("")
#                                                              )

# process.CalibrationTracks = process.AlignmentTrackSelector.clone(
#     #    src = 'generalTracks',
#     src = 'ALCARECOSiStripCalMinBias',
#     filter = True,
#     applyBasicCuts = True,
#     ptMin = 0.8,
#     nHitMin = 6,
#     chi2nMax = 10.,
#     )

# # refit and BS can be dropped if done together with RECO.
# # track filter can be moved in acalreco if no otehr users
# process.trackFilterRefit = cms.Sequence( process.CalibrationTracks + process.offlineBeamSpot + process.CalibrationTracksRefit )

# process.p = cms.Path(process.trackFilterRefit*process.SiStripCalib)
