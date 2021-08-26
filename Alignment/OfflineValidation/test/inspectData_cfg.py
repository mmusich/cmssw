import glob
import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing()

###################################################################
# Setup 'standard' options
###################################################################

options.register('OutFileName',
                 "test.root", # default value
                 VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                 VarParsing.VarParsing.varType.string, # string, int, or float
                 "name of the output file (test.root is default)")

options.register('myGT',
                 "auto:run3_data_prompt", # default value
                 VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                 VarParsing.VarParsing.varType.string, # string, int, or float
                 "name of the input Global Tag")

options.register('myDataset',
                 "myDataset_v1",
                 VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                 VarParsing.VarParsing.varType.string, # string, int, or float
                 "name of the input dataset")

options.register('maxEvents',
                 -1,
                 VarParsing.VarParsing.multiplicity.singleton, # singleton or list                 
                 VarParsing.VarParsing.varType.int, # string, int, or float
                 "num. events to run")

options.parseArguments()

process = cms.Process("AlCaRECOAnalysis")

###################################################################
# Message logger service
###################################################################
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000

# process.load("FWCore.MessageLogger.MessageLogger_cfi")
# process.MessageLogger.cerr = cms.untracked.PSet(enable = cms.untracked.bool(False))
# process.MessageLogger.cout = cms.untracked.PSet(INFO = cms.untracked.PSet(
#     reportEvery = cms.untracked.int32(1000) # every 100th only
#     #    limit = cms.untracked.int32(10)       # or limit to 10 printouts...
#     ))

###################################################################
# Geometry producer and standard includes
###################################################################
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
process.load("Configuration.StandardSequences.Services_cff")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load('Configuration.StandardSequences.MagneticField_cff')
#process.load("Configuration.StandardSequences.MagneticField_0T_cff")
process.load("CondCore.CondDB.CondDB_cfi")

####################################################################
# Get the GlogalTag
####################################################################
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag,options.myGT, '')

# process.GlobalTag.toGet = cms.VPSet(
#     cms.PSet(record = cms.string("SiPixelTemplateDBObjectRcd"),
#              label = cms.untracked.string("0T"),
#              #tag = cms.string("SiPixelTemplateDBObject_phase1_0T_mc_BoR3_v1"),
#              tag = cms.string("SiPixelTemplateDBObject_phase1_0T_mc_BoR3_v1_bugfix"),
#              connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
#              ),
#     cms.PSet(record = cms.string("SiPixelGenErrorDBObjectRcd"),
#              #tag = cms.string("SiPixelGenErrorDBObject_phase1_0T_mc_BoR3_v1"),
#              tag = cms.string("SiPixelGenErrorDBObject_phase1_0T_mc_BoR3_v1_bugfix"),
#              connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
#              ),
# )


###################################################################
# Source
###################################################################

readFiles = cms.untracked.vstring()
process.source = cms.Source("PoolSource",fileNames = readFiles)
# the_files=[]
# file_list = glob.glob("/eos/cms/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/420/00000/*")
# for f in file_list:
#     the_files.append(f.replace("/eos/cms",""))

# readFiles.extend(the_files)
    
# print(the_files)
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(options.maxEvents))

