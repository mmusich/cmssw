import FWCore.ParameterSet.Config as cms 
maxEvents = cms.untracked.PSet( 
input = cms.untracked.int32(-1) 
) 
readFiles = cms.untracked.vstring() 
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles) 
readFiles.extend( [ 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/496/00000/001D4C6B-B32C-E511-B778-02163E0133F2.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/496/00000/22A13020-B02C-E511-9B57-02163E011DE5.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/496/00000/2AF4FD78-AC2C-E511-9506-02163E0134CB.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/496/00000/320C5221-AE2C-E511-9D91-02163E0137FD.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/496/00000/4051DB99-BD2C-E511-8668-02163E01208E.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/496/00000/50B76487-AD2C-E511-AE7D-02163E012787.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/496/00000/640BF5B5-B32C-E511-BF12-02163E0133B5.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/496/00000/7893AAC3-A92C-E511-AB12-02163E012044.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/496/00000/E2B78B15-AC2C-E511-A34A-02163E011CD6.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/496/00000/E62157A9-B62C-E511-B6A3-02163E0137FD.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/496/00000/EAF54D0E-AB2C-E511-8F9F-02163E014181.root', 
] ); 
