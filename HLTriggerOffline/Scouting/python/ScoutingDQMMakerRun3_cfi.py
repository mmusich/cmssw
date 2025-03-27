import FWCore.ParameterSet.Config as cms
from DQMServices.Core.DQMEDAnalyzer import DQMEDAnalyzer


L1Info = ["L1_DoubleMu_12_5","L1_DoubleMu_15_7","L1_DoubleMu4p5er2p0_SQ_OS_Mass_Min7","L1_DoubleMu4p5er2p0_SQ_OS_Mass_7to18","L1_DoubleMu8_SQ","L1_DoubleMu0er1p4_SQ_OS_dEta_Max1p2","L1_DoubleMu4er2p0_SQ_OS_dR_Max1p6","L1_DoubleMu5_SQ_OS_dR_Max1p6","L1_DoubleMu3er2p0_SQ_OS_dR_Max1p6","L1_DoubleMu0er1p5_SQ_OS_dEta_Max1p2","L1_DoubleMu0er2p0_SQ_OS_dEta_Max1p6","L1_DoubleMu0er1p4_OQ_OS_dEta_Max1p6","L1_DoubleMu0er2p0_SQ_OS_dEta_Max1p5","L1_DoubleMu0er1p4_SQ_OS_dR_Max1p4","L1_DoubleMu0er1p5_SQ_OS_dR_Max1p4","L1_DoubleMu4p5_SQ_OS_dR_Max1p2","L1_DoubleMu4_SQ_OS_dR_Max1p2","L1_DoubleMu0_Upt15_Upt7","L1_DoubleMu0_Upt6_IP_Min1_Upt4","L1_DoubleMu6_Upt6_SQ_er2p0","L1_DoubleMu7_Upt7_SQ_er2p0","L1_DoubleMu8_Upt8_SQ_er2p0","L1_DoubleMu0er2p0_SQ_dEta_Max1p6","L1_DoubleMu0er2p0_SQ_dEta_Max1p5"]

scoutingDQMMakerRun3 = DQMEDAnalyzer('ScoutingDQMMakerRun3',
                                      triggerresults   = cms.InputTag("TriggerResults", "", "HLT"),
                                      ReadPrescalesFromFile = cms.bool( False ),
                                      AlgInputTag       = cms.InputTag("gtStage2Digis"),
                                      l1tAlgBlkInputTag = cms.InputTag("gtStage2Digis"),
                                      l1tExtBlkInputTag = cms.InputTag("gtStage2Digis"),
                                      doL1 = cms.bool( True ),
                                      l1Seeds           = cms.vstring(L1Info),
                                      muons             = cms.InputTag("hltScoutingMuonPackerNoVtx"),
                                      electrons         = cms.InputTag("hltScoutingEgammaPacker"),
                                      photons           = cms.InputTag("hltScoutingEgammaPacker"),
                                      pfcands           = cms.InputTag("hltScoutingPFPacker"),
                                      pfjets            = cms.InputTag("hltScoutingPFPacker"),
                                      tracks            = cms.InputTag("hltScoutingTrackPacker"),
                                      primaryVertices   = cms.InputTag("hltScoutingPrimaryVertexPacker","primaryVtx"),
                                      displacedVertices = cms.InputTag("hltScoutingMuonPackerNoVtx","displacedVtx"),
                                      pfMet             = cms.InputTag("hltScoutingPFPacker","pfMetPt"),
                                      pfMetPhi          = cms.InputTag("hltScoutingPFPacker","pfMetPhi"),
                                      rho               = cms.InputTag("hltScoutingPFPacker","rho"),
                                  )

