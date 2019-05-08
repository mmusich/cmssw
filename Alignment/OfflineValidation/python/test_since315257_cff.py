import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/Collisions2018/ReRecoABCD-HGIOV/HLTPhysics_Run2018A-TkAlMinBias-06Jun2018-v1_ALCARECO/HLTPhysics_Run2018A-TkAlMinBias-06Jun2018-v1_ALCARECO_since315257_JSON.txt').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2018A/HLTPhysics/ALCARECO/TkAlMinBias-06Jun2018-v1/40000/7CF4B818-F993-E811-9510-008CFA197AF4.root',
'/store/data/Run2018A/HLTPhysics/ALCARECO/TkAlMinBias-06Jun2018-v1/40000/686D8C54-6D9C-E811-B805-0CC47AD98BF0.root',
'/store/data/Run2018A/HLTPhysics/ALCARECO/TkAlMinBias-06Jun2018-v1/40000/6CAAACED-8692-E811-B6B0-008CFA197B4C.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
