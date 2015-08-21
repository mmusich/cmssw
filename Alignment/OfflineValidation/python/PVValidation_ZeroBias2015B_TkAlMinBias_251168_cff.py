import FWCore.ParameterSet.Config as cms 
maxEvents = cms.untracked.PSet( 
input = cms.untracked.int32(-1) 
) 
readFiles = cms.untracked.vstring() 
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles) 
readFiles.extend( [ 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/168/00000/0430E66A-CC26-E511-9D05-02163E01261E.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/168/00000/149A057D-CB26-E511-8CFB-02163E012973.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/168/00000/68EF98EF-D526-E511-8E05-02163E012B2A.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/168/00000/88E286A6-CD26-E511-B48D-02163E01363D.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/168/00000/D6BA4CC3-CE26-E511-9E54-02163E012A7F.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/168/00000/D6F740E3-D726-E511-AA3E-02163E0139CF.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/168/00000/F0204731-CD26-E511-B64B-02163E011E2D.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/168/00000/F68FBADB-D026-E511-9CFF-02163E0136A9.root', 
] ); 
