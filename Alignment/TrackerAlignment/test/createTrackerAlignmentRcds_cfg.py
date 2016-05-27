import FWCore.ParameterSet.Config as cms
process = cms.Process("Alignment")

process.load("Configuration.StandardSequences.MagneticField_cff") # B-field map
process.load("Configuration.Geometry.GeometryRecoDB_cff") # Ideal geometry and interface
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff") # Global tag
from Configuration.AlCa.GlobalTag import GlobalTag
process.load("Alignment.TrackerAlignment.createIdealTkAlRecords_cfi")

################################################################################
# parameters to configure:                                                     #
process.GlobalTag = GlobalTag(process.GlobalTag, "80X_dataRun2_Prompt_v8")     #
                                                                               #
process.createIdealTkAlRecords.alignToGlobalTag   = True                       #
################################################################################

################################################################################
# Insert the PB geometry in the ES                                             #
################################################################################

from CondCore.CondDB.CondDB_cfi import *
process.PoolDBESSourceGeometry = cms.ESSource("PoolDBESSource",CondDB.clone(connect = cms.string('frontier://FrontierPrep/CMS_CONDITIONS')),
                                              timetype = cms.string('runnumber'),
                                              #connect = cms.string('sqlite_file:/data/vami/projects/pilotBlade/1ConditionDBs/PilotGeometry.db') #local file
                                              #PilotGeometry.db --> with PB and Fake PB
                                              #PilotGeometry0.db --> with PB only
                                              toGet = cms.VPSet(cms.PSet(record = cms.string('GeometryFileRcd'),
                                                                         #tag = cms.string('XMLFILE_Geometry_74YV2_Extended2015_mc') #for the local file
                                                                         tag = cms.string('SiPixelPilotGeometry_v1')
                                                                         ),
                                                                cms.PSet(record = cms.string('IdealGeometryRecord'),
                                                                         tag = cms.string('TKRECO_Geometry_forPilotBlade_v1')
                                                                         ),
                                                                cms.PSet(record = cms.string('PGeometricDetExtraRcd'),
                                                                         tag = cms.string('TKExtra_Geometry_forPilotBlade_v1')
                                                                         ),
                                                                cms.PSet(record = cms.string('PTrackerParametersRcd'),
                                                                         tag = cms.string('TKParameters_Geometry_forPilotBlade_v1')
                                                                         )
                                                                )
                                              )

process.es_prefer_geometry = cms.ESPrefer( "PoolDBESSource", "PoolDBESSourceGeometry" ) 

usedGlobalTag = process.GlobalTag.globaltag._value
print "Using Global Tag:", usedGlobalTag

process.PoolDBOutputService = cms.Service("PoolDBOutputService",
    CondDB,
    timetype = cms.untracked.string("runnumber"),
    toPut = cms.VPSet(
        cms.PSet(
            record = cms.string("TrackerAlignmentRcd"),
            tag = cms.string("Alignments")
        ),
        cms.PSet(
            record = cms.string("TrackerAlignmentErrorExtendedRcd"),
            tag = cms.string("AlignmentErrorsExtended")
        ),
        cms.PSet(
            record = cms.string("TrackerSurfaceDeformationRcd"),
            tag = cms.string("AlignmentSurfaceDeformations")
        ),
    )
)
process.PoolDBOutputService.connect = \
    ("sqlite_file:tracker_alignment_"+
     usedGlobalTag+("_reference.db"
                    if process.createIdealTkAlRecords.createReferenceRcd
                    else ".db"))

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))
process.source = cms.Source("EmptySource",
                            firstRun = cms.untracked.uint32(274000) # take the latest IOV!
                            )
process.p = cms.Path(process.createIdealTkAlRecords)
