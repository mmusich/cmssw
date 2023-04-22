import glob
import math
import FWCore.ParameterSet.Config as cms

process = cms.Process("AlCaRECOAnalysis")

###################################################################
# Set the process to run multi-threaded
###################################################################
process.options.numberOfThreads = 8

###################################################################
# Message logger service
###################################################################
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.enable = False
process.MessageLogger.ZtoMMNtupler=dict()  
process.MessageLogger.cout = cms.untracked.PSet(
    enable = cms.untracked.bool(True),
    threshold = cms.untracked.string("INFO"),
    default   = cms.untracked.PSet(limit = cms.untracked.int32(0)),                       
    FwkReport = cms.untracked.PSet(limit = cms.untracked.int32(-1),
                                   reportEvery = cms.untracked.int32(1000)
                                   ),                                                      
    ZtoMMNtupler = cms.untracked.PSet( limit = cms.untracked.int32(-1)),
    enableStatistics = cms.untracked.bool(True)
    )

###################################################################
# Geometry producer and standard includes
###################################################################
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
process.load("Configuration.StandardSequences.Services_cff")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load("CondCore.CondDB.CondDB_cfi")

####################################################################
# Get the GlogalTag
####################################################################
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag,"130X_dataRun3_Prompt_v2", '')

###################################################################
# Source
###################################################################
readFiles = cms.untracked.vstring()
process.source = cms.Source("PoolSource",fileNames = readFiles)
readFiles.extend([
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/362/00000/d6641b44-f4e4-4054-b5b0-f038e567c61e.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/433/00000/1f93221e-23ce-4731-906a-48c9fe405515.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/438/00000/5812613b-751a-42e6-b030-4f85747c58da.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/435/00000/df6e27d1-5367-4192-83ed-2be9303d7837.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/503/00000/10d1e4d2-3675-422d-94f2-9feb049ca754.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/437/00000/ea6b065d-1912-491e-9cce-732eaf6fa038.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/437/00000/7ce5bac8-0b29-40f3-a63b-fd0813d5678d.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/613/00000/5f7649f0-b8db-43cf-aefb-39c79f7c8b07.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/439/00000/13e86424-5658-4398-b48c-1cb9c3789b4d.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/439/00000/82e85ac6-b5c8-434a-a756-8ea9252dfc96.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/439/00000/a83b5f31-7784-46ae-9fcf-2b4e56f476c8.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/452/00000/744e93d3-9671-45dc-807a-37c29a470617.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/457/00000/a3e82144-0529-4dda-a884-a874578bbe75.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/459/00000/b79052f0-9bbc-4f8c-b16a-3111baa5a46b.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/596/00000/32e53389-c938-4248-8ee4-bb0a809b5ccd.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/616/00000/69b1d192-4042-4fcf-9f3b-30ee66213a46.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/617/00000/fa190ab2-126d-45e7-a182-97956436dc04.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/673/00000/ae1a453c-4ef5-4a68-a6ce-2066aea9870d.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/618/00000/a1d1fbb8-c759-448e-b3a2-1794ea13adb5.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/439/00000/3fa232e6-a6b3-40ec-91ff-8a7452ce8f75.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/597/00000/7617bc16-1956-4aa3-b6e2-3efc8f350174.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/654/00000/ba7aa4ec-5fbb-452c-a3c7-4fc5265e6dff.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/695/00000/590026f0-525e-4f30-a85e-32c6a3139183.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/615/00000/276bb1d9-32ce-4d1d-a5c8-ac695029abd5.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/614/00000/d89e6bb1-7029-4d6a-bb2e-49439271e553.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/622/00000/f5c84943-d409-4f5f-8507-dfa301dcde58.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/726/00000/ffd48ba0-7467-4ead-a982-38373a6e8625.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/696/00000/416f30df-6679-4d64-9ca9-9a76fbd895d0.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/653/00000/d62587f8-1fc6-477e-b013-a6027907cc67.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/720/00000/a243f207-8fbe-46a3-8556-9694c56ab155.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/720/00000/e76f304c-e978-478a-813d-494ce1174d8a.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/727/00000/9de95d39-eadd-40a2-a7f6-ecc098e07b5e.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/653/00000/eda5169c-15b4-48ec-97f4-d54886a26446.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/757/00000/5a6c734f-badd-431d-81bf-36a463cac0b0.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/760/00000/265e98cc-6552-4101-8585-be229ea7e848.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/657/00000/f7e6da76-2b20-41c0-952f-9986dfa47c22.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/653/00000/f0013a71-ae57-4101-b75e-0661c09058c9.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/655/00000/263713f0-fbd9-4a7d-83ea-30d80240b70f.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/760/00000/9ab8ae7b-9318-48be-afab-b64c3bd23e27.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/696/00000/74910078-ad7c-416b-9209-f349bf877510.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/696/00000/e4da78cc-12e8-44ab-9c55-7fdb328a0336.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/758/00000/f723bd8f-2102-4606-ae20-ef56ffb46c0c.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/698/00000/420b8e8f-a521-4023-9ef4-010ee4befa2b.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/696/00000/03208ea5-d512-47b4-bae6-00db746d936e.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/728/00000/e9e0e12f-cdb7-45aa-a2b3-18138d4d7044.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/720/00000/3176145f-e51b-4b02-abc3-a84242c8a5c8.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/720/00000/fa138d74-22e2-428d-9acf-00f8282fd242.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/759/00000/3bfccdb4-26ae-4316-b281-30365ab85ec6.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/695/00000/e6d27cbf-d198-4bd8-9f70-799e6ca80c8f.root',
    # '/store/data/Run2022G/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/362/696/00000/2585968f-8523-4a8d-a269-bbd186d14bb0.root'
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/757/00000/f83ca9a8-660a-4c7b-a2dd-76a29bc04e3f.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/766/00000/8cf7eb39-6b62-4d26-8c4c-32f2ec43336a.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/779/00000/5bd767b0-1a5d-42ed-9b42-98a17d79a425.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/778/00000/37d17084-8bcd-436d-b510-e060e0843063.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/777/00000/9b146704-4f60-4ac2-91d1-40a6ce96053f.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/803/00000/45fafff7-f21a-49aa-9343-a8aa64a7e2bf.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/806/00000/d948142e-fd54-4f19-8277-d358aae40005.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/808/00000/51b4aec5-e497-433d-9198-c1d3a39cb1fe.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/809/00000/d39b4945-b239-4f22-84ca-26f483980767.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/812/00000/57f29c69-b79c-4e7f-85c9-09491a3cafcd.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/734/00000/9967acaf-6533-4265-9da3-0ff3cbe6b346.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/756/00000/d1310ec1-3991-46de-99b9-ea345c86f898.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/802/00000/1d431aa2-83e1-435c-9789-193b020722d6.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/804/00000/6f2ed37c-2925-45c0-834d-d1068e362666.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/754/00000/3f1b02c2-3543-407b-a303-a0ac7c29c5d8.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/756/00000/8660005a-6356-4190-add5-3b9ee8683f25.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/735/00000/89b6324b-a953-462d-9c58-300509181e9b.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/735/00000/e5a02b95-337d-4131-a378-0ed3aa11a6d2.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/760/00000/47ed31d4-15b9-413d-9676-2fe68f68de6a.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/776/00000/65b5f68f-0d1d-4d55-821b-bc85df1ef027.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/781/00000/73be168f-5622-41a9-a18e-76a380027af1.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/776/00000/6e9db9ee-addc-4c83-8928-76ef62e42a12.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/780/00000/dffddcae-447b-4e4f-90eb-e1b47c5119f0.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/767/00000/4f108bdd-9ad2-406e-b191-8050cf88483e.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/771/00000/65e228f3-6d65-45c5-bbe1-48de14ab3efa.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/770/00000/e12cdec9-4d64-4e73-822b-ab44728997aa.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/759/00000/13785dca-c04d-4bb5-b401-49352d5f8882.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/758/00000/c5c4e08b-734e-4439-a10d-61b5681284cd.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/769/00000/b0084862-aec1-4de1-a6cf-8bac7f4d126a.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/901/00000/821256a7-e7b5-434b-95b0-48138da9035f.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/815/00000/2137fc0b-98f4-46a3-aa58-c77b34c3cb8c.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/886/00000/705f423c-6010-4454-b4ca-2e7746dc1304.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/892/00000/06d848d2-7b03-4594-8d50-ad400b9d68fe.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/899/00000/58ccf294-c2d4-4ff4-8e7d-274181201d6f.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/902/00000/af6e26b1-d4e5-41cf-831e-95db36307b19.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/899/00000/51a66a19-944f-4d60-9c06-373bd2d6f062.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/900/00000/5589ecad-299d-4020-8cfa-c4718e8658de.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/887/00000/beef2bec-c6c0-4dee-80a4-d3bef6e6f0cd.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/888/00000/39c95484-6775-44a0-8b25-f8f5572706ce.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/889/00000/7f854af7-3663-451f-b6ca-20e95bd31917.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/890/00000/d6569aa8-072e-498b-b22c-e8877f172b42.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/896/00000/8326e7ad-3fb2-4c2e-b908-e02678275411.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/885/00000/2490cefd-486e-4196-b09e-853bdd44d853.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/893/00000/faa5a63d-b448-4c39-a035-b075502601c2.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/897/00000/273ce673-8227-49d7-8c7c-b5c98ea6a2bb.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/930/00000/90e5deff-1b0d-48a6-b8ab-114bca1d42d6.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/805/00000/4f43adc3-c424-4f77-9ebd-52937a8008fd.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/814/00000/83a8e23d-dc44-48e4-97dd-babce6ea154b.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/813/00000/8fbd5b88-95da-41dd-8e27-909e6ffa8618.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/807/00000/d036b6c3-8683-4ed1-a713-2c3f4b104b58.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/858/00000/3f0ee3d4-5f90-4517-9903-8f3fdcac4349.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/859/00000/276c2818-9841-4eef-b1e7-0031e9303bab.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/894/00000/d9c12675-bfcc-4a22-9ae5-5f9d6856a24c.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/895/00000/fcc8952b-9272-4666-a1d8-90e154d3262d.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/891/00000/04740c77-e861-4b93-abc2-83b9a5db30a0.root',
    '/store/data/Run2022D/Muon/ALCARECO/TkAlZMuMu-PromptReco-v2/000/357/898/00000/c946ee52-fbb0-4fe2-a1df-f5140199303c.root'
])

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