readFiles.extend([
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/259/00000/772cc7e7-0ab3-4994-bc61-970933652547.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/361/00000/ea93aeb6-fd5e-4f70-8e83-cc8da7b085ac.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/560/00000/88dc3d26-409c-47c6-ba6d-320b3cdf6a56.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/384/00000/374fc58d-00a9-4a8f-944c-31ffd7f02a16.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/375/00000/cfe39fff-9e8d-4887-86b6-ef4ee23b99e8.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/350/00000/cff2d6fa-6591-4b18-8ab1-ba4ed9c50fb0.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/501/00000/bf664031-5552-4f95-b66e-379a940513d8.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/045/00000/ad70ad1d-65d1-4839-8c26-06edb3ef0b13.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/004/00000/ecd8f90e-2399-475c-8470-9500b386942f.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/565/00000/a5cfbbee-d1b2-4dce-99cc-7700a35a5468.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/005/00000/b50f1524-4a24-4de8-a913-574afe1908fb.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/385/00000/b47b233d-aca6-4321-89c0-54d9b6c7fbfb.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/434/00000/25cffd1b-20bf-4263-b6a5-51de166fb79c.root',
#'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/680/00000/8207a4dc-b146-46e7-b52f-75997019aed6.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/606/00000/cc525f62-aad4-4968-8bb8-212169464f94.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/561/00000/3c463bee-def5-436f-abac-a74daee986bb.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/271/00000/cc9d7cb0-cbef-47e9-afac-bbeb9a20a77f.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/666/00000/ab45d5d8-cea4-435b-b4f9-2ed96adcbb39.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/676/00000/11e924fc-7927-4c83-94bd-d4f411d534f7.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/426/00000/0d143899-1e38-4f7a-8bc0-55c026de9cb3.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/007/00000/5412c44c-7b55-49b5-bde1-254f50dfdb93.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/062/00000/11412e93-ab9a-4803-b0e1-412f8b697da6.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/663/00000/aa6605c0-526d-4c39-a462-6705a5c21d59.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/678/00000/2a39b790-e3ad-46cb-9232-b0fb8ea7e193.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/409/00000/fe534ed9-bb0e-4cf1-97bf-0b2503daade2.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/618/00000/c70039ac-93f6-4e39-9094-b3c4fea2d84f.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/386/00000/b02b78e7-726d-4151-91f5-014557334b18.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/169/00000/b5c7aaca-0a73-4c4f-bd5a-8075191d816c.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/380/00000/cc9f9b04-82f4-403c-8004-84b4a5db1960.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/634/00000/d0425a5f-fd01-4623-80f5-bc3d793aff19.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/769/00000/6968b7d3-45d5-418c-825b-dbcb2ed74655.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/433/00000/bb26c439-1f33-4361-a759-59221162ad7b.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/555/00000/bb31ed96-c4b6-4648-ac6b-0058bd983c14.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/059/00000/652d8077-8c73-4db4-9f96-0123841a5994.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/436/00000/646cf6d7-4761-4a23-a20a-bc0de469a574.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/558/00000/4ac577fc-8119-47e4-a7e4-1f6d31a592c2.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/607/00000/be8e1da9-f478-4141-9b98-722e615da482.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/519/00000/a564f106-b87e-4ccf-8e70-03373445e5f3.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/665/00000/2213f870-e493-4978-8c16-01ab3f7da597.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/070/00000/febac4f4-aecb-4452-be02-5c1094655b52.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/677/00000/756c14c2-a2bd-4893-9c5d-d3aef1f246e0.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/567/00000/ed932f59-2dc5-4dd2-a627-e11c488a8304.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/009/00000/3e12ff87-b171-4a51-bf78-596dd66eef82.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/860/00000/717ccbea-ec6f-4293-90a4-2019aa287c94.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/049/00000/c0082c2f-c720-44f1-981d-4634c708f40f.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/772/00000/7fa19536-d957-4b25-98a9-37fc33863c56.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/494/00000/f8a382d3-0c7a-46fd-b18d-e00c91ee749f.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/424/00000/f3810c63-b2c0-47d8-8cbe-74c800ced0fd.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/260/00000/c2fbd124-a724-4580-b572-6ec41690a7ea.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/646/00000/20d0bda2-3d14-47ea-8a8f-8af74a322e19.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/416/00000/fedd6996-2500-4fce-a5fb-15b344dfca25.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/267/00000/844cb356-5592-486e-a8d7-5b4ffc891e1e.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/184/00000/fb0a74b2-7d4f-4cef-af63-4b4917ee35d4.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/167/00000/1f3a414c-fd63-4e27-88c1-85614baf1747.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/348/00000/e71723c8-3901-4d26-b8ef-289f9a5b9623.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/520/00000/2edb2aa5-e3f0-445c-8d6c-103b6b3c7479.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/621/00000/d81b0c51-419d-48c2-bcbb-487af128d5d4.root',
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/934/00000/998e5fdb-0479-44f1-b76c-28d39a24f554.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/623/00000/04379dc5-975d-42d7-a8ad-146824ea7d63.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/657/00000/d467ebe6-ad5e-4f6c-8cbd-38749733264e.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/018/00000/d5f08dc9-7684-4ba9-844f-37f0b0bfa658.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/403/00000/6b3f19fe-ae09-42e3-b29b-89f8d1c5b2ba.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/568/00000/29b2a5b4-3e64-4443-82ac-1650fb719062.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/121/00000/644657b8-b73d-43e7-88d1-17a153269066.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/633/00000/c58569b7-6336-43bf-b5f3-080ba0decc39.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/185/00000/b7c29cc2-24ee-49a0-92c3-7cf641a126ed.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/065/00000/4efba5fd-9b31-448b-8cf6-a9615fbfb501.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/188/00000/20bc1e41-96c1-4073-b805-b79175885cb7.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/767/00000/6bbce3dd-8809-44fa-94b5-b51744637b11.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/648/00000/775900a7-5372-4d49-aec7-34ee7452409b.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/042/00000/465d9675-5ec7-403c-a4dc-4963ace0ba2e.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/080/00000/d7ccc661-8c63-4e58-902a-8ce58535baab.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/609/00000/48dc1703-a192-4053-9706-e9052e1e02eb.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/171/00000/59d8d1ec-858c-4ccd-a899-5c33bc64936b.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/864/00000/796db9f0-1435-45c2-b972-663deb5d0015.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/046/00000/29d48f19-54f1-41dc-98bd-d81a0711f898.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/668/00000/29e605bc-eb59-4207-b7cb-7db34576ac7a.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/268/00000/e41501df-a254-4bda-8ab5-5987fe466de7.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/640/00000/b33de429-303c-4cc3-9a1d-684175a71b80.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/638/00000/82ded8cd-3ca2-4f07-b142-81db7bec548e.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/068/00000/da616e66-0a0d-4b1d-b83d-c8d71db980a8.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/936/00000/20bfb9ab-83e3-46ae-96ff-cea767a0ffee.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/496/00000/f0bd1ed2-a678-40bb-98bf-94027260fad8.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/538/00000/c47af3b1-1ae3-40ab-9a9a-2d88f7554d6e.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/644/00000/eed643f4-b7ff-45ed-a132-fcc24557cca6.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/621/00000/afa93cc7-5b02-49a7-8faa-4845fc4525c5.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/681/00000/21272874-53b5-469b-a46f-e17171387fc8.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/067/00000/0a5bbbba-ee80-477e-9431-c64a0d21b22d.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/677/00000/a7e9d28d-3c50-449b-b4db-b5bd1529b990.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/625/00000/42a0636f-e247-4a66-a80b-214877874b5d.root', 
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/619/00000/6cb5b1c1-87b5-4de6-8590-7f789095cfb0.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/366/00000/c50ddf88-7ade-4519-b277-f8a03e3efd88.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/266/00000/d87b5c34-4931-4f71-9ba4-6ad85340039f.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/680/00000/d55b01ec-8d1a-4bc4-86bc-8c92230fc565.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/082/00000/24acfc2c-e546-488f-b291-8235492a0e6e.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/498/00000/1b4f86a9-ccd0-40cd-8d67-56bb4e2e202f.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/387/00000/1a676ad9-2083-4aff-b5a3-eb9d79c604f5.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/034/00000/7fea47f9-4668-4019-bb67-9433d48197a5.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/566/00000/45c48cd4-aacf-48d1-865e-1e9dfa246840.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/518/00000/4acaf304-aaf9-4003-9ffa-56fe9b639991.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/068/00000/5ea4eb37-bf48-41ce-a514-536010fbdc21.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/774/00000/8bc72178-c727-43b7-b253-471067bf8080.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/186/00000/4a902f2f-7e0a-40fc-b39c-33d615f3d676.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/862/00000/7f3eed15-d1c5-44e4-a474-a14b651fb99b.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/937/00000/597b76c6-caa7-4b78-99a1-236240b8166d.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/343/642/00000/32f7b9e2-cdf5-4c9c-9cef-54c1e1b98311.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/632/00000/a30859a5-29ee-4872-90d5-d26a3d2959ca.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/266/00000/9881adcd-1d42-4123-ae8f-f45828e5dc92.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/679/00000/e8189203-341e-4d6d-b5de-9cfdeeee6a55.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/423/00000/33ae77f1-8ad1-40d8-9b9c-d65e62fb3fe3.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/134/00000/af587822-d3f4-43f5-8809-b2a245479e7a.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/001/00000/be2cc4df-de6f-4d59-a199-650fa4b11301.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/420/00000/59c6c5a2-9d5c-49e1-b523-25e5828c95b9.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/421/00000/7fa4fb7f-4cf1-4d02-94d4-66b3832a8b6b.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/063/00000/1c63b18e-51ff-40e9-b63d-4831d78bbebf.root',  
'/store/data/Commissioning2021/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/344/064/00000/41a7c492-7f89-419a-852f-5ff698d23fc9.root'
])

