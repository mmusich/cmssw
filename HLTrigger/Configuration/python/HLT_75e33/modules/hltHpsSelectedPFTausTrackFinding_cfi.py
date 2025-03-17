import FWCore.ParameterSet.Config as cms

from RecoTauTag.RecoTau.PFTauSelector import PFTauSelector as _PFTauSelector

hltHpsSelectedPFTausTrackFinding = _PFTauSelector(
    cut = 'pt > 0',
    discriminatorContainers = [],
    discriminators = [dict(
        discriminator = ("hltHpsPFTauTrackFindingDiscriminator"),
        selectionCut = 0.5
    )],
    src = ("hltHpsPFTauProducer")
)
