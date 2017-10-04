import FWCore.ParameterSet.Config as cms
import copy 

# -----------------------------------------------------------------------
# Default configuration

default = cms.VPSet(
    #### Barrel Pixel HB X- 
    cms.PSet(partition = cms.string("TIB"),
             doScale   = cms.bool(True),
             doSmear   = cms.bool(True),
             scaleFactor = cms.double(1.1),
             smearFactor = cms.double(0.2)
             ),
    cms.PSet(partition = cms.string("TOB"),
             doScale   = cms.bool(True),
             doSmear   = cms.bool(True),
             scaleFactor = cms.double(1.2),
             smearFactor = cms.double(0.15)
             ),
    cms.PSet(partition = cms.string("TID"),
             doScale   = cms.bool(True),
             doSmear   = cms.bool(True),
             scaleFactor = cms.double(1.3),
             smearFactor = cms.double(0.10)
             ),
    cms.PSet(partition = cms.string("TEC"),
             doScale   = cms.bool(True),
             doSmear   = cms.bool(True),
             scaleFactor = cms.double(1.4),
             smearFactor = cms.double(0.05)
             )
    )
