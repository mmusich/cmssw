import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")
# -- Load default module/services configurations -- //
# Message logger service
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cout = cms.untracked.PSet(
    threshold = cms.untracked.string('INFO'),
    default = cms.untracked.PSet(
        limit = cms.untracked.int32(10000000)
    )
)
#replace MessageLogger.debugModules = { "*" }

# service = Tracer {}
# Ideal geometry producer
process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")

# Global Tag
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'GR_P_V43D::All' # take your favourite
#process.GlobalTag.globaltag = 'START53_V27::All' # take your favourite

# Initial Geometry
from CondCore.DBCommon.CondDBSetup_cfi import *
process.trackerAlignment = cms.ESSource(
    "PoolDBESSource",
    CondDBSetup,
    connect = cms.string("sqlite_file:/afs/cern.ch/user/m/musich/public/PixelShiftsForPA/TrackerAlignment_2009_v1_express_210659-211162.db"),
    toGet = cms.VPSet(cms.PSet(record = cms.string("TrackerAlignmentRcd"),
                               tag = cms.string("Alignments")
                               )
                      )
    )

process.es_prefer_trackerAlignment = cms.ESPrefer("PoolDBESSource", "trackerAlignment")

# This uses the object from the tag and applies the misalignment scenario on top of that object
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

# Checks the IOV of the alignment to be applied. Only has an effect
# if applyDbAlignment is True as well. If set to True, the alignment
# record to be applied is expected to have a validity from 1 to INF
process.AlignmentProducer.checkDbAlignmentValidity = False

process.load("Geometry.TrackerNumberingBuilder.trackerNumberingGeometry_cfi")

# Misalignment example scenario producer
# This works only if you like to produce something w.r.t. ideal
#process.load("Alignment.TrackerAlignment.MisalignedTracker_cfi")
#process.MisalignedTracker.saveToDbase = True # to store to DB
#import Alignment.TrackerAlignment.Scenarios_cff as _Scenarios
#process.MisalignedTracker.scenario = _Scenarios.TrackerCSA14Scenario
#process.MisalignedTracker.scenario = _Scenarios.Tracker10pbScenario
#process.MisalignedTracker.scenario = _Scenarios.SurveyLASOnlyScenario
#process.MisalignedTracker.scenario = _Scenarios.SurveyLASCosmicsScenario
#process.MisalignedTracker.scenario = _Scenarios.TrackerCRAFTScenario

# the module
process.prod = cms.EDAnalyzer("TestAnalyzer",
    fileName = cms.untracked.string('misaligned.root')
)

process.source = cms.Source("EmptySource",
                            firstRun = cms.untracked.uint32(210659) # choose your run!
                            )

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1) )

# Database output service
import CondCore.DBCommon.CondDBSetup_cfi
process.PoolDBOutputService = cms.Service("PoolDBOutputService",
    CondCore.DBCommon.CondDBSetup_cfi.CondDBSetup,
    # Writing to oracle needs the following shell variable setting (in zsh):
    # export CORAL_AUTH_PATH=/afs/cern.ch/cms/DB/conddb
    # connect = cms.string('oracle://cms_orcoff_prep/CMS_COND_ALIGNMENT'),  # preparation/develop. DB
    timetype = cms.untracked.string('runnumber'),

    #connect = cms.string('sqlite_file:testBPIX_HS_ZOffset_15um_from_GR_P_V43D_run_GT_210659_fromRandom.db'),                                     
    #connect = cms.string('sqlite_file:testBPIX_HS_PCL_like_FixedMovements_from_GR_P_V43D_run_GT_210659_fromRandom.db'),
    connect = cms.string('sqlite_file:testBPIX_HS_PCL_like_DicedMovements_from_GR_P_V43D_run_GT_210659_fromRandom.db'),
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



