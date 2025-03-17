import FWCore.ParameterSet.Config as cms

from RecoTauTag.RecoTau.RecoTauPiZeroUnembedder import RecoTauPiZeroUnembedder as _RecoTauPiZeroUnembedder

hltHpsPFTauProducer = _RecoTauPiZeroUnembedder(
    src = cms.InputTag("hltHpsPFTauProducerSansRefs")
)
