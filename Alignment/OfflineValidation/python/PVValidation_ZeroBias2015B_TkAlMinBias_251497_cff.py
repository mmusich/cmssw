import FWCore.ParameterSet.Config as cms 
maxEvents = cms.untracked.PSet( 
input = cms.untracked.int32(-1) 
) 
readFiles = cms.untracked.vstring() 
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles) 
readFiles.extend( [ 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/497/00000/1805671B-1929-E511-941E-02163E0133A7.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/497/00000/3A629231-0329-E511-BC9B-02163E014230.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/497/00000/72F202EC-FB28-E511-A21A-02163E01412F.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/497/00000/A4E1C1EB-2529-E511-832C-02163E01208E.root', 
'/store/data/Run2015B/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/497/00000/F02356C6-FB28-E511-8F32-02163E012376.root', 
] ); 
