import FWCore.ParameterSet.Config as cms 
maxEvents = cms.untracked.PSet( 
input = cms.untracked.int32(-1) 
) 
readFiles = cms.untracked.vstring() 
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles) 
readFiles.extend( [ 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/252/00000/0460CAFD-8D27-E511-AA20-02163E01280D.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/252/00000/0ED93788-9527-E511-A04C-02163E0120D4.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/252/00000/1C7A9059-8F27-E511-8203-02163E0143C0.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/252/00000/24AAA209-9F27-E511-BD30-02163E011CD6.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/252/00000/26BC2647-9227-E511-B0C4-02163E011836.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/252/00000/48E28714-9427-E511-8AFF-02163E0133D1.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/252/00000/7E75A3D7-9627-E511-822A-02163E012627.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/252/00000/8A44CC4A-9327-E511-B98C-02163E014437.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/252/00000/94E4E901-9227-E511-B87B-02163E0134AB.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/252/00000/A2BB689E-9B27-E511-ADAB-02163E01414A.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/252/00000/E2806833-8E27-E511-91F6-02163E013553.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/252/00000/EE23E2B0-9227-E511-A6C1-02163E0118BC.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/252/00000/F0CEF023-9127-E511-8798-02163E0127DF.root', 
] ); 
