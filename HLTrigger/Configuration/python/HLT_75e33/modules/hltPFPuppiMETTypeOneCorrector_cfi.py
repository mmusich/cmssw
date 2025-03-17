import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Type1MET.PFJetMETcorrInputProducer import PFJetMETcorrInputProducer as _PFJetMETcorrInputProducer

hltPFPuppiMETTypeOneCorrector = _PFJetMETcorrInputProducer(
    jetCorrEtaMax = 9.9,
    jetCorrLabel = ("hltAK4PFPuppiJetCorrector"),
    jetCorrLabelRes = ("hltAK4PFPuppiJetCorrector"),
    offsetCorrLabel = ("hltAK4PFPuppiJetCorrectorL1"),
    skipEM = True,
    skipEMfractionThreshold = 0.9,
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = True,
    src = ("hltAK4PFPuppiJets"),
    type1JetPtThreshold = 30.0
)
