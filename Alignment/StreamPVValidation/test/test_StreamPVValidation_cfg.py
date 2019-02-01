import FWCore.ParameterSet.Config as cms
import sys
 
isDA = True
isMC = False
allFromGT = False
applyBows = False
applyExtraConditions = False

process = cms.Process("PrimaryVertexValidation") 

###################################################################
def customiseAlignmentAndAPE(process):
###################################################################
    if not hasattr(process.GlobalTag,'toGet'):
        process.GlobalTag.toGet=cms.VPSet()
    process.GlobalTag.toGet.extend( cms.VPSet(cms.PSet(record = cms.string("TrackerAlignmentRcd"),
                                                       tag = cms.string("TrackerAlignment_PCL_byRun_v2_express"),
                                                       connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                                                       ),
                                              cms.PSet(record = cms.string("TrackerAlignmentErrorExtendedRcd"),
                                                       tag = cms.string("TrackerAlignmentExtendedErr_2009_v2_express_IOVs"),
                                                       connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                                                       )
                                              )
                                    )
    return process

###################################################################
def customiseKinksAndBows(process):
###################################################################
     if not hasattr(process.GlobalTag,'toGet'):
          process.GlobalTag.toGet=cms.VPSet()
     process.GlobalTag.toGet.extend(cms.VPSet(cms.PSet(record = cms.string("TrackerSurfaceDeformationRcd"),
                                                       tag = cms.string("TrackerSurafceDeformations_v1_express"),
                                                       connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                                                       ),        
                                              )
                                    )

     return process

###################################################################
# Event source and run selection
###################################################################
readFiles = cms.untracked.vstring()
readFiles.extend(['/store/data/Run2018D/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/321/833/00000/B64AF9B1-B5AE-E811-A825-02163E015C4D.root',
                  '/store/data/Run2018D/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/321/833/00000/AE811201-B5AE-E811-90CE-FA163E85DB9B.root',
                  '/store/data/Run2018D/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/321/833/00000/EA4F2A84-B5AE-E811-934E-02163E010C06.root',
                  '/store/data/Run2018D/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/321/833/00000/A042AEC1-B4AE-E811-8852-FA163ED0943D.root',
                  '/store/data/Run2018D/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/321/833/00000/B2410A14-B4AE-E811-B2FF-02163E010CCE.root'])

# readFiles.extend(['/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_113.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_77.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_68.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_50.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_35.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_42.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_89.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_80.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_82.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_44.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_9.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_2.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_130.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_133.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_115.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_64.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_43.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_47.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_72.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_122.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_73.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_120.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_109.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_121.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_24.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_97.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_93.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_3.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_118.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_34.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_22.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_101.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_70.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_67.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_40.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_8.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_39.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_12.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_92.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_19.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_104.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_27.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_131.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_49.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_78.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_86.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_87.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_94.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_55.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_125.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_30.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_45.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_69.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_54.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_66.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_52.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_48.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_1.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_36.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_7.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_21.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_41.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_90.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_124.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_65.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_11.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_20.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_85.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_117.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_4.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_88.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_17.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_76.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_91.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_126.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_132.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_13.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_129.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_114.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_33.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_46.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_116.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_95.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_127.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_84.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_103.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_99.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_5.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_31.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_128.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_100.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_106.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_56.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_51.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_58.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_10.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_14.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_37.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_107.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_57.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_53.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_23.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_25.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_28.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_38.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_112.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_18.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_29.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_32.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_110.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_62.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_74.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_83.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_71.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_119.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_15.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_81.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_61.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_60.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_102.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_105.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_111.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_79.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_6.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_26.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_59.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_96.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_16.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_75.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_98.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_108.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_123.root',
#                   '/store/user/tvami/Monitoring/HLTPhysics/crab_2018pp_HLTPhysics_Run321833_with2DON_HighPrio_v1/190129_125126/0000/TkAlMinBias_63.root'])

process.source = cms.Source("PoolSource",
                            fileNames = readFiles ,
                            duplicateCheckMode = cms.untracked.string('checkAllFilesOpened'),
                            inputCommands=cms.untracked.vstring('keep *',
                                                                'drop CTPPSDiamondRecHitedmDetSetVector_ctppsDiamondRecHits__RECO'
                                                                )
                            )


