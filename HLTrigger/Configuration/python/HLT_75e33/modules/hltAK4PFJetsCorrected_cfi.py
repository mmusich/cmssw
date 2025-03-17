import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Modules.CorrectedPFJetProducer import CorrectedPFJetProducer as _CorrectedPFJetProducer

hltAK4PFJetsCorrected = _CorrectedPFJetProducer(
    correctors = cms.VInputTag("hltAK4PFJetCorrector"),
    src = ("hltAK4PFJets")
)
