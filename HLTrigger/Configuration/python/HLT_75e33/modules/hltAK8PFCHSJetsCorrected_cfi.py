import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Modules.CorrectedPFJetProducer import CorrectedPFJetProducer as _CorrectedPFJetProducer

hltAK8PFCHSJetsCorrected = _CorrectedPFJetProducer(
    correctors = cms.VInputTag("hltAK8PFCHSJetCorrector"),
    src = cms.InputTag("hltAK8PFCHSJets")
)
