import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

###################################################################
# Setup 'standard' options
###################################################################
options = VarParsing.VarParsing()

options.register('conditionGT',
                 "92X_upgrade2017_realistic_v1",
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "condition global tag for the job (\"auto:run2_data\" is default)")

options.register('conditionOverwrite',
                 "",
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "configuration to overwrite the condition into the GT (\"\" is default)")

options.register('inputCollection',
                 "generalTracks",
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "collections to be used for input (\"ALCARECOSiStripCalMinBias\" is default)")

options.register('outputFile',
                 "calibTreeTest.root",
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "name for the output root file (\"calibTreeTest.root\" is default)")


#readFiles = cms.vstring()

options.register('inputFiles',
                 "/store/relval/CMSSW_9_2_3/RelValTTbar_13/GEN-SIM-RECO/PUpmx25ns_92X_upgrade2017_realistic_v2_earlyBS2017-v1/10000/16F7F59A-4051-E711-BAC0-0CC47A4C8ED8.root",
                 # "/store/relval/CMSSW_9_2_3/RelValTTbar_13/GEN-SIM-RECO/PUpmx25ns_92X_upgrade2017_realistic_v2_earlyBS2017-v1/10000/3270D178-6051-E711-B323-0025905B8590.root
                 # "/store/relval/CMSSW_9_2_3/RelValTTbar_13/GEN-SIM-RECO/PUpmx25ns_92X_upgrade2017_realistic_v2_earlyBS2017-v1/10000/500DC555-4351-E711-B8F1-0025905B85C0.root
                 # "/store/relval/CMSSW_9_2_3/RelValTTbar_13/GEN-SIM-RECO/PUpmx25ns_92X_upgrade2017_realistic_v2_earlyBS2017-v1/10000/70C300B1-4451-E711-B723-0025905A60D0.root
                 # "/store/relval/CMSSW_9_2_3/RelValTTbar_13/GEN-SIM-RECO/PUpmx25ns_92X_upgrade2017_realistic_v2_earlyBS2017-v1/10000/78A70796-3F51-E711-9A4C-0CC47A7C35F4.root
                 # "/store/relval/CMSSW_9_2_3/RelValTTbar_13/GEN-SIM-RECO/PUpmx25ns_92X_upgrade2017_realistic_v2_earlyBS2017-v1/10000/E2431272-3E51-E711-BFA5-0025905A6126.root
                 # "/store/relval/CMSSW_9_2_3/RelValTTbar_13/GEN-SIM-RECO/PUpmx25ns_92X_upgrade2017_realistic_v2_earlyBS2017-v1/10000/E600437E-4551-E711-8EDA-0025905A60A6.root
                 # "/store/relval/CMSSW_9_2_3/RelValTTbar_13/GEN-SIM-RECO/PUpmx25ns_92X_upgrade2017_realistic_v2_earlyBS2017-v1/10000/F4F082FF-3F51-E711-858B-0CC47A78A2F6.root
                 # "/store/relval/CMSSW_9_2_3/RelValTTbar_13/GEN-SIM-RECO/PUpmx25ns_92X_upgrade2017_realistic_v2_earlyBS2017-v1/10000/FCE94075-6051-E711-A961-0CC47A7C3428.root
                 VarParsing.VarParsing.multiplicity.list,
                 VarParsing.VarParsing.varType.string,
                 "file to process")

options.register('maxEvents',
                 -1,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "number of events to process (\"-1\" for all)")

# To use the prompt reco dataset please use 'generalTracks' as inputCollection
# To use the cosmic reco dataset please use 'ctfWithMaterialTracksP5' as inputCollection

options.parseArguments()

print "conditionGT       : ", options.conditionGT
print "conditionOverwrite: ", options.conditionOverwrite
print "inputCollection   : ", options.inputCollection
print "maxEvents         : ", options.maxEvents
print "outputFile        : ", options.outputFile
print "inputFiles        : ", options.inputFiles

process = cms.Process('CALIB')
process.load('CalibTracker.Configuration.setupCalibrationTree_cff')
process.load('Configuration/StandardSequences/MagneticField_cff')
process.load('Configuration.Geometry.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, options.conditionGT, options.conditionOverwrite)

process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.Services_cff')
process.add_( cms.Service( "TFileService",
                           fileName = cms.string( options.outputFile ),
                           closeFileFast = cms.untracked.bool(True)  ) )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )
#process.source = cms.Source (
#    "PoolSource",
#    fileNames = cms.untracked.vstring(options.inputFiles)
#    )


readFiles = cms.untracked.vstring()

readFiles.extend([
        "/store/relval/CMSSW_9_2_2/RelValTTbar_13/GEN-SIM-RECO/PU25ns_92X_upgrade2017_realistic_v1-v1/10000/3EFD6013-B54D-E711-B6E6-0CC47A7C3434.root",
        "/store/relval/CMSSW_9_2_2/RelValTTbar_13/GEN-SIM-RECO/PU25ns_92X_upgrade2017_realistic_v1-v1/10000/4A756F39-BB4D-E711-AFBD-0CC47A7C356A.root",
        "/store/relval/CMSSW_9_2_2/RelValTTbar_13/GEN-SIM-RECO/PU25ns_92X_upgrade2017_realistic_v1-v1/10000/4A88FA63-294E-E711-8F45-0025905A4964.root",
        "/store/relval/CMSSW_9_2_2/RelValTTbar_13/GEN-SIM-RECO/PU25ns_92X_upgrade2017_realistic_v1-v1/10000/523AFFD6-C04D-E711-910C-0CC47A4D76CC.root",
        "/store/relval/CMSSW_9_2_2/RelValTTbar_13/GEN-SIM-RECO/PU25ns_92X_upgrade2017_realistic_v1-v1/10000/5ED1F6E0-C14D-E711-8BE6-0025905B8592.root",
        "/store/relval/CMSSW_9_2_2/RelValTTbar_13/GEN-SIM-RECO/PU25ns_92X_upgrade2017_realistic_v1-v1/10000/7C9ADC20-BA4D-E711-8481-0CC47A7C347E.root",
        "/store/relval/CMSSW_9_2_2/RelValTTbar_13/GEN-SIM-RECO/PU25ns_92X_upgrade2017_realistic_v1-v1/10000/96895A7E-BC4D-E711-B61C-0025905B855E.root",
        "/store/relval/CMSSW_9_2_2/RelValTTbar_13/GEN-SIM-RECO/PU25ns_92X_upgrade2017_realistic_v1-v1/10000/A46F487E-BC4D-E711-8538-0025905A60D0.root",
        "/store/relval/CMSSW_9_2_2/RelValTTbar_13/GEN-SIM-RECO/PU25ns_92X_upgrade2017_realistic_v1-v1/10000/ECFEA1BD-BF4D-E711-A404-0CC47A7C345C.root"
        # "/store/relval/CMSSW_9_2_3/RelValTTbar_13/GEN-SIM-RECO/PUpmx25ns_92X_upgrade2017_realistic_v2_earlyBS2017-v1/10000/16F7F59A-4051-E711-BAC0-0CC47A4C8ED8.root",
        # "/store/relval/CMSSW_9_2_3/RelValTTbar_13/GEN-SIM-RECO/PUpmx25ns_92X_upgrade2017_realistic_v2_earlyBS2017-v1/10000/3270D178-6051-E711-B323-0025905B8590.root",
        # "/store/relval/CMSSW_9_2_3/RelValTTbar_13/GEN-SIM-RECO/PUpmx25ns_92X_upgrade2017_realistic_v2_earlyBS2017-v1/10000/500DC555-4351-E711-B8F1-0025905B85C0.root",
        # "/store/relval/CMSSW_9_2_3/RelValTTbar_13/GEN-SIM-RECO/PUpmx25ns_92X_upgrade2017_realistic_v2_earlyBS2017-v1/10000/70C300B1-4451-E711-B723-0025905A60D0.root",
        # "/store/relval/CMSSW_9_2_3/RelValTTbar_13/GEN-SIM-RECO/PUpmx25ns_92X_upgrade2017_realistic_v2_earlyBS2017-v1/10000/78A70796-3F51-E711-9A4C-0CC47A7C35F4.root",
        # "/store/relval/CMSSW_9_2_3/RelValTTbar_13/GEN-SIM-RECO/PUpmx25ns_92X_upgrade2017_realistic_v2_earlyBS2017-v1/10000/E2431272-3E51-E711-BFA5-0025905A6126.root",
        # "/store/relval/CMSSW_9_2_3/RelValTTbar_13/GEN-SIM-RECO/PUpmx25ns_92X_upgrade2017_realistic_v2_earlyBS2017-v1/10000/E600437E-4551-E711-8EDA-0025905A60A6.root",
        # "/store/relval/CMSSW_9_2_3/RelValTTbar_13/GEN-SIM-RECO/PUpmx25ns_92X_upgrade2017_realistic_v2_earlyBS2017-v1/10000/F4F082FF-3F51-E711-858B-0CC47A78A2F6.root",
        # "/store/relval/CMSSW_9_2_3/RelValTTbar_13/GEN-SIM-RECO/PUpmx25ns_92X_upgrade2017_realistic_v2_earlyBS2017-v1/10000/FCE94075-6051-E711-A961-0CC47A7C3428.root"
        ])

