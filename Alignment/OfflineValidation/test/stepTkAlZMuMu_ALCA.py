# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: stepTkAlZMuMu -s ALCA:TkAlZMuMu --conditions auto:phase2_realistic_T25 --datatier ALCARECO -n -1 --eventcontent ALCARECO --geometry Extended2026D98 --era Phase2C17I13M9 -n -1 --fileout file:step5.root --nThreads 4 --dasquery=file dataset=/RelValZMM_14/CMSSW_14_0_0_pre2-133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/GEN-SIM-RECO
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C17I13M9_cff import Phase2C17I13M9

process = cms.Process('ALCA',Phase2C17I13M9)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D98Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.AlCaRecoStreamsMC_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(      
        # '/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/1481bfbc-fdf4-4f90-95af-6dee16531d6f.root',
        # '/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/3b832c44-be67-42b4-bdda-96424f023a63.root',
        # '/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/3ee69424-4178-4918-ab8c-9cb661e6adb0.root',
        # '/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/454cd761-a6c2-4fa9-a977-03fb93d33730.root',
        # '/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/4af59678-c8fd-47fc-bec1-6b427eadb3ed.root',
        # '/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/750e1f66-c169-48be-ac22-4660d5a632b1.root',
        # '/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/75187b62-cee5-4569-9ffb-44f5fd7a1bda.root',
        # '/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/857bed3a-d752-4b53-a37b-43dd3ce97603.root',
        # '/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/a3045d82-ea23-49c8-9e6a-469298ed763d.root',
        # '/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/c0d6470a-9d11-4870-bd63-eaec2d68ab42.root',
        # '/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/d5674a0e-f501-4b59-8564-af48a1e35617.root',
        # '/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/d8af002a-53e3-4b24-98ee-985ee2a43af9.root',
        # '/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/e5d7219d-b834-458f-bd48-3c71d1baa385.root',
        # '/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/e9d5b345-9984-49c5-8bf9-6d4a27a35db0.root',
        # '/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/fe8b47e9-be5d-4518-9925-12359ac92400.root'

        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/f078bd9f-2d1d-47f7-8cb6-7c7c3fab00d9.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/8617e418-5bec-47bb-b325-b8f5db4da6d0.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/1229b69a-446c-45d2-8227-bec01f6efded.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/45f5007d-00eb-4f42-929d-0638295bd31d.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/b237d036-e709-415c-b624-1d44b4e232c4.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/46fbf395-6c7c-4e79-a041-aee785320ee0.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/c07f7311-9068-4faa-94c9-195a6733f883.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/c6c18018-9292-4b33-a7e0-0a2eac7e964f.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/041e22d5-6ab5-4dd8-9046-68efc34ebe24.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/640dac54-f0c6-4b22-824c-e86e1d2a8ab6.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/6f6eeea1-7be6-41c2-8a7f-87bf537c3992.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/0b64e5b4-e251-45e2-abda-6b325ba896f1.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/8b9b9585-703f-4294-a559-26c007f15c4b.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/0878623e-369f-45ba-bf56-422b990c8b66.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/51ab59c6-374c-4ada-b899-e9f4b6f09927.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/2ccda4c3-bece-4196-bea8-a5b46c67d548.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/2d5295d4-2b75-4ab5-9ab3-1c0e308bf546.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/535ee44e-b327-49af-864b-d4aef4cc5558.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/462048e3-2a4c-4b8c-b963-a7ca271487b8.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/8fc6d3fc-62ef-499d-b217-25c4fd6a08e6.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/de415951-e814-473a-a961-bd5b5be19bbf.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/c477a5d9-3e30-4a17-a599-e8d091ca8b21.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/d507a3d3-f36b-4b04-8978-4f43e176db4e.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/86cb6334-4d4b-4269-90e0-aa774296bd96.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/dccefbc4-04d8-4dad-ab7a-2139cbc08602.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/161d67b2-e895-4484-bc98-f1ef0b76385b.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/6d20f84d-51d6-42ec-8593-0977e6ea02ad.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/203249b3-9669-4bdf-a151-35e4a8b15c0c.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/ea328833-b32e-4a01-bb22-d4ab023f26e1.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/f08ac30b-b449-4686-92d8-b1e80d3dd06a.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/236fa815-a8df-40c1-a318-4381d17510da.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/6f3f2aee-dc94-4fb6-abec-b669931d621e.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/27777a23-b456-400f-b9cf-e1017921dbad.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/b5e27402-9ae0-44d0-9f9c-2e4d4b6c5abe.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/19956c4d-204f-44f6-b66e-a60e43066bde.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/ff281729-4335-46ba-bb66-1664f73a41c0.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/c9db2ba7-9c65-45d7-b4b8-cedc9ab6284c.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/7c1eadd0-e81c-4992-9e0f-cf32bc1a84bb.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/cd4fe947-33d8-4ced-a055-40ce0ce64c47.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/41c5f4ee-21db-433f-99a8-5b2c3610dcc2.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/0bd6ae1f-bfea-43db-8803-e62d7406cd1b.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/2d76167a-1d17-4b34-80de-c25421c6c583.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/988f9066-9cc5-4efc-9ad2-e42251cdb54a.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/e0d7f2d9-702a-4f39-ba6e-07eb649603f6.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/8c4fede3-915c-41cc-a399-a3fc34736db9.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/37bfc522-ed4b-423f-8e5f-c893dfbd881c.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/82af470f-d7f8-401c-b821-83b9ae597cb0.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/800962e9-82c2-42e5-9c9f-a8931afc16e0.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/58aa90f7-1b9d-449e-b693-1c7d8d725df6.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/94624127-2ef9-41ca-841a-e5ddf4e8118a.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/d0a104d5-3df7-49f1-a524-e576ce8368ae.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/3a088851-9628-43a7-9540-09307436b4a1.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/00547f76-27f4-46ba-abf8-73339b40bf84.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/42fa7585-8d2f-4b6c-a467-f0bc1805c173.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/0451e8e5-6ed7-430f-8e43-731f45663eef.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/ed5339f4-1118-41e5-8280-84ae61b0daeb.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/243d9a17-c60d-48f9-9de4-f36a03ab10d6.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/da53180e-4b76-4d1e-8622-33091cef08cb.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/0449d545-189c-42d6-bd95-7b59e191ed92.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/dd010f3b-3c0d-40b9-b32b-05e2f876f9d6.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/1b947da2-fe57-450c-835f-077c45f56106.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/aa2c5dbf-621d-45d6-8830-c09bfab3ba2c.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/aefbfa47-5de3-4cea-a723-b06655e090e6.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/506d22f2-1872-4473-9f32-3305f3973ebe.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/4724dd1d-f679-465b-a51c-ffdb48dcbf15.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/fe3dd9a7-4486-4048-bb58-bd04a4629094.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/0037f328-2af6-493d-91d7-31c1a60bcb0a.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/7a7bd7c4-eb2f-4b35-a918-7e83434f90fb.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/8cfac55b-f31a-4a5b-9e9d-170282884b90.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/ffad0d2f-4a9c-4412-8853-83fe8b91d231.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/915b26a6-0588-40c8-8aa0-c1d1a5ce0f31.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/a4dededb-527a-4286-b469-195d605c8fd6.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/ba173fcb-5b2b-48fd-a8b6-5cc36096c402.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/f3227ce6-d81e-44f0-bb85-3516791be0f2.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/fe3dd985-072b-456f-9e31-72ea9204b202.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/e0cd641d-86ed-42f9-97c1-686b3006cafe.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/cca4c8ea-76e6-479e-a155-bcdd66220e54.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/8f4ff71c-c992-42bf-8521-aba782e653f0.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/53297aad-16d1-4a3f-b69f-187b3ad50e49.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/48fc04a1-5578-4ce3-99cf-35bf77402e1c.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/06cb4c76-c424-448a-af01-b0120fec0488.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/41c09ee5-3c06-41a3-880a-df4bc31429ad.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/b71e38c1-8ee9-4174-aa48-0b1ad049b4ba.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/8e65e697-8b33-4f6c-9118-5ad50f666b10.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/f2670209-5259-4c54-beef-ffde15d25c2f.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/b605c803-cd79-443e-b49b-9e2394f3e8c8.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/9250e9cb-8a3f-4dba-8539-e0d7cc00a3fc.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/a726f544-b7e0-4781-bdba-6066e9b39023.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/da8d29fa-3b20-468e-8976-f6b858106402.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/b4c9ac91-b77a-45af-8c13-188be120cec5.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/fca7b385-4faa-45ad-8ced-7e67c74af142.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/eb23752f-7156-419c-8b8d-498bd9cc59d1.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/627f909f-9181-4742-ac75-2c903de44c4f.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/83aa1851-2beb-46a8-a9a6-0433af397ce2.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/42d8aace-5d92-4fd6-ac90-6261e2e2d186.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/74e4f625-1445-464e-a935-a6cbdf6d2dcf.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/94f91c50-591b-4cff-ad87-4e1e4b83e4de.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/61764c93-c668-44f8-8318-71f44392ea87.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/e06d06ea-5c1a-45c9-92b9-09b0f494e3e3.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/b9f07c8a-c332-4540-87c7-7cb2fc3298fc.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/47000e4d-1180-4f8f-98bc-e3bb30818aa2.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/8e065f11-bfdd-4fcc-a8a7-8edfc4d4edf9.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/e0badd11-aa2d-4a83-a889-f8680fbb1889.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/3aa6b36b-ef9e-4713-a01e-2dd6ff74322a.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/76217a7b-9f59-44d5-886d-8ecb7cea2ea9.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/5a4e916c-7e48-4b17-995b-7dd2c9b81d65.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/e9a0390e-1786-438d-9c34-65956e7ef1b4.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/beee3336-c21e-4791-86db-9b9a94e12872.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/37ffefa7-971a-456f-83b2-34c49c842832.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/db2341cf-ae46-4751-b872-c6c2bf9c208b.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/d2811da8-ddc9-412b-ac47-c9ec7a2a48ac.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/01932bf0-f5ea-46e9-b15f-bc24c0936bf7.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/ef70a4b8-4390-437a-8649-2417434834bb.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/f9849128-6a76-49ef-bfd0-21309bcda99c.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/28ab8ce5-d754-484d-bd47-241f57a620fe.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/6acc43d1-8cca-4a98-8903-53a156bbc74f.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/dcfa77b7-7891-4a8a-8e89-a0ac19800b69.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/09e17fc6-bc81-44ed-99fa-2485933ab2e7.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/3af5ab66-ba18-4891-8eda-6dda98318fb9.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/a9597b36-42ec-402b-8ea2-f6820d020ef0.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/a5ee4323-2f4e-4b6d-ae4b-8c10a561aaf3.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/fad0c0eb-6471-4540-963f-5270eb5c1b42.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/f114af6e-47d4-4150-8851-7a0b11421816.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/8158abb5-a404-49cc-bc6f-5d8a0671e1e5.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/070df486-060d-4fee-8e42-4eb676dfe199.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/9b9f9df2-581c-4336-a839-82026be626ec.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/56292d0d-acc2-4e04-9020-6c7243f074dd.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/a9122451-28bb-482c-988f-7606cbba180d.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/a8bbdb1c-bf0f-41ef-9d21-95851b98d44e.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/b52be473-088b-409a-9dc0-2b0482c69557.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/16e7a32e-506a-4768-906b-fd4ae0c9b26d.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/c35696b5-baad-467e-bf3e-e11a185d7b75.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/769f954b-8db9-485c-add1-d0793dc7bd88.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/eba2f8a1-50a8-4383-acb5-3560f54858d0.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/2c43e289-a9c2-4b85-bebe-adf38cc13f9e.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/50551c50-7c93-45ab-a946-2c36e8ad0f7a.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/849b0e10-8790-4e46-b9d8-462fa3a2cb88.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/2ca6d38c-2069-4ecb-8493-f7024495f3f9.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/1b517f7f-b419-40fc-b814-72fb9fef44af.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/e4ca8678-2ad6-464c-9c8b-ade5059c8d20.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/2774f693-d4fd-4dbd-b235-037bbaa53048.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/1fa76c42-45d4-4371-9717-e4f57b5dd367.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/9650a1f9-9ce0-4409-956f-2f2021775abc.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/0312d688-b3da-49a4-ab4f-da224e20e223.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/a1ec0e16-2042-4309-8672-96b49f6d3303.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/34e5820d-ce1e-48fe-aedf-5a24e3471c20.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/5bb1e567-9116-448d-a91c-383393193c8b.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/8dea5ec5-be91-4b78-bc93-09ad16422d47.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/0c57f317-0fb4-4f38-a557-5159121355ab.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/02ad33fc-9cf9-44c9-8cff-d76da5a412e4.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/c5112753-c611-497d-933a-f4b2b03611bc.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/90efcb96-8679-4d94-b280-0896b7117928.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/7bde7315-d0b8-4f34-9597-7a7c50505a73.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/a22d39eb-59a2-4ee9-bd95-ab77dc132efa.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/be0c4844-408a-4c67-83d0-a70cf880f295.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/17abd76a-b673-44cd-8020-0d5dd7bbe3aa.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/27ec240f-d77e-4a10-9ebf-afc782f4b224.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/f5e20cdb-289b-46e0-8f7c-af3b7bec50b7.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/6b71c2ae-1c54-4198-891b-232426cbc91f.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/f859d121-d1ba-4d04-b3a2-73a51d663050.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/a073cc5f-15b3-4143-b4dc-67626292a17d.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/61c6dbe4-c2e7-4df0-b0e9-5212e3c5186e.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/aed152e9-f4cb-4132-99af-de7734b892bf.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/911036bf-5e8b-4c0e-96c7-6d7be1449f1f.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/4608d966-a8c3-49bc-bc2e-3ef9d24a9d4b.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/8d092cb9-7f9c-4083-b8e4-70062fee7715.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/08f87534-024b-4457-9795-d0a154829159.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/b93e6292-8e7d-4c97-995c-b6c24185ecf1.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/98e2aeba-a819-4ed7-9a47-c5228309c155.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/44562bc8-7fdd-49cb-a689-6992157b3d57.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/ed95cd3a-4f9e-41f8-b1ae-cdb92b955d27.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/8582af15-f04f-4aa8-ac1b-bc1d862a375f.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/15114e35-fe1e-4b99-9b62-ecbc6e285037.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/5b55a9f0-f138-4305-8c98-6a97a8054a41.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/9d3857d9-2dfe-45aa-abc5-8db4eee74da6.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/065a1110-78b5-4308-b62b-c873c8b5c25f.root',
        '/store/relval/CMSSW_14_0_0_pre1/RelValZMM_14/GEN-SIM-RECO/PU_133X_mcRun4_realistic_v1_2026D98PU200-v1/2590000/721867c2-bf53-4611-8736-ada0c0765b4b.root'        
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    TryToContinue = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToCallForTryToContinue = cms.untracked.vstring(),
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('stepTkAlZMuMu nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition


# Additional output definition
process.ALCARECOStreamTkAlZMuMu = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlZMuMu')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('TkAlZMuMu')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('TkAlZMuMu.root'),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep recoTracks_ALCARECOTkAlZMuMu_*_*',
        'keep recoTrackExtras_ALCARECOTkAlZMuMu_*_*',
        'keep TrackingRecHitsOwned_ALCARECOTkAlZMuMu_*_*',
        'keep SiPixelClusteredmNewDetSetVector_ALCARECOTkAlZMuMu_*_*',
        'keep L1AcceptBunchCrossings_*_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_TriggerResults_*_*',
        'keep *_offlinePrimaryVertices_*_*',
        'keep DCSRecord_onlineMetaDataDigis_*_*',
        'keep Phase2TrackerCluster1DedmNewDetSetVector_ALCARECOTkAlZMuMu_*_*'
    )
)

# Other statements
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOTkAlZMuMu_noDrop.outputCommands)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T25', '')

# Path and EndPath definitions
process.endjob_step = cms.EndPath(process.endOfProcess)
process.ALCARECOStreamTkAlZMuMuOutPath = cms.EndPath(process.ALCARECOStreamTkAlZMuMu)

# Schedule definition
process.schedule = cms.Schedule(process.pathALCARECOTkAlZMuMu,process.endjob_step,process.ALCARECOStreamTkAlZMuMuOutPath)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads = 4
process.options.numberOfStreams = 0



# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
