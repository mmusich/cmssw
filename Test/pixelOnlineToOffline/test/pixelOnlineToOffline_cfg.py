from __future__ import print_function
import FWCore.ParameterSet.Config as cms
process = cms.Process("Test") 

###################################################################
# Messages
###################################################################
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1

###################################################################
# Event Source
###################################################################
process.source = cms.Source("EmptySource",
                            firstRun = cms.untracked.uint32(343498),
                            numberEventsInRun = cms.untracked.uint32(1),
                            )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

###################################################################
# Global Tag
###################################################################
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_data_prompt', '')

###################################################################
# Standard loads
###################################################################
process.load("Configuration.Geometry.GeometryRecoDB_cff")

###################################################################
# Analysis
###################################################################
process.pixelOnlineToOffline = cms.EDAnalyzer("pixelOnlineToOffline",
                                              modulelist = cms.vstring("BPix_BmI_SEC7_LYR2_LDR12F_MOD1", 
                                                                       "BPix_BmI_SEC8_LYR2_LDR14F_MOD1", 
                                                                       "BPix_BmO_SEC3_LYR2_LDR5F_MOD1", 
                                                                       "BPix_BmO_SEC3_LYR2_LDR5F_MOD2", 
                                                                       "BPix_BmO_SEC3_LYR2_LDR5F_MOD3", 
                                                                       "BPix_BpO_SEC1_LYR2_LDR1F_MOD1", 
                                                                       "BPix_BpO_SEC1_LYR2_LDR1F_MOD2", 
                                                                       "BPix_BpO_SEC1_LYR2_LDR1F_MOD3"))

###################################################################
# Path
###################################################################
process.p = cms.Path(process.pixelOnlineToOffline)
