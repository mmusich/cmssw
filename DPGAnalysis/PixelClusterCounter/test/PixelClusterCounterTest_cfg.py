import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('/store/data/Run2023D/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/370/497/00000/edf9d224-8581-452d-bfa0-ef38e452c634.root'))

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.GeometryDB_cff")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_data_prompt', '')

process.PixelClusterFilter = cms.EDFilter("PixelCountFilter",
                                          src = cms.InputTag('ALCARECOTkAlMinBias'),
                                          minNumber = cms.uint32(4000))

process.PixelOccupancyFilter = cms.EDFilter("PixelOccupancyFilter",
                                            src = cms.InputTag('ALCARECOTkAlMinBias'),
                                            minDetSetCounts = cms.uint32(1),
                                            maxDetSetCounts = cms.uint32(100),
                                            minNumber = cms.uint32(100))


process.PixelClusterCounter = cms.EDAnalyzer("PixelClusterCounter", 
                                             pixelClusters = cms.untracked.InputTag('ALCARECOTkAlMinBias'))

process.PixelClusterCheckPath = cms.Path(process.PixelClusterFilter+process.PixelClusterCounter)
