import FWCore.ParameterSet.Config as cms

from RecoTauTag.RecoTau.PFTauTransverseImpactParameters import PFTauTransverseImpactParameters as _PFTauTransverseImpactParameters

hltHpsPFTauTransverseImpactParametersForDeepTau = _PFTauTransverseImpactParameters(
    PFTauPVATag = ("hltHpsPFTauPrimaryVertexProducerForDeepTau"),
    PFTauSVATag = ("hltHpsPFTauSecondaryVertexProducerForDeepTau"),
    PFTauTag = ("hltHpsPFTauProducer"),
    useFullCalculation = True
)
