import FWCore.ParameterSet.Config as cms

from RecoJets.JetProducers.FixedGridRhoProducerFastjet import FixedGridRhoProducerFastjet as _FixedGridRhoProducerFastjet

hltFixedGridRhoFastjetAll = _FixedGridRhoProducerFastjet(
    gridSpacing = 0.55,
    maxRapidity = 5.0,
    pfCandidatesTag = ("hltParticleFlowTmp")
)
