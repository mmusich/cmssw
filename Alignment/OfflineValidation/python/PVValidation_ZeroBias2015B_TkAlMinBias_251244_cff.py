import FWCore.ParameterSet.Config as cms 
maxEvents = cms.untracked.PSet( 
input = cms.untracked.int32(-1) 
) 
readFiles = cms.untracked.vstring() 
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles) 
readFiles.extend( [ 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/244/00000/0C856F63-5627-E511-A5E7-02163E014462.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/244/00000/24535EB5-6627-E511-9196-02163E0126E1.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/244/00000/52CFB67D-5527-E511-AA06-02163E012093.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/244/00000/78D834DC-6727-E511-ADAC-02163E012283.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/244/00000/901C664A-5327-E511-B188-02163E01420D.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/244/00000/A4D15818-6527-E511-A118-02163E0133A7.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/244/00000/B288630D-5A27-E511-9412-02163E0143F8.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/244/00000/C27F6B94-7327-E511-A7AB-02163E0143C0.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/244/00000/C44D45B5-6C27-E511-BBB9-02163E0124CC.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/244/00000/CA57B2C3-4F27-E511-A6F2-02163E0134AB.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/244/00000/D2936C82-5127-E511-8B7F-02163E014527.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/244/00000/E405D6B2-DC28-E511-ACAA-02163E013896.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/244/00000/F2DD6481-4E28-E511-BAE5-02163E011955.root', 
] ); 
