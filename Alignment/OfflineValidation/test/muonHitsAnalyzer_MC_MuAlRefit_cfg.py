import FWCore.ParameterSet.Config as cms


process = cms.Process("Demo")

# input taken from https://twiki.cern.ch/twiki/bin/viewauth/CMS/MuAlSamplesMC
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring("root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_100_1_kAB.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_101_1_eD7.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_102_1_f4D.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_103_1_rxe.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_104_1_M11.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_105_1_WR0.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_106_1_mrd.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_107_1_arj.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_108_1_xEk.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_109_1_AQf.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_10_1_oyF.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_110_1_qHJ.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_111_1_ITg.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_112_1_UOg.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_113_1_RPT.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_114_1_LBL.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_115_1_xaM.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_116_1_o4H.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_117_1_XyT.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_118_1_hVi.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_119_1_cwj.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_11_1_mr5.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_120_1_2JQ.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_121_1_lcq.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_122_1_CzD.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_123_1_pTc.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_124_1_rbN.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_125_1_LTf.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_126_1_iGl.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_127_1_MsH.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_128_1_hV8.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_129_1_pQE.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_12_1_QPD.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_130_1_2bk.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_131_1_1A7.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_132_1_otm.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_133_1_Ogb.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_134_1_8bU.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_135_1_u5m.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_136_1_o8H.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_137_1_up8.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_138_1_2TH.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_139_1_a5E.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_13_1_mA8.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_140_1_Lnt.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_141_1_fqp.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_142_1_LVP.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_143_1_iq2.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_144_1_Cpo.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_145_1_fCT.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_146_1_WSz.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_147_1_a1o.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_148_1_dS5.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_149_1_shB.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_14_1_199.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_150_1_Hf5.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_151_1_cdX.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_15_1_eLW.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_16_1_bxr.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_17_1_BGA.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_18_1_7EZ.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_19_1_p0N.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_1_1_rAu.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_20_1_HKr.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_21_1_DiT.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_22_1_uhz.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_23_1_dRc.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_24_1_fbR.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_25_1_Tjg.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_26_1_Ym1.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_27_1_5QF.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_28_1_v58.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_29_1_aRK.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_2_1_svF.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_30_1_uy9.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_31_1_Xig.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_32_1_zfE.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_33_1_wv6.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_34_1_kBn.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_35_1_CKh.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_36_1_skG.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_37_1_ZNh.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_38_1_T0W.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_39_1_Cj6.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_3_1_6s1.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_40_1_k1d.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_41_1_vmW.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_42_1_WBd.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_43_1_IMF.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_44_1_GA5.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_45_1_8UB.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_46_1_LN8.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_47_1_8se.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_48_1_ZKe.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_49_1_Osp.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_4_1_Y2B.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_50_1_IE5.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_51_1_4f5.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_52_1_UvF.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_53_1_Jir.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_54_1_ryY.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_55_1_2Jt.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_56_1_Cby.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_57_1_G7P.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_58_1_KYp.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_59_1_cz2.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_5_1_PvK.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_60_1_S3Q.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_61_1_WMs.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_62_1_5zg.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_63_1_3CL.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_64_1_72E.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_65_1_nNa.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_66_1_fp7.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_67_1_VPz.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_68_1_p3B.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_69_1_u2z.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_6_1_TWD.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_70_1_CVD.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_71_1_f4r.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_72_1_pQY.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_73_1_MNa.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_74_1_ZW6.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_75_1_X4W.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_76_1_Kl1.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_77_1_T5V.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_78_1_HtJ.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_79_1_uzc.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_7_1_ojS.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_80_1_AJk.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_81_1_GGz.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_82_1_Gli.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_83_1_TZj.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_84_1_LVR.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_85_1_oce.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_86_1_zus.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_87_1_jTZ.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_88_1_xRC.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_89_1_sL5.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_8_1_QyY.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_90_1_637.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_91_1_wyI.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_92_1_CwG.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_93_1_AAE.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_94_1_7py.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_95_1_du4.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_96_1_Faj.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_97_1_4vQ.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_98_1_r5j.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_99_1_kjP.root",
                                                              "root://eoscms//eos/cms/store/caf/user/pakhotin/singleMuonGun_RECO_v4/singleMuonGun_RECO_v4_Consolidated_v3/8f04993aadaf700f87a5ec0188006dcc/singleMuonGun_RECO_Consolidated_9_1_fvD.root"
    
  
    
                                                              )
                            )


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100))

process.MessageLogger = cms.Service("MessageLogger",
                                    destinations = cms.untracked.vstring("cout"),
                                    cout = cms.untracked.PSet(threshold = cms.untracked.string("INFO")))

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.GlobalTag.globaltag = "GR_R_53_V16A::All"
process.GlobalTag.globaltag = "START53_V14::All"

# this line works after 53x
process.load("Configuration.Geometry.GeometryIdeal_cff")
# this line works before 53x
#process.load("Configuration.StandardSequences.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")

process.load("RecoTracker.TrackProducer.TrackRefitter_cfi")

process.muAlGeneralTracks = process.TrackRefitter.clone()

process.muAlAncientMuonSeed = process.ancientMuonSeed.clone()

process.muAlStandAloneMuons = process.standAloneMuons.clone()
# this line switch on "old" hit based muon reconstruction
#process.muAlStandAloneMuons.STATrajBuilderParameters.BWFilterParameters.MuonTrajectoryUpdatorParameters.Granularity = 2
process.muAlStandAloneMuons.InputObjects = cms.InputTag("muAlAncientMuonSeed")

