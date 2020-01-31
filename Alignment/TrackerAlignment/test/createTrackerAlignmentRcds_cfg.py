from __future__ import print_function
import FWCore.ParameterSet.Config as cms
process = cms.Process("Alignment")

process.load("Configuration.StandardSequences.MagneticField_cff") # B-field map
#process.load("Configuration.Geometry.GeometryRecoDB_cff") # Ideal geometry and interface
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2026D49_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff") # Global tag
from Configuration.AlCa.GlobalTag import GlobalTag
process.load("Alignment.TrackerAlignment.createIdealTkAlRecords_cfi")

################################################################################
# parameters to configure:
process.GlobalTag = GlobalTag(process.GlobalTag, "auto:phase2_realistic_T15")
process.createIdealTkAlRecords.alignToGlobalTag   = False
process.createIdealTkAlRecords.createReferenceRcd = False
################################################################################
usedGlobalTag = process.GlobalTag.globaltag.value()
print("Using Global Tag:", usedGlobalTag)

from CondCore.CondDB.CondDB_cfi import *
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
    ("sqlite_file:tracker_alignment_phase2_D49"+
     usedGlobalTag+("_reference.db"
                    if process.createIdealTkAlRecords.createReferenceRcd
                    else ".db"))

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))
process.source = cms.Source("EmptySource")
process.p = cms.Path(process.createIdealTkAlRecords)
