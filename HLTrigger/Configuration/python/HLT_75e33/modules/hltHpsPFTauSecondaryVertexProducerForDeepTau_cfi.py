import FWCore.ParameterSet.Config as cms

from RecoTauTag.RecoTau.PFTauSecondaryVertexProducer import PFTauSecondaryVertexProducer as _PFTauSecondaryVertexProducer

hltHpsPFTauSecondaryVertexProducerForDeepTau = _PFTauSecondaryVertexProducer(
    PFTauTag = cms.InputTag("hltHpsPFTauProducer")
)
