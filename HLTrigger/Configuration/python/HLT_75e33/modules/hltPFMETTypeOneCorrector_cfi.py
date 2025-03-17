import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Type1MET.PFJetMETcorrInputProducer import PFJetMETcorrInputProducer as _PFJetMETcorrInputProducer

hltPFMETTypeOneCorrector = _PFJetMETcorrInputProducer(
    jetCorrEtaMax = 9.9,
    jetCorrLabel = ("hltAK4PFCHSJetCorrector"),
    jetCorrLabelRes = ("hltAK4PFCHSJetCorrector"),
    offsetCorrLabel = ("hltAK4PFCHSJetCorrectorL1"),
    skipEM = True,
    skipEMfractionThreshold = 0.9,
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = True,
    src = ("hltAK4PFCHSJets"),
    type1JetPtThreshold = 30.0
)