###################################################################
# momentum constraint for 0T
###################################################################
process.load("RecoTracker.TrackProducer.MomentumConstraintProducer_cff")
import RecoTracker.TrackProducer.MomentumConstraintProducer_cff
process.AliMomConstraint = RecoTracker.TrackProducer.MomentumConstraintProducer_cff.MyMomConstraint.clone()
process.AliMomConstraint.src = 'ALCARECOTkAlCosmicsCTF0T'
process.AliMomConstraint.fixedMomentum = 5.0
process.AliMomConstraint.fixedMomentumError = 0.005

###################################################################
# Alignment Track Selector
###################################################################
import Alignment.CommonAlignmentProducer.AlignmentTrackSelector_cfi

process.MuSkimSelector = Alignment.CommonAlignmentProducer.AlignmentTrackSelector_cfi.AlignmentTrackSelector.clone(
    applyBasicCuts = True,                                                                            
    filter = True,
    src = 'ALCARECOTkAlCosmicsCTF0T',
    ptMin = 17.,
    pMin = 17.,
    etaMin = -2.5,
    etaMax = 2.5,
    d0Min = -2.,
    d0Max = 2.,
    dzMin = -25.,
    dzMax = 25.,
    nHitMin = 6,
    nHitMin2D = 0,
    )