###################################################################
# Alignment Track Selector
###################################################################
import Alignment.CommonAlignmentProducer.AlignmentTrackSelector_cfi
process.MuSkimSelector = Alignment.CommonAlignmentProducer.AlignmentTrackSelector_cfi.AlignmentTrackSelector.clone(
    applyBasicCuts = True,                                                                            
    filter = True,
    src = "ALCARECOTkAlZMuMu",
    ptMin = 17.,
    pMin = 17.,
    etaMin = -2.5,
    etaMax = 2.5,
    d0Min = -2.,
    d0Max = 2.,
    dzMin = -25.,
    dzMax = 25.,
    nHitMin = 6,
    nHitMin2D = 0)

###################################################################
# The TrackRefitter
###################################################################
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
import RecoTracker.TrackProducer.TrackRefitters_cff
process.TrackRefitter1 = RecoTracker.TrackProducer.TrackRefitter_cfi.TrackRefitter.clone(
    src = "ALCARECOTkAlZMuMu",
    TrajectoryInEvent = True,
    TTRHBuilder = "WithAngleAndTemplate",
    NavigationSchool = "")

###################################################################
# The analysis module
###################################################################
process.myanalysis = cms.EDAnalyzer("ZtoMMNtupler",
                                    #tracks = cms.InputTag('TrackRefitter1'))
                                    tracks = cms.InputTag('ALCARECOTkAlZMuMu'))