process.options = cms.untracked.PSet(
    numberOfThreads = cms.untracked.uint32(4)
    )

#process.load("Alignment.OfflineValidation.DATASETTEMPLATE");
runboundary = 321833
process.source.firstRun = cms.untracked.uint32(int(runboundary))
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

###################################################################
# JSON Filtering
###################################################################
if isMC:
     print ">>>>>>>>>> testPVValidation_cfg.py: msg%-i: This is Simulation!"
     runboundary = 1
else:
     print ">>>>>>>>>> testPVValidation_cfg.py: msg%-i: This is DATA!"
     import FWCore.PythonUtilities.LumiList as LumiList
     process.source.lumisToProcess = LumiList.LumiList(filename ='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/DCSOnly/json_DCSONLY.txt').getVLuminosityBlockRange()

###################################################################
# Messages
###################################################################
#process.load("FWCore.MessageService.MessageLogger_cfi")
#process.MessageLogger.destinations = ['cout', 'cerr']
#process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.load('FWCore.MessageService.MessageLogger_cfi')

# Activate LogVerbatim output in FilterOutLowPt (needs to be a edm::one:Filter)
process.MessageLogger.categories.append("FilterOutLowPt")
process.MessageLogger.categories.append("PrimaryVertexValidation")

process.MessageLogger.destinations = cms.untracked.vstring("cout")
process.MessageLogger.cout = cms.untracked.PSet(
    threshold = cms.untracked.string("INFO"),
    default   = cms.untracked.PSet(limit = cms.untracked.int32(0)),
    FwkReport = cms.untracked.PSet(limit = cms.untracked.int32(-1),
                                   reportEvery = cms.untracked.int32(1000)
                                   ),
    FilterOutLowPt = cms.untracked.PSet( limit = cms.untracked.int32(-1) ),
    PrimaryVertexValidation = cms.untracked.PSet( limit = cms.untracked.int32(-1) )
    )

process.MessageLogger.statistics.append('cout')

####################################################################
# Produce the Transient Track Record in the event
####################################################################
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")

####################################################################
# Get the Magnetic Field
####################################################################
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')

###################################################################
# Standard loads
###################################################################
process.load("Configuration.Geometry.GeometryRecoDB_cff")

####################################################################
# Get the BeamSpot
####################################################################
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")

####################################################################
# Get the GlogalTag
####################################################################
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, '104X_dataRun2_pixel2DTemplate_Cand_v1', '')
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_dataRun2_Prompt_v7', '')

if allFromGT:
     print ">>>>>>>>>> testPVValidation_cfg.py: msg%-i: All is taken from GT"
