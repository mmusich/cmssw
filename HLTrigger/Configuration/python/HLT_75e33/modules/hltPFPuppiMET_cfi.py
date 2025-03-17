import FWCore.ParameterSet.Config as cms

from RecoMET.METProducers.pfMetPuppi_cfi import pfMetPuppi as _pfMetPuppi

hltPFPuppiMET = _pfMetPuppi.clone(
    applyWeight = True,
    calculateSignificance = False,
    globalThreshold = 0.0,
    src = ("hltParticleFlowTmp"),
    srcWeights = ("hltPFPuppiNoLep")
)
