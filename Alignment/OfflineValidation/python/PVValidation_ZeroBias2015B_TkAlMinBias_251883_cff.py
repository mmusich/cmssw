import FWCore.ParameterSet.Config as cms 
maxEvents = cms.untracked.PSet( 
input = cms.untracked.int32(-1) 
) 
readFiles = cms.untracked.vstring() 
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles) 
readFiles.extend( [ 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/883/00000/0805B3E8-292D-E511-AEC8-02163E011DA4.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/883/00000/2C7A8C47-212D-E511-8E55-02163E0133B5.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/883/00000/4A356D35-3D2D-E511-A995-02163E0133A4.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/883/00000/5CBDB33F-252D-E511-957A-02163E01340A.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/883/00000/5E07AFED-202D-E511-BBBE-02163E011B6C.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/883/00000/6297DB03-272D-E511-86C6-02163E01265A.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/883/00000/7040F8C9-2D2D-E511-8C1E-02163E011ABC.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/883/00000/8EF8D1BD-252D-E511-ABAF-02163E013901.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/883/00000/A6710BC5-212D-E511-B7D8-02163E0136A2.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/883/00000/BA2E4E45-242D-E511-BDE9-02163E0138F6.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/883/00000/BAF20852-202D-E511-8D57-02163E0126D1.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/883/00000/BE9D4F81-232D-E511-BCEF-02163E011C7F.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/883/00000/D8E017D5-222D-E511-818B-02163E012031.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/883/00000/E6A808FA-272D-E511-90EE-02163E0133B5.root', 
] ); 
