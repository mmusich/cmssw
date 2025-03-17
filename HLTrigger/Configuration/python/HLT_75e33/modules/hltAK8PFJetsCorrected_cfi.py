import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Modules.CorrectedPFJetProducer import CorrectedPFJetProducer as _CorrectedPFJetProducer

hltAK8PFJetsCorrected = _CorrectedPFJetProducer(
    correctors = cms.VInputTag("hltAK8PFJetCorrector"),
    src = cms.InputTag("hltAK8PFJets")
)
