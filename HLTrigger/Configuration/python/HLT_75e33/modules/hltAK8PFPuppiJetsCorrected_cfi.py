import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Modules.CorrectedPFJetProducer import CorrectedPFJetProducer as _CorrectedPFJetProducer

hltAK8PFPuppiJetsCorrected = _CorrectedPFJetProducer(
    correctors = cms.VInputTag("hltAK8PFPuppiJetCorrector"),
    src = ("hltAK8PFPuppiJets")
)
