import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")
process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")

process.load("Geometry.TrackerNumberingBuilder.trackerNumberingGeometry_cfi")

#process.load("CondCore.DBCommon.CondDBSetup_cfi")
from CondCore.DBCommon.CondDBSetup_cfi import *

process.source = cms.Source("EmptySource",
                            firstRun = cms.untracked.uint32(210659) # choose your run! This one is for Run > 210658
                            )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
    )

# initial geom
# configure the database file
#
# This particular configuration refers to: GR_P_V43D
#
from CondCore.DBCommon.CondDBSetup_cfi import *
process.trackerGeom = cms.ESSource("PoolDBESSource",
                                   CondDBSetup,
                                   timetype = cms.string('runnumber'),
                                   toGet = cms.VPSet(cms.PSet(record = cms.string('TrackerAlignmentRcd'),
                                                              tag = cms.string('TrackerAlignment_2009_v1_express')
                                                              ), 
                                                     cms.PSet(record = cms.string('TrackerAlignmentErrorRcd'),
                                                              tag = cms.string('TrackerAlignmentErr_2009_v2_express')
                                                              )
                                                     ),
                                   connect = cms.string('frontier://PromptProd/CMS_COND_31X_ALIGNMENT')
                                   )

# input
process.load("Alignment.TrackerAlignment.TrackerSystematicMisalignments_cfi")
process.TrackerSystematicMisalignments.fromDBGeom = True

#uncomment one or more of these to apply the misalignment(s)

#process.TrackerSystematicMisalignments.radialEpsilon     = 5.00e-4 # default 5e-4 ~ 600 um
#process.TrackerSystematicMisalignments.telescopeEpsilon  = 5.00e-4 # default 5e-4 ~ 600 um
#process.TrackerSystematicMisalignments.layerRotEpsilon   = 9.43e-6 # 9.43e-6
#process.TrackerSystematicMisalignments.bowingEpsilon     = 6.77e-9 # 6.77e-9
#process.TrackerSystematicMisalignments.zExpEpsilon       = 2.02e-4 # 2.02e-4
#process.TrackerSystematicMisalignments.twistEpsilon      = 2.04e-6 # 2.04e-6
#process.TrackerSystematicMisalignments.ellipticalEpsilon = 5.00e-4 # 5e-4
#process.TrackerSystematicMisalignments.skewEpsilon       = 5.5e-2 # 5.5e-2
#process.TrackerSystematicMisalignments.sagittaEpsilon    = 5.00e-4 # 5.0e-4


#process.TrackerSystematicMisalignments.zOffsetEpsilon    = 1.5e-3  #(15 um = PCL threshold) 
process.TrackerSystematicMisalignments.zOffsetEpsilon    = 1.e-3
#process.TrackerSystematicMisalignments.zOffsetEpsilon     = 0.5e-3 

#misalignment phases
process.TrackerSystematicMisalignments.ellipticalDelta   = 0
process.TrackerSystematicMisalignments.skewDelta         = 0
process.TrackerSystematicMisalignments.sagittaDelta      = 0
	
# output
process.PoolDBOutputService = cms.Service("PoolDBOutputService",
                                          CondDBSetup,
                                          toPut = cms.VPSet(cms.PSet(record = cms.string('TrackerAlignmentRcd'),
                                                                     tag = cms.string('Alignments')
                                                                     ), 
                                                            cms.PSet(record = cms.string('TrackerAlignmentErrorRcd'),
                                                                     tag = cms.string('AlignmentErrors')
                                                                     )
                                                            ),
                                          #connect = cms.string('sqlite_file:testBPIX_HS_ZOffset_15um_from_GR_P_V43D_run_GT_210659.db')
                                          connect = cms.string('sqlite_file:testBPIX_HS_ZOffset_10um_from_GR_P_V43D_run_GT_210659.db')
                                          #connect = cms.string('sqlite_file:testBPIX_HS_ZOffset_5um_from_GR_P_V43D_run_GT_210659.db')                                        
                                          )

process.p = cms.Path( process.TrackerSystematicMisalignments )