###################################################################
# The TrackRefitter
###################################################################
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
import RecoTracker.TrackProducer.TrackRefitters_cff
process.TrackRefitter1 = process.TrackRefitterP5.clone(
    src =  'ALCARECOTkAlCosmicsCTF0T', #'AliMomConstraint',
    TrajectoryInEvent = True,
    TTRHBuilder = "WithTrackAngle",  #"WithAngleAndTemplate",
    NavigationSchool = "",
    #constraint = 'momentum', ### SPECIFIC FOR CRUZET
    #srcConstr='AliMomConstraint' ### SPECIFIC FOR CRUZET$works only with tag V02-10-02 TrackingTools/PatternTools / or CMSSW >=31X
    )

###################################################################
# The analysis module
###################################################################
process.myanalysis = cms.EDAnalyzer("GeneralPurposeTrackAnalyzer",
                                    TkTag  = cms.InputTag('TrackRefitter1'),
                                    isCosmics = cms.bool(True)
                                    )

process.fastdmr = cms.EDAnalyzer("DMRChecker",
                                 TkTag  = cms.InputTag('TrackRefitter1'),
                                 isCosmics = cms.bool(True)
                                 )

###################################################################
# Output name
###################################################################
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string(options.OutFileName)
                                   )

###################################################################
# Path
###################################################################
process.p1 = cms.Path(process.offlineBeamSpot*
                      #process.AliMomConstraint*
                      process.TrackRefitter1*
                      process.myanalysis*
                      process.fastdmr
                      )
