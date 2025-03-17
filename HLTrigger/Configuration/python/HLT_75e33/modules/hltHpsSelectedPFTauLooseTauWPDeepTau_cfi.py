import FWCore.ParameterSet.Config as cms

from RecoTauTag.RecoTau.PFTauSelector import PFTauSelector as _PFTauSelector

hltHpsSelectedPFTauLooseTauWPDeepTau = _PFTauSelector(
    cut = 'pt > 27 && abs(eta) < 2.1',
    discriminatorContainers = [dict(
        discriminator = ("hltHpsPFTauDeepTauProducer","VSjet"),
        rawValues = [],
        selectionCuts = [],
        workingPoints = ['double t1 = 0.5419, t2 = 0.4837, t3 = 0.050, x1 = 27, x2 = 100, x3 = 300; if (pt <= x1) return t1; if (pt >= x3) return t3; if (pt < x2) return (t2 - t1) / (x2 - x1) * (pt - x1) + t1; return (t3 - t2) / (x3 - x2) * (pt - x2) + t2;']
    )],
    discriminators = [],
    src = ("hltHpsPFTauProducer")
)
