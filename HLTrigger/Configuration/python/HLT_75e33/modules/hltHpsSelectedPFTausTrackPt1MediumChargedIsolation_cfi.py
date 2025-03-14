import FWCore.ParameterSet.Config as cms

from RecoTauTag.RecoTau.PFTauSelector import PFTauSelector as _PFTauSelector

hltHpsSelectedPFTausTrackPt1MediumChargedIsolation = _PFTauSelector(
    cut = cms.string('pt > 0'),
    discriminatorContainers = cms.VPSet(),
    discriminators = cms.VPSet(cms.PSet(
        discriminator = cms.InputTag("hltHpsPFTauMediumAbsOrRelChargedIsolationDiscriminator"),
        selectionCut = cms.double(0.5)
    )),
    src = cms.InputTag("hltHpsPFTauProducer")
)
