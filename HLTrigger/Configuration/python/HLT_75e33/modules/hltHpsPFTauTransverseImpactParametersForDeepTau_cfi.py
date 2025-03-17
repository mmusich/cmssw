import FWCore.ParameterSet.Config as cms

from RecoTauTag.RecoTau.PFTauTransverseImpactParameters import PFTauTransverseImpactParameters as _PFTauTransverseImpactParameters

hltHpsPFTauTransverseImpactParametersForDeepTau = _PFTauTransverseImpactParameters(
    PFTauPVATag = cms.InputTag("hltHpsPFTauPrimaryVertexProducerForDeepTau"),
    PFTauSVATag = cms.InputTag("hltHpsPFTauSecondaryVertexProducerForDeepTau"),
    PFTauTag = cms.InputTag("hltHpsPFTauProducer"),
    useFullCalculation = cms.bool(True)
)
