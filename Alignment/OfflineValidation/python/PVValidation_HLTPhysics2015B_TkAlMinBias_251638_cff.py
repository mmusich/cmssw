import FWCore.ParameterSet.Config as cms 
maxEvents = cms.untracked.PSet( 
input = cms.untracked.int32(-1) 
) 
readFiles = cms.untracked.vstring() 
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles) 
readFiles.extend( [ 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/638/00000/082D2D72-FB2A-E511-8EA5-02163E013406.root', 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/638/00000/480DE243-F52A-E511-980C-02163E01287D.root', 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/638/00000/6ACA9B97-532B-E511-8130-02163E01414A.root', 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/638/00000/7626607A-032B-E511-B716-02163E01360C.root', 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/638/00000/7C9BAB5B-102B-E511-BBC4-02163E01474A.root', 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/638/00000/8E618BC9-3F2B-E511-8FFF-02163E0133CA.root', 
] ); 