#import runs
process.source = cms.Source (
    "PoolSource",
    #fileNames = cms.untracked.vstring( options.inputFiles )
    fileNames = readFiles
    )

process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.MessageLogger.cerr.FwkReport.reportEvery = 100

#definition of input collection
process.CalibrationTracks.src = cms.InputTag( options.inputCollection )
process.shallowTracks.Tracks  = cms.InputTag( options.inputCollection )
#process.shallowGainCalibrationAllBunch   = 'ALCARECOSiStripCalMinBias' #cms.InputTag( options.inputCollection )
#process.shallowGainCalibrationAllBunch0T = 'ALCARECOSiStripCalMinBias' #cms.InputTag( options.inputCollection )


# BSCNoBeamHalo selection (Not to use for Cosmic Runs) --- OUTDATED!!!
## process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff')
## process.load('HLTrigger/HLTfilters/hltLevel1GTSeed_cfi')

## process.L1T1=process.hltLevel1GTSeed.clone()
## process.L1T1.L1TechTriggerSeeding = cms.bool(True)
## process.L1T1.L1SeedsLogicalExpression = cms.string('(40 OR 41) AND NOT (36 OR 37 OR 38 OR 39)')

#process.TkCalPath = cms.Path(process.L1T1*process.TkCalFullSequence)
process.TkCalPath_StdBunch   = cms.Path(process.TkCalSeq_StdBunch)
process.TkCalPath_StdBunch0T = cms.Path(process.TkCalSeq_StdBunch0T)
process.TkCalPath_IsoMuon    = cms.Path(process.TkCalSeq_IsoMuon)
process.TkCalPath_IsoMuon0T  = cms.Path(process.TkCalSeq_IsoMuon0T)
process.TkCalPath_AagBunch   = cms.Path(process.TkCalSeq_AagBunch)
process.TkCalPath_AagBunch0T = cms.Path(process.TkCalSeq_AagBunch0T)
process.TkCalPath_HitEffOnly = cms.Path(process.TkCalSeq_HitEffOnly)

process.schedule = cms.Schedule( #process.TkCalPath_StdBunch, 
                                 #process.TkCalPath_StdBunch0T,
                                 #process.TkCalPath_IsoMuon,
                                 #process.TkCalPath_IsoMuon0T,
                                 #process.TkCalPath_AagBunch,
                                 #process.TkCalPath_AagBunch0T,
                                 process.TkCalPath_HitEffOnly
                                 )


process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('OtherCMS', 
                                    'StdException', 
                                    'Unknown', 
                                    'BadAlloc', 
                                    'BadExceptionType', 
                                    'ProductNotFound', 
                                    'DictionaryNotFound', 
                                    'InsertFailure', 
                                    'Configuration', 
                                    'LogicError', 
                                    'UnimplementedFeature', 
                                    'InvalidReference', 
                                    'NullPointerError', 
                                    'NoProductSpecified', 
                                    'EventTimeout', 
                                    'EventCorruption', 
                                    'ScheduleExecutionFailure', 
                                    'EventProcessorFailure', 
                                    'FileInPathError', 
                                    'FileOpenError', 
                                    'FileReadError', 
                                    'FatalRootError', 
                                    'MismatchedInputFiles', 
                                    'ProductDoesNotSupportViews', 
                                    'ProductDoesNotSupportPtr', 
                                    'NotFound')
    )