else:
     ####################################################################
     # Get Alignment constants and APE
     ####################################################################
     process=customiseAlignmentAndAPE(process)

     ####################################################################
     # Kinks and Bows (optional)
     ####################################################################
     if applyBows:
          print ">>>>>>>>>> testPVValidation_cfg.py: msg%-i: Applying TrackerSurfaceDeformations!"
          process=customiseKinksAndBows(process)
     else:
          print ">>>>>>>>>> testPVValidation_cfg.py: msg%-i: MultiPVValidation: Not applying TrackerSurfaceDeformations!"

     ####################################################################
     # Extra corrections not included in the GT
     ####################################################################
     if applyExtraConditions:
          print ">>>>>>>>>> testPVValidation_cfg.py: msg%-i: Applying Extra conditions!"

          import CalibTracker.Configuration.Common.PoolDBESSource_cfi
 
          process.conditionsInSiPixelTemplateDBObjectRcd= CalibTracker.Configuration.Common.PoolDBESSource_cfi.poolDBESSource.clone( 
              connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'), 
              toGet = cms.VPSet(cms.PSet(record = cms.string('SiPixelTemplateDBObjectRcd'), 
                                         tag = cms.string('SiPixelTemplateDBObject_38T_v13_offline'), 
                                         ) 
                                ) 
              ) 
          process.prefer_conditionsInSiPixelTemplateDBObjectRcd = cms.ESPrefer("PoolDBESSource", "conditionsInSiPixelTemplateDBObjectRcd") 
 
 
          process.conditionsInSiPixel2DTemplateDBObjectRcd= CalibTracker.Configuration.Common.PoolDBESSource_cfi.poolDBESSource.clone( 
              connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'), 
              toGet = cms.VPSet(cms.PSet(record = cms.string('SiPixel2DTemplateDBObjectRcd'), 
                                         tag = cms.string('SiPixel2DTemplateDBObject_38T_v1_offline'), 
                                         ),
                                cms.PSet(record = cms.string('SiPixel2DTemplateDBObjectRcd'), 
                                         label = cms.untracked.string('numerator'),
                                         tag = cms.string('SiPixel2DTemplateDBObject_38T_v1_offline'), 
                                         ) 
                                ) 
              ) 
          process.prefer_conditionsInSiPixel2DTemplateDBObjectRcd = cms.ESPrefer("PoolDBESSource", "conditionsInSiPixel2DTemplateDBObjectRcd") 
 
          ##### END OF EXTRA CONDITIONS
 
     else:
          print ">>>>>>>>>> testPVValidation_cfg.py: msg%-i: Not applying extra calibration constants!"
     
####################################################################
# Load and Configure event selection
####################################################################
process.primaryVertexFilter = cms.EDFilter("VertexSelector",
                                             src = cms.InputTag("offlinePrimaryVertices"),
                                             cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2"),
                                             filter = cms.bool(True)
                                             )

process.noscraping = cms.EDFilter("FilterOutScraping",
                                  applyfilter = cms.untracked.bool(True),
                                  src =  cms.untracked.InputTag("ALCARECOTkAlMinBias"),
                                  debugOn = cms.untracked.bool(False),
                                  numtrack = cms.untracked.uint32(10),
                                  thresh = cms.untracked.double(0.25)
                                  )

process.load("Alignment.CommonAlignment.filterOutLowPt_cfi")
process.filterOutLowPt.applyfilter = True
process.filterOutLowPt.src = "ALCARECOTkAlMinBias"
process.filterOutLowPt.numtrack = 0
process.filterOutLowPt.thresh = 1
process.filterOutLowPt.ptmin  = 3.0
process.filterOutLowPt.runControl = True
process.filterOutLowPt.runControlNumber = [runboundary]

if isMC:
     process.goodvertexSkim = cms.Sequence(process.noscraping+process.filterOutLowPt)
else:
     process.goodvertexSkim = cms.Sequence(process.primaryVertexFilter + process.noscraping + process.filterOutLowPt)

####################################################################
# Load and Configure Measurement Tracker Event
# (this would be needed in case NavigationSchool is set != from ''
####################################################################
# process.load("RecoTracker.MeasurementDet.MeasurementTrackerEventProducer_cfi") 
# process.MeasurementTrackerEvent.pixelClusterProducer = 'ALCARECOTkAlMinBias'
# process.MeasurementTrackerEvent.stripClusterProducer = 'ALCARECOTkAlMinBias'
# process.MeasurementTrackerEvent.inactivePixelDetectorLabels = cms.VInputTag()
# process.MeasurementTrackerEvent.inactiveStripDetectorLabels = cms.VInputTag()

####################################################################
# Load and Configure TrackRefitter
####################################################################
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
import RecoTracker.TrackProducer.TrackRefitters_cff
process.FinalTrackRefitter = RecoTracker.TrackProducer.TrackRefitter_cfi.TrackRefitter.clone()
process.FinalTrackRefitter.src = "ALCARECOTkAlMinBias"
process.FinalTrackRefitter.TrajectoryInEvent = True
process.FinalTrackRefitter.NavigationSchool = ''
process.FinalTrackRefitter.TTRHBuilder = "WithAngleAndTemplate"
#process.FinalTrackRefitter.TTRHBuilder = "WithTrackAngle"

####################################################################
# Activate Cluster Repair in the refit
####################################################################
#process.TTRHBuilderAngleAndTemplate.PixelCPE = cms.string('PixelCPEClusterRepair')

