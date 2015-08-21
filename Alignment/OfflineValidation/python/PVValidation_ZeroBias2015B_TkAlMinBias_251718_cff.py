import FWCore.ParameterSet.Config as cms 
maxEvents = cms.untracked.PSet( 
input = cms.untracked.int32(-1) 
) 
readFiles = cms.untracked.vstring() 
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles) 
readFiles.extend( [ 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/718/00000/12319BD4-DF2B-E511-9F65-02163E0126E1.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/718/00000/364CC358-082C-E511-901A-02163E0134BD.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/718/00000/6AA68852-E32B-E511-9938-02163E014624.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/718/00000/825C349E-FA2B-E511-B8CC-02163E014531.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/718/00000/88563870-E82B-E511-B5BB-02163E01206A.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/718/00000/92FBC9B0-F32B-E511-995D-02163E0144CC.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/718/00000/94F00B0F-DF2B-E511-BCFB-02163E0128B9.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/718/00000/AADD6864-F72B-E511-9CE8-02163E0144D6.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/718/00000/B8693F6D-EC2B-E511-9D3C-02163E013455.root', 
] ); 
