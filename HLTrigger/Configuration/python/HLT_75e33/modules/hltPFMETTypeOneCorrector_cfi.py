import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Type1MET.PFJetMETcorrInputProducer import PFJetMETcorrInputProducer as _PFJetMETcorrInputProducer

hltPFMETTypeOneCorrector = _PFJetMETcorrInputProducer(
    jetCorrEtaMax = cms.double(9.9),
    jetCorrLabel = cms.InputTag("hltAK4PFCHSJetCorrector"),
    jetCorrLabelRes = cms.InputTag("hltAK4PFCHSJetCorrector"),
    offsetCorrLabel = cms.InputTag("hltAK4PFCHSJetCorrectorL1"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("hltAK4PFCHSJets"),
    type1JetPtThreshold = cms.double(30.0)
)
