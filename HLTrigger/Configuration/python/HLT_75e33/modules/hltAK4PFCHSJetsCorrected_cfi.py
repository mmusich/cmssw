import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Modules.CorrectedPFJetProducer import CorrectedPFJetProducer as _CorrectedPFJetProducer

hltAK4PFCHSJetsCorrected = _CorrectedPFJetProducer(
    correctors = cms.VInputTag("hltAK4PFCHSJetCorrector"),
    src = ("hltAK4PFCHSJets")
)
