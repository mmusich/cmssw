import FWCore.ParameterSet.Config as cms 
maxEvents = cms.untracked.PSet( 
input = cms.untracked.int32(-1) 
) 
readFiles = cms.untracked.vstring() 
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles) 
readFiles.extend( [ 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/244/00000/303FBCB6-5A27-E511-87A8-02163E0122C2.root', 
] ); 
