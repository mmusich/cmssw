import FWCore.ParameterSet.Config as cms 
maxEvents = cms.untracked.PSet( 
input = cms.untracked.int32(-1) 
) 
readFiles = cms.untracked.vstring() 
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles) 
readFiles.extend( [ 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/548/00000/AC8BA6C0-E129-E511-B791-02163E0127D3.root', 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/548/00000/DE17BC09-D429-E511-9FDF-02163E0135B5.root', 
] ); 
