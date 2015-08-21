import FWCore.ParameterSet.Config as cms 
maxEvents = cms.untracked.PSet( 
input = cms.untracked.int32(-1) 
) 
readFiles = cms.untracked.vstring() 
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles) 
readFiles.extend( [ 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/497/00000/804C1FAF-F528-E511-A19F-02163E012916.root', 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/497/00000/924B5F13-FA28-E511-9101-02163E013746.root', 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/497/00000/EA9D0AA0-F428-E511-8CB9-02163E011CDB.root', 
] ); 
