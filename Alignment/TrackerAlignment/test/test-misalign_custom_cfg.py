import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("TEST")

###################################################################
# Setup 'standard' options
###################################################################
options = VarParsing.VarParsing()
options.register('fromGT',
                 True,VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.bool,
                 "True: run from GT; False: run from user specified payloads")
options.parseArguments()

###################################################################
# Message logger service
###################################################################
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cout = cms.untracked.PSet(
    threshold = cms.untracked.string('INFO'),
    default = cms.untracked.PSet(
        limit = cms.untracked.int32(10000000)
    )
)
# replace MessageLogger.debugModules = { "*" }
# service = Tracer {}

###################################################################
# Ideal geometry producer and standard includes
###################################################################
process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")
process.load("Geometry.TrackerNumberingBuilder.trackerNumberingGeometry_cfi")

###################################################################
# Option 1: just state the Global Tag (and pick some run)
###################################################################
if options.fromGT:
    process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
    process.GlobalTag.globaltag = 'GR_P_V43D::All' # take your favourite
    print "Using global tag: %s" % process.GlobalTag.globaltag._value

###################################################################
# Option 2: You need to specify each tag (with unlimited IOV)
###################################################################
else:
    ##
    ## Global Position Record
    ##
    from CondCore.DBCommon.CondDBSetup_cfi import *
    process.GLBPos = cms.ESSource(
        "PoolDBESSource",
        CondDBSetup,
        connect = cms.string("frontier://PromptProd/CMS_COND_31X_ALIGNMENT"),
        toGet = cms.VPSet(cms.PSet(record = cms.string("GlobalPositionRcd"),
                                   tag = cms.string("GlobalAlignment_2009_v2_express")
                                   )
                          )
        )
    
    process.es_prefer_GLBPosRcd = cms.ESPrefer("PoolDBESSource", "GLBPos")

    ##
    ## APE
    ##
    process.trackerAPE = cms.ESSource(
        "PoolDBESSource",
        CondDBSetup,
        connect = cms.string("frontier://PromptProd/CMS_COND_31X_ALIGNMENT"),
        toGet = cms.VPSet(cms.PSet(record = cms.string("TrackerAlignmentErrorRcd"),
                                   tag = cms.string("TrackerAlignmentErr_2009_v2_express")
                                   )
                          )
        )
    
    process.es_prefer_trackerAPE = cms.ESPrefer("PoolDBESSource", "trackerAPE")

    ##
    ## Initial Geometry (with unlimited IOV)
    ##
    process.trackerAlignment = cms.ESSource(
        "PoolDBESSource",
        CondDBSetup,
        # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideHowToMisalignPixel#Create_and_unlimited_IOV_payload
        connect = cms.string("sqlite_file:/afs/cern.ch/user/m/musich/public/PixelShiftsForPA/UnlimitedIOV/TrackerAlignment_2009_v1_express_IOV18.db"),
        toGet = cms.VPSet(cms.PSet(record = cms.string("TrackerAlignmentRcd"),
                                   tag = cms.string("Alignments")
                                   )
                          )
        )
    
    process.es_prefer_trackerAlignment = cms.ESPrefer("PoolDBESSource", "trackerAlignment")

    ##
    ##  SurfaceDeformations (with unlimited IOV)
    ##
    process.trackerSurfaceDeformations = cms.ESSource(
        "PoolDBESSource",
        CondDBSetup,
        # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideHowToMisalignPixel#Create_and_unlimited_IOV_payload
        connect = cms.string("sqlite_file:/afs/cern.ch/user/m/musich/public/PixelShiftsForPA/UnlimitedIOV/TrackerSurafceDeformations_v1_express_IOV2.db"), 
        toGet = cms.VPSet(cms.PSet(record = cms.string("TrackerSurfaceDeformationRcd"),
                                   tag = cms.string("SurfaceDeformations")
                                   )
                          )
        )

    process.es_prefer_trackerSurfaceDeformations = cms.ESPrefer("PoolDBESSource", "trackerSurfaceDeformations")

    print ">>>>>>>>>>>>>>>  Using Sparse Tags!"
    #print process.GLBPos.connect.__dict__
    print "GlobalPosition Rcd from %s %s" % (process.GLBPos.connect._value,process.GLBPos.toGet[0].tag._value)
    print "APE from %s %s" % (process.trackerAPE.connect._value,process.trackerAPE.toGet[0].tag._value)
    print "Alignment from %s %s" % (process.trackerAlignment.connect._value,process.trackerAlignment.toGet[0].tag._value)
    print "SurfaceDeformations from %s %s" % (process.trackerSurfaceDeformations.connect._value,process.trackerSurfaceDeformations.toGet[0].tag._value)
    print "<<<<<<<<<<<<<<<"

