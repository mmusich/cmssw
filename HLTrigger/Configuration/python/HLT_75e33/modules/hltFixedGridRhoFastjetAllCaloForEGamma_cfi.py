import FWCore.ParameterSet.Config as cms

from RecoJets.JetProducers.FixedGridRhoProducerFastjetFromRecHit import FixedGridRhoProducerFastjetFromRecHit as _FixedGridRhoProducerFastjetFromRecHit

hltFixedGridRhoFastjetAllCaloForEGamma = _FixedGridRhoProducerFastjetFromRecHit(
    eThresHB = [0.8, 1.2, 1.2, 1.2],
    eThresHE = cms.vdouble(
        0.1, 0.2, 0.2, 0.2, 0.2,
        0.2, 0.2
    ),
    ebRecHitsTag = ("hltEcalRecHit","EcalRecHitsEB"),
    eeRecHitsTag = ("hltEcalRecHit","EcalRecHitsEE"),
    gridSpacing = 0.55,
    hbheRecHitsTag = ("hltHbhereco"),
    maxRapidity = 2.5,
    skipECAL = False,
    skipHCAL = False
)
