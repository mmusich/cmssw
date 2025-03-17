import FWCore.ParameterSet.Config as cms

from RecoTauTag.RecoTau.PFTauSelector import PFTauSelector as _PFTauSelector

hltHpsSelectedPFTausTrackPt1MediumChargedIsolation = _PFTauSelector(
    cut = 'pt > 0',
    discriminatorContainers = [],
    discriminators = [dict(
        discriminator = ("hltHpsPFTauMediumAbsOrRelChargedIsolationDiscriminator"),
        selectionCut = 0.5
    )],
    src = ("hltHpsPFTauProducer")
)
