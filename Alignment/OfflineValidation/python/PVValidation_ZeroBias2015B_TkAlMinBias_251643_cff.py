import FWCore.ParameterSet.Config as cms 
maxEvents = cms.untracked.PSet( 
input = cms.untracked.int32(-1) 
) 
readFiles = cms.untracked.vstring() 
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles) 
readFiles.extend( [ 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/04C64882-842C-E511-8BD5-02163E0133F9.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/04F383F6-7F2C-E511-9A88-02163E01206A.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/06CC2C1D-8A2C-E511-9F14-02163E0117FF.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/0AC12990-802C-E511-A37F-02163E01364E.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/0CA090D1-7E2C-E511-8F71-02163E01299A.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/1C84BABB-8A2C-E511-B141-02163E011D88.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/26290164-832C-E511-A78A-02163E012603.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/26A9B999-882C-E511-8B21-02163E011A02.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/2E2DBE70-852C-E511-93CE-02163E013542.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/486174A9-892C-E511-8C8D-02163E0127DF.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/4E68E0AB-8B2C-E511-B817-02163E013896.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/5E1D72EA-8C2C-E511-A41F-02163E0123C0.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/64E40189-822C-E511-BFC5-02163E0144D6.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/6637EFDC-7D2C-E511-8CA0-02163E011DCE.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/6CBAD608-912C-E511-8BFD-02163E014558.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/706AFA08-D72C-E511-A91B-02163E012031.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/724F9E5F-872C-E511-B546-02163E014186.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/88A702CD-832C-E511-8038-02163E0124CC.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/964CABDE-842C-E511-9ABC-02163E0143C0.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/A210FBC1-812C-E511-8E26-02163E0129DA.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/B80F0CB2-8E2C-E511-B671-02163E012B10.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/D894423D-962C-E511-B4D5-02163E014527.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/DAF4DD1E-942C-E511-8062-02163E0137FD.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/E25DE3AB-862C-E511-91D0-02163E0141EF.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/F0D3CC91-8D2C-E511-B213-02163E01265A.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/FC8A67F5-8A2C-E511-A7EE-02163E011D88.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/643/00000/FE9439DB-A32C-E511-8757-02163E01387D.root', 
] ); 
