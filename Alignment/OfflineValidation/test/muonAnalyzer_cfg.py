import FWCore.ParameterSet.Config as cms

process = cms.Process("MUONANALYZER")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'

process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(-1))

process.source = cms.Source("PoolSource",
                            fileNames=cms.untracked.vstring(
                                '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/0f73e103-273c-416c-8fdd-e322aa8de063.root',
                                '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/1abd3dd2-bc65-4028-995e-9ad505672d08.root',
                                '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/1ffbad78-d003-4a61-869d-46ac2087e80c.root',
                                '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/4085c749-1d0b-4264-9a46-6ed926475a6b.root',
                                '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/560602b8-bd74-4228-bd95-a49099cc031e.root',
                                '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/59292bf8-70e0-4982-a4af-6f27370dfba8.root',
                                '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/70b39b48-f2b8-4584-b268-e464aaba3531.root',
                                '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/734e7003-ac98-462c-87c8-66dedc28fe8a.root',
                                '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/a807ed3e-e844-41b3-b6e1-ea16e6ae9632.root',
                                '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/af7f0f95-05f8-42cf-9792-0f8653c651eb.root',
                                '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/b0a8ead8-0fcd-48d5-822f-a323925b101a.root',
                                '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/b579e360-bb6a-4707-a4c9-9b01f2ce4e7d.root',
                                '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/b996f92a-73fd-4e45-9e37-20c7e86c2061.root',
                                '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/b9a33790-ba83-4715-b28f-b6c95e19c7ca.root',
                                '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/bc8feccd-4e0b-402d-8741-edcb0e7e571b.root',
                                '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/bc90c644-bb51-4488-b1d0-b42b2ec7a991.root',
                                '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/d3fecec7-889d-442a-9249-fdf2eadbd24b.root',
                                '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/d99c2acd-545b-4095-80a8-8f57e77b4551.root',
                                '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/db45efef-81c1-4da8-99d8-6e491edf0237.root')
                                #'/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/1481bfbc-fdf4-4f90-95af-6dee16531d6f.root',
                                #'/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/3b832c44-be67-42b4-bdda-96424f023a63.root',
                                #'/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/3ee69424-4178-4918-ab8c-9cb661e6adb0.root',
                                #'/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/454cd761-a6c2-4fa9-a977-03fb93d33730.root',
                                #'/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/4af59678-c8fd-47fc-bec1-6b427eadb3ed.root',
                                #'/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/750e1f66-c169-48be-ac22-4660d5a632b1.root',
                                #'/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/75187b62-cee5-4569-9ffb-44f5fd7a1bda.root',
                                #'/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/857bed3a-d752-4b53-a37b-43dd3ce97603.root',
                                #'/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/a3045d82-ea23-49c8-9e6a-469298ed763d.root',
                                #'/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/c0d6470a-9d11-4870-bd63-eaec2d68ab42.root',
                                #'/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/d5674a0e-f501-4b59-8564-af48a1e35617.root',
                                #'/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/d8af002a-53e3-4b24-98ee-985ee2a43af9.root',
                                #'/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/e5d7219d-b834-458f-bd48-3c71d1baa385.root',
                                #'/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/e9d5b345-9984-49c5-8bf9-6d4a27a35db0.root',
                                #'/store/relval/CMSSW_14_0_0_pre2/RelValZMM_14/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU-v2/2590000/fe8b47e9-be5d-4518-9925-12359ac92400.root')
                            )

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string('muonAnalyzerOutput_SingleMu.root')
                                   )

process.muonAnalyzer = cms.EDAnalyzer("MuonAnalyzer",
                                     muonCollection=cms.InputTag("muons")
                                     )

process.p = cms.Path(process.muonAnalyzer)