###################################################################
# This uses the object from the tag and applies the misalignment scenario on top of that object
###################################################################
process.load("Alignment.CommonAlignmentProducer.AlignmentProducer_cff")
process.AlignmentProducer.doMisalignmentScenario=True
process.AlignmentProducer.applyDbAlignment=True
from Alignment.TrackerAlignment.Scenarios_cff import *

#process.AlignmentProducer.MisalignmentScenario = NoMovementsScenario
#process.AlignmentProducer.MisalignmentScenario = PixelTrackerOnlyZShift
#process.AlignmentProducer.MisalignmentScenario = PixelTrackerFixedShiftsAndRotations
process.AlignmentProducer.MisalignmentScenario = PixelTrackerDicedShiftsAndRotations

process.AlignmentProducer.saveToDB=True
process.AlignmentProducer.saveApeToDB=True


###################################################################
# Checks the IOV of the alignment to be applied. Only has an effect
# if applyDbAlignment is True as well. If set to True, the alignment
# record to be applied is expected to have a validity from 1 to INF
# Default is true
###################################################################
if options.fromGT:
    process.AlignmentProducer.checkDbAlignmentValidity = False

###################################################################
# Misalignment example scenario producer
# >>>>>>> THIS WORKS ONLY IF YOU WANT TO START FROM IDEAL
###################################################################
#process.load("Alignment.TrackerAlignment.MisalignedTracker_cfi")
#process.MisalignedTracker.saveToDbase = True # to store to DB
#import Alignment.TrackerAlignment.Scenarios_cff as _Scenarios
#process.MisalignedTracker.scenario = _Scenarios.TrackerCSA14Scenario
#process.MisalignedTracker.scenario = _Scenarios.Tracker10pbScenario
#process.MisalignedTracker.scenario = _Scenarios.SurveyLASOnlyScenario
#process.MisalignedTracker.scenario = _Scenarios.SurveyLASCosmicsScenario
#process.MisalignedTracker.scenario = _Scenarios.TrackerCRAFTScenario

###################################################################
# The module
###################################################################
process.prod = cms.EDAnalyzer("TestAnalyzer",
    fileName = cms.untracked.string('misaligned.root')
)

###################################################################
# Output name
###################################################################
outputfilename = None
scenariolabel  = process.AlignmentProducer.MisalignmentScenario._Labelable__label

###################################################################
# Source
###################################################################
if options.fromGT:
    process.source = cms.Source("EmptySource",
                                firstRun = cms.untracked.uint32(210659) # choose your run!
                                )
    outputfilename = "testBPIX_HS_PCL_like_"+str(scenariolabel)+"_from"+process.GlobalTag.globaltag._value.replace('::All','')+"_fromRandomTool.db"
else:
    process.source = cms.Source("EmptySource")
    outputfilename = "testBPIX_HS_PCL_like_"+str(scenariolabel)+"_fromSparseTags_fromRandomTool.db"

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1) )

###################################################################
# Database output service
###################################################################

import CondCore.DBCommon.CondDBSetup_cfi
process.PoolDBOutputService = cms.Service("PoolDBOutputService",
    CondCore.DBCommon.CondDBSetup_cfi.CondDBSetup,
    # Writing to oracle needs the following shell variable setting (in zsh):
    # export CORAL_AUTH_PATH=/afs/cern.ch/cms/DB/conddb
    # connect = cms.string('oracle://cms_orcoff_prep/CMS_COND_ALIGNMENT'),  # preparation/develop. DB
    timetype = cms.untracked.string('runnumber'),

    #connect = cms.string('sqlite_file:testBPIX_HS_ZOffset_15um_from_GR_P_V43D_run_GT_210659_fromRandom.db'),                                     
    #connect = cms.string('sqlite_file:testBPIX_HS_PCL_like_FixedMovements_from_GR_P_V43D_run_GT_210659_fromRandom.db'),                                     
    #connect = cms.string('sqlite_file:testBPIX_HS_PCL_like_DicedMovements_from_GR_P_V43D_IOV18_fromRandom_v2.db'),

    connect = cms.string('sqlite_file:'+outputfilename),                                      
    toPut = cms.VPSet(cms.PSet(
        record = cms.string('TrackerAlignmentRcd'),
        tag = cms.string('Alignments')
    ), 
        cms.PSet(
            record = cms.string('TrackerAlignmentErrorRcd'),
            tag = cms.string('AlignmentErrors')
        ))
)
process.PoolDBOutputService.DBParameters.messageLevel = 2

process.p1 = cms.Path(process.prod)



