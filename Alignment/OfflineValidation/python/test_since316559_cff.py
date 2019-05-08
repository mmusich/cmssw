import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/Collisions2018/ReRecoABCD/json_DCSONLY.txt').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2018A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/316/713/00000/E42A0055-2366-E811-99BB-FA163E74E2EE.root',
'/store/data/Run2018A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/316/749/00000/98D50951-0F66-E811-8C3D-02163E017EB8.root',
'/store/data/Run2018A/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v3/000/316/701/00000/1C70F833-6066-E811-ABA3-FA163EA55BB8.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
