import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Modules.CorrectedPFJetProducer import CorrectedPFJetProducer as _CorrectedPFJetProducer

hltAK4PFPuppiJetsCorrected = _CorrectedPFJetProducer(
    correctors = cms.VInputTag("hltAK4PFPuppiJetCorrector"),
    src = ("hltAK4PFPuppiJets")
)