####################################################################
## Refit the vertex collection
####################################################################
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")

from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import offlinePrimaryVertices 
process.offlinePrimaryVerticesFromRefittedTrks = offlinePrimaryVertices.clone()
process.offlinePrimaryVerticesFromRefittedTrks.TrackLabel                                       = cms.InputTag("FinalTrackRefitter") 
process.offlinePrimaryVerticesFromRefittedTrks.vertexCollections.maxDistanceToBeam              = 1
process.offlinePrimaryVerticesFromRefittedTrks.TkFilterParameters.maxNormalizedChi2             = 20
process.offlinePrimaryVerticesFromRefittedTrks.TkFilterParameters.minSiliconLayersWithHits      = 5
process.offlinePrimaryVerticesFromRefittedTrks.TkFilterParameters.maxD0Significance             = 5.0 
process.offlinePrimaryVerticesFromRefittedTrks.TkFilterParameters.minPixelLayersWithHits        = 2 

####################################################################
# Load and Configure common selection sequence
####################################################################
# import Alignment.CommonAlignment.tools.trackselectionRefitting as trackselRefit
# process.seqTrackselRefit = trackselRefit.getSequence(process,'ALCARECOTkAlMinBias')
# process.HighPurityTrackSelector.trackQualities = cms.vstring()
# process.HighPurityTrackSelector.pMin     = cms.double(0.)                                                                          
# process.AlignmentTrackSelector.pMin      = cms.double(0.)  
# process.AlignmentTrackSelector.ptMin     = cms.double(0.)
# process.AlignmentTrackSelector.nHitMin2D = cms.uint32(0)
# process.AlignmentTrackSelector.nHitMin   = cms.double(0.)
# process.AlignmentTrackSelector.d0Min     = cms.double(-999999.0)
# process.AlignmentTrackSelector.d0Max     = cms.double(+999999.0)                  
# process.AlignmentTrackSelector.dzMin     = cms.double(-999999.0)
# process.AlignmentTrackSelector.dzMax     = cms.double(+999999.0)  

####################################################################
# Output file
####################################################################
process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("testing_PromptReco_PromptGT.root")
                                   )                                    

####################################################################
# Deterministic annealing clustering
####################################################################
if isDA:
     print ">>>>>>>>>> testPVValidation_cfg.py: msg%-i: Running DA Algorithm!"
     process.PVValidation = cms.EDAnalyzer("PrimaryVertexValidation",
                                           TrackCollectionTag = cms.InputTag("FinalTrackRefitter"),
                                           VertexCollectionTag = cms.InputTag("offlinePrimaryVertices"),  
                                           Debug = cms.bool(False),
                                           storeNtuple = cms.bool(False),
                                           useTracksFromRecoVtx = cms.bool(False),
                                           isLightNtuple = cms.bool(True),
                                           askFirstLayerHit = cms.bool(False),
                                           probePt = cms.untracked.double(3.0),
                                           intLumi = cms.untracked.double(1),
                                           runControl = cms.untracked.bool(True),
                                           runControlNumber = cms.untracked.vuint32(int(runboundary)),
                                           
                                           TkFilterParameters = cms.PSet(algorithm=cms.string('filter'),                           
                                                                         maxNormalizedChi2 = cms.double(5.0),                        # chi2ndof < 5                  
                                                                         minPixelLayersWithHits = cms.int32(2),                      # PX hits > 2                       
                                                                         minSiliconLayersWithHits = cms.int32(5),                    # TK hits > 5  
                                                                         maxD0Significance = cms.double(5.0),                        # fake cut (requiring 1 PXB hit)     
                                                                         minPt = cms.double(0.0),                                    # better for softish events                        
                                                                         trackQuality = cms.string("any")
                                                                         ),
                                           
                                           TkClusParameters=cms.PSet(algorithm=cms.string('DA'),
                                                                     TkDAClusParameters = cms.PSet(coolingFactor = cms.double(0.8),  # moderate annealing speed
                                                                                                   Tmin = cms.double(4.),            # end of annealing
                                                                                                   vertexSize = cms.double(0.05),    # ~ resolution / sqrt(Tmin)
                                                                                                   d0CutOff = cms.double(3.),        # downweight high IP tracks
                                                                                                   dzCutOff = cms.double(4.)         # outlier rejection after freeze-out (T<Tmin)
                                                                                                   )
                                                                     )
                                           )