from Alignment.OfflineValidation.diMuonValidation_cfi import diMuonValidation as _diMuonValidation
process.DiMuonMassValidation = _diMuonValidation.clone(
    TkTag = 'ALCARECOTkAlZMuMu',
    # mu mu mass
    Pair_mass_min   = 80.,
    Pair_mass_max   = 120.,
    Pair_mass_nbins = 80,
    Pair_etaminpos  = -1,
    Pair_etamaxpos  = 1,
    Pair_etaminneg  = -1,
    Pair_etamaxneg  = 1,
    # cosTheta CS
    Variable_CosThetaCS_xmin  = -1.,
    Variable_CosThetaCS_xmax  =  1.,
    Variable_CosThetaCS_nbins = 20,
    # DeltaEta
    Variable_DeltaEta_xmin  = -4.8,
    Variable_DeltaEta_xmax  = 4.8,
    Variable_DeltaEta_nbins = 20,
    # EtaMinus
    Variable_EtaMinus_xmin  = -2.4,
    Variable_EtaMinus_xmax  =  2.4,
    Variable_EtaMinus_nbins = 12,
    # EtaPlus
    Variable_EtaPlus_xmin  = -2.4,
    Variable_EtaPlus_xmax  =  2.4,
    Variable_EtaPlus_nbins = 12,
    # Phi CS
    Variable_PhiCS_xmin  = -math.pi/2.,
    Variable_PhiCS_xmax  =  math.pi/2.,
    Variable_PhiCS_nbins = 20,
    # Phi Minus
    Variable_PhiMinus_xmin  = -math.pi,
    Variable_PhiMinus_xmax  =  math.pi,
    Variable_PhiMinus_nbins = 16,
    # Phi Plus
    Variable_PhiPlus_xmin  = -math.pi,
    Variable_PhiPlus_xmax  =  math.pi,
    Variable_PhiPlus_nbins = 16,
    # mu mu pT
    Variable_PairPt_xmin  = 0.,
    Variable_PairPt_xmax  = 100.,
    Variable_PairPt_nbins = 100)

###################################################################
# Output name
###################################################################
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("ZmmNtuple_2022Dv2.root"))

###################################################################
# Path
###################################################################
process.p1 = cms.Path(process.offlineBeamSpot
                      #*process.TrackRefitter1
                      * process.myanalysis
                      * process.DiMuonMassValidation)
