import FWCore.ParameterSet.Config as cms 
maxEvents = cms.untracked.PSet( 
input = cms.untracked.int32(-1) 
) 
readFiles = cms.untracked.vstring() 
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles) 
readFiles.extend( [ 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/251/00000/1649EF5C-7D27-E511-A4BF-02163E012B2A.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/251/00000/8424FE87-8627-E511-8FD6-02163E011AAF.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/251/00000/AC41D77E-7B27-E511-A017-02163E013425.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/251/00000/CC3AED20-8227-E511-8B04-02163E014272.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/251/00000/F6733BE5-7F27-E511-83FC-02163E01235C.root', 
] ); 
