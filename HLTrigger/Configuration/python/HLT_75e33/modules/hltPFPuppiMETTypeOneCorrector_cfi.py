import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Type1MET.PFJetMETcorrInputProducer import PFJetMETcorrInputProducer as _PFJetMETcorrInputProducer

hltPFPuppiMETTypeOneCorrector = _PFJetMETcorrInputProducer(
    jetCorrEtaMax = cms.double(9.9),
    jetCorrLabel = cms.InputTag("hltAK4PFPuppiJetCorrector"),
    jetCorrLabelRes = cms.InputTag("hltAK4PFPuppiJetCorrector"),
    offsetCorrLabel = cms.InputTag("hltAK4PFPuppiJetCorrectorL1"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("hltAK4PFPuppiJets"),
    type1JetPtThreshold = cms.double(30.0)
)
