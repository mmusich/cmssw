import FWCore.ParameterSet.Config as cms

from RecoTauTag.RecoTau.RecoTauCleaner import RecoTauCleaner as _RecoTauCleaner

hltHpsPFTauProducerSansRefs = _RecoTauCleaner(
    cleaners = [
        dict(
            name = 'HPS_Select',
            plugin = 'RecoTauDiscriminantCleanerPlugin',
            src = ("hltHpsSelectionDiscriminator")
        ),
        dict(
            minTrackPt = 5.0,
            name = 'killSoftTwoProngTaus',
            plugin = 'RecoTauSoftTwoProngTausCleanerPlugin'
        ),
        dict(
            name = 'ChargedHadronMultiplicity',
            plugin = 'RecoTauChargedHadronMultiplicityCleanerPlugin'
        ),
        dict(
            name = 'Pt',
            plugin = 'RecoTauStringCleanerPlugin',
            selection = 'leadPFCand().isNonnull()',
            selectionFailValue = 1000.0,
            selectionPassFunction = '-pt()',
            tolerance = 0.01
        ),
        dict(
            name = 'StripMultiplicity',
            plugin = 'RecoTauStringCleanerPlugin',
            selection = 'leadPFCand().isNonnull()',
            selectionFailValue = 1000.0,
            selectionPassFunction = '-signalPiZeroCandidates().size()'
        ),
        dict(
            name = 'CombinedIsolation',
            plugin = 'RecoTauStringCleanerPlugin',
            selection = 'leadPFCand().isNonnull()',
            selectionFailValue = 1000.0,
            selectionPassFunction = 'isolationPFChargedHadrCandsPtSum() + isolationPFGammaCandsEtSum()'
        )
    ],
    outputSelection = '',
    src = ("hltHpsCombinatoricRecoTaus"),
    verbosity = 0
)
