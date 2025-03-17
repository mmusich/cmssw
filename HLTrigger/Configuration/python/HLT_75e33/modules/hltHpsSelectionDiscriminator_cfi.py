import FWCore.ParameterSet.Config as cms

from RecoTauTag.RecoTau.PFRecoTauDiscriminationByHPSSelection import PFRecoTauDiscriminationByHPSSelection as _PFRecoTauDiscriminationByHPSSelection

hltHpsSelectionDiscriminator = _PFRecoTauDiscriminationByHPSSelection(
    PFTauProducer = ("hltHpsCombinatoricRecoTaus"),
    Prediscriminants = dict(
        BooleanOperator = 'and'
    ),
    decayModes = [
        dict(
            applyBendCorrection = dict(
                eta = True,
                mass = True,
                phi = True
            ),
            maxMass = '1.',
            minMass = -1000.0,
            nCharged = 1,
            nChargedPFCandsMin = 1,
            nPiZeros = 0,
            nTracksMin = 1
        ),
        dict(
            applyBendCorrection = dict(
                eta = True,
                mass = True,
                phi = True
            ),
            assumeStripMass = 0.1349,
            maxMass = 'max(1.72, min(1.72*sqrt(pt/100.), 4.2))',
            minMass = 0.0,
            nCharged = 1,
            nChargedPFCandsMin = 1,
            nPiZeros = 1,
            nTracksMin = 1
        ),
        dict(
            applyBendCorrection = dict(
                eta = True,
                mass = True,
                phi = True
            ),
            assumeStripMass = 0.0,
            maxMass = 'max(1.72, min(1.72*sqrt(pt/100.), 4.0))',
            maxPi0Mass = 0.8,
            minMass = 0.4,
            minPi0Mass = 0.0,
            nCharged = 1,
            nChargedPFCandsMin = 1,
            nPiZeros = 2,
            nTracksMin = 1
        ),
        dict(
            applyBendCorrection = dict(
                eta = False,
                mass = True,
                phi = True
            ),
            maxMass = '1.2',
            minMass = 0.0,
            nCharged = 2,
            nChargedPFCandsMin = 1,
            nPiZeros = 0,
            nTracksMin = 2
        ),
        dict(
            applyBendCorrection = dict(
                eta = False,
                mass = True,
                phi = True
            ),
            maxMass = 'max(1.6, min(1.6*sqrt(pt/100.), 4.0))',
            minMass = 0.0,
            nCharged = 2,
            nChargedPFCandsMin = 1,
            nPiZeros = 1,
            nTracksMin = 2
        ),
        dict(
            applyBendCorrection = dict(
                eta = False,
                mass = True,
                phi = True
            ),
            maxMass = '1.6',
            minMass = 0.7,
            nCharged = 3,
            nChargedPFCandsMin = 1,
            nPiZeros = 0,
            nTracksMin = 2
        ),
        dict(
            applyBendCorrection = dict(
                eta = False,
                mass = False,
                phi = False
            ),
            maxMass = '1.6',
            minMass = 0.9,
            nCharged = 3,
            nChargedPFCandsMin = 1,
            nPiZeros = 1,
            nTracksMin = 2
        )
    ],
    matchingCone = 0.5,
    minPixelHits = 0,
    minTauPt = 0.0,
    requireTauChargedHadronsToBeChargedPFCands = False,
    verbosity = 0
)
