import FWCore.ParameterSet.Config as cms 
maxEvents = cms.untracked.PSet( 
input = cms.untracked.int32(-1) 
) 
readFiles = cms.untracked.vstring() 
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles) 
readFiles.extend( [ 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/499/00000/3A1A90F2-DB29-E511-867B-02163E011D57.root', 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/499/00000/4863B0BD-0D29-E511-BA82-02163E01280D.root', 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/499/00000/FC65868B-752A-E511-AF55-02163E01420D.root', 
] ); 