process.muAlGlobalMuons = process.globalMuons.clone()
process.muAlGlobalMuons.TrackerCollectionLabel = cms.InputTag("muAlGeneralTracks")
process.muAlGlobalMuons.MuonCollectionLabel = cms.InputTag("muAlStandAloneMuons","UpdatedAtVtx")

process.muAlTevMuons = process.tevMuons.clone()
process.muAlTevMuons.MuonCollectionLabel = cms.InputTag("muAlGlobalMuons")

process.muAlGlbTrackQual = process.glbTrackQual.clone()
process.muAlGlbTrackQual.InputCollection = cms.InputTag("muAlGlobalMuons")
process.muAlGlbTrackQual.InputLinksCollection = cms.InputTag("muAlGlobalMuons")

process.muAlMuons = process.muons1stStep.clone()
process.muAlMuons.inputCollectionTypes = cms.vstring('inner tracks','links','outer tracks','tev firstHit','tev picky','tev dyt')
process.muAlMuons.inputCollectionLabels = cms.VInputTag( cms.InputTag("muAlGeneralTracks"),
                                                         cms.InputTag("muAlGlobalMuons"),
                                                         cms.InputTag("muAlStandAloneMuons","UpdatedAtVtx"),
                                                         cms.InputTag("muAlTevMuons","firstHit"),
                                                         cms.InputTag("muAlTevMuons","picky"),
                                                         cms.InputTag("muAlTevMuons","dyt")
                                                       )

process.muAlMuons.fillGlobalTrackQuality = cms.bool(True)
process.muAlMuons.globalTrackQualityInputTag = cms.InputTag('muAlGlbTrackQual')
#process.muAlMuons.fillGlobalTrackRefits = cms.bool(False)

# This is to load new CondDB
from CondCore.DBCommon.CondDBSetup_cfi import *

# Tracker alignment record
process.TrackerAlignmentInputDB = cms.ESSource("PoolDBESSource",
                                               CondDBSetup,
                                               connect = cms.string('sqlite_file:/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/mp1382/jobData/jobm1/alignments_MP.db'),
                                               toGet = cms.VPSet(cms.PSet(record = cms.string("TrackerAlignmentRcd"),
                                                                          tag = cms.string('Alignments')
                                                                          )
                                                                 )
                                               )

process.es_prefer_TrackerAlignmentInputDB = cms.ESPrefer("PoolDBESSource", "TrackerAlignmentInputDB")

process.TrackerSurfaceDeformationInputDB = cms.ESSource("PoolDBESSource",
                                                        CondDBSetup,
                                                        connect = cms.string('sqlite_file:/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/mp1382/jobData/jobm1/alignments_MP.db'),
                                                        toGet = cms.VPSet(cms.PSet(cms.PSet(record = cms.string("TrackerSurfaceDeformationRcd"),
                                                                                            tag = cms.string('Deformations')
                                                                                            )
                                                                                   )
                                                                          )
                                                        )

process.es_prefer_TrackerSurfaceDeformationInputDB = cms.ESPrefer("PoolDBESSource", "TrackerSurfaceDeformationInputDB")

#--------------%<----------------------
# New pixel fo mp1375 Tracker alignment candidate - add the fragment below to gather_cfg.py
# --------------%<----------------------
from CondCore.DBCommon.CondDBSetup_cfi import *
process.myPixelTemplate = cms.ESSource("PoolDBESSource",
                                       CondDBSetup,
                                       connect = cms.string("frontier://FrontierProd/CMS_COND_31X_PIXEL"),
                                       toGet = cms.VPSet(cms.PSet(record = cms.string("SiPixelTemplateDBObjectRcd"),
                                                                  tag = cms.string("SiPixelTemplates38T_2010_2011_mc")
                                                                  )
                                                         )
                                       )

process.es_prefer_myPixelTemplate = cms.ESPrefer("PoolDBESSource","myPixelTemplate")

process.MuonHitsAnalyzer = cms.EDAnalyzer("MuonHitsAnalyzer",
                                          tracksTag      = cms.InputTag("globalMuons"),
                                          muonsTag       = cms.InputTag("muAlMuons"),
                                          minTrackPt     = cms.double(20.),
                                          minTrackEta    = cms.double(-2.4),
                                          maxTrackEta    = cms.double(2.4),
                                          minTrackerHits = cms.int32(10),
                                          )

process.ChamberFilter = cms.EDFilter("ChamberFilter",
                                     tracksTag      = cms.InputTag("globalMuons"),
                                     minTrackPt     = cms.double(30.),
                                     minTrackEta    = cms.double(-2.4),
                                     maxTrackEta    = cms.double(2.4),
                                     minTrackerHits = cms.int32(10),
                                     minDTHits      = cms.int32(1),
                                     minCSCHits     = cms.int32(1)
                                     )

process.p = cms.Path(process.muAlGeneralTracks *
                     process.muAlAncientMuonSeed *
                     process.muAlStandAloneMuons *
                     process.muAlGlobalMuons *
                     process.muAlTevMuons *
                     process.muAlGlbTrackQual *
                     process.muAlMuons *
                     process.ChamberFilter)
                     #*process.MuonHitsAnalyzer)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("histo.root")
                                   )
