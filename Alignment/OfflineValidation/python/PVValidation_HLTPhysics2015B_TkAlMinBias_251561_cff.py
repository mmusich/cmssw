import FWCore.ParameterSet.Config as cms 
maxEvents = cms.untracked.PSet( 
input = cms.untracked.int32(-1) 
) 
readFiles = cms.untracked.vstring() 
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles) 
readFiles.extend( [ 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/561/00000/16198D90-3D2A-E511-83F7-02163E014509.root', 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/561/00000/2AA79E1A-5A2A-E511-B58F-02163E011DFF.root', 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/561/00000/38D5BF04-4F2A-E511-BBAC-02163E01338A.root', 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/561/00000/4601A25D-3E2A-E511-88BE-02163E014166.root', 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/561/00000/76DB8A2E-392A-E511-9E55-02163E011D57.root', 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/561/00000/78BDB67E-382A-E511-B984-02163E01252E.root', 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/561/00000/AA1C3366-392A-E511-B2B1-02163E011A29.root', 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/561/00000/AEB0B2DC-3C2A-E511-8782-02163E0121E9.root', 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/561/00000/D817BA90-3B2A-E511-B2F2-02163E014275.root', 
'/store/data/Run2015B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/251/561/00000/F2ACFF60-3A2A-E511-9C1D-02163E014462.root', 
] ); 
