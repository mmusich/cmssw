import FWCore.ParameterSet.Config as cms 
maxEvents = cms.untracked.PSet( 
input = cms.untracked.int32(-1) 
) 
readFiles = cms.untracked.vstring() 
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles) 
readFiles.extend( [ 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/499/00000/22D56727-1429-E511-A0C3-02163E012183.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/499/00000/2625E8A5-1129-E511-B8D1-02163E01192D.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/499/00000/88FAF7B5-0A29-E511-A8C6-02163E014437.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/499/00000/962724AD-0B29-E511-907C-02163E01280D.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/499/00000/E80A591E-0D29-E511-BCDC-02163E011DDE.root', 
] ); 
