import FWCore.ParameterSet.Config as cms 
maxEvents = cms.untracked.PSet( 
input = cms.untracked.int32(-1) 
) 
readFiles = cms.untracked.vstring() 
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles) 
readFiles.extend( [ 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/718/00000/6AA35508-EB2B-E511-8A8E-02163E0134FD.root', 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/718/00000/6E2E25D1-EB2B-E511-89E3-02163E014527.root', 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/718/00000/9026F020-E92B-E511-99BE-02163E01359E.root', 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/718/00000/CE3EECB4-EE2B-E511-A63E-02163E01252E.root', 
] ); 