####################################################################
# GAP clustering
####################################################################
else:
     print ">>>>>>>>>> testPVValidation_cfg.py: msg%-i: Running GAP Algorithm!"
     process.PVValidation = cms.EDAnalyzer("PrimaryVertexValidation",
                                           TrackCollectionTag = cms.InputTag("FinalTrackRefitter"),
                                           VertexCollectionTag = cms.InputTag("offlinePrimaryVertices"), 
                                           Debug = cms.bool(False),
                                           isLightNtuple = cms.bool(True),
                                           storeNtuple = cms.bool(False),
                                           useTracksFromRecoVtx = cms.bool(False),
                                           askFirstLayerHit = cms.bool(False),
                                           probePt = cms.untracked.double(3.0),
                                           intLumi = cms.untracked.double(1),
                                           runControl = cms.untracked.bool(True),
                                           runControlNumber = cms.untracked.vuint32(int(runboundary)),
                                           
                                           TkFilterParameters = cms.PSet(algorithm=cms.string('filter'),                             
                                                                         maxNormalizedChi2 = cms.double(5.0),                        # chi2ndof < 20                  
                                                                         minPixelLayersWithHits=cms.int32(2),                        # PX hits > 2                   
                                                                         minSiliconLayersWithHits = cms.int32(5),                    # TK hits > 5                   
                                                                         maxD0Significance = cms.double(5.0),                        # fake cut (requiring 1 PXB hit)
                                                                         minPt = cms.double(0.0),                                    # better for softish events     
                                                                         trackQuality = cms.string("any")
                                                                         ),
                                        
                                           TkClusParameters = cms.PSet(algorithm   = cms.string('gap'),
                                                                       TkGapClusParameters = cms.PSet(zSeparation = cms.double(0.2)  # 0.2 cm max separation betw. clusters
                                                                                                      ) 
                                                                       )
                                           )

####################################################################
# Analysis
####################################################################
# process.fastpv = cms.EDAnalyzer('FastPVValidator',
#                                 TrackCollection  = cms.InputTag("FinalTrackRefitter"),
#                                 VertexCollection = cms.InputTag("offlinePrimaryVertices"),
#                                 #VertexCollection  = cms.InputTag("offlinePrimaryVerticesFromRefittedTrks")
#                                 minVertexNdf        = cms.untracked.double(10.),
#                                 minVertexMeanWeight = cms.untracked.double(0.5),
#                                 useMatched          = cms.untracked.bool(False),
#                                 applyVertexQuality  = cms.untracked.bool(False)
#                                 )                                                                                  

# process.errorScaleCal = cms.EDAnalyzer('errorScaleCal',
#                                        vtxCollection    	= cms.InputTag("offlinePrimaryVerticesFromRefittedTrks"),
#                                        trackCollection		= cms.InputTag("FinalTrackRefitter"),		
#                                        minVertexNdf        = cms.untracked.double(10.),
#                                        minVertexMeanWeight = cms.untracked.double(0.5)
#                                        )

process.streamPVValidation = cms.EDAnalyzer('StreamPVValidation',
                                            tagVertices = cms.untracked.InputTag("offlinePrimaryVerticesFromRefittedTrks")
                                            )

####################################################################
# Path
####################################################################
process.p = cms.Path(process.goodvertexSkim*
                     process.offlineBeamSpot*
                     #process.seqTrackselRefit*
                     # in case the navigation shool is removed
                     #process.MeasurementTrackerEvent*
                     # in case the common refitting sequence is removed
                     process.FinalTrackRefitter*
                     #process.PVValidation
                     process.offlinePrimaryVerticesFromRefittedTrks*
                     #process.fastpv
                     process.streamPVValidation
                     #*process.errorScaleCal
                     )
