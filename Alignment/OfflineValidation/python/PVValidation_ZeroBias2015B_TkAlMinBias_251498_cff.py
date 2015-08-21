import FWCore.ParameterSet.Config as cms 
maxEvents = cms.untracked.PSet( 
input = cms.untracked.int32(-1) 
) 
readFiles = cms.untracked.vstring() 
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles) 
readFiles.extend( [ 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/498/00000/38277BF2-0429-E511-B9BC-02163E01412F.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/498/00000/84E704B2-0E29-E511-A214-02163E011EE9.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/498/00000/D66049C9-1429-E511-B009-02163E011CD7.root', 
] ); 
