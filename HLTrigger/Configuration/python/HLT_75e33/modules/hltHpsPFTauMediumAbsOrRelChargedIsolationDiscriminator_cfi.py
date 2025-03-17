import FWCore.ParameterSet.Config as cms

from RecoTauTag.RecoTau.PFTauDiscriminatorLogicalAndProducer import PFTauDiscriminatorLogicalAndProducer as _PFTauDiscriminatorLogicalAndProducer

hltHpsPFTauMediumAbsOrRelChargedIsolationDiscriminator = _PFTauDiscriminatorLogicalAndProducer(
    FailValue = 0.0,
    PFTauProducer = ("hltHpsPFTauProducer"),
    PassValue = 1.0,
    Prediscriminants = dict(
        BooleanOperator = cms.string('or'),
        discr1 = dict(
            Producer = ("hltHpsPFTauMediumAbsoluteChargedIsolationDiscriminator"),
            cut = 0.5
        ),
        discr2 = dict(
            Producer = ("hltHpsPFTauMediumRelativeChargedIsolationDiscriminator"),
            cut = 0.5
        )
    )
)
