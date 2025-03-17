import FWCore.ParameterSet.Config as cms

from RecoMET.METProducers.pfMetPuppi_cfi import pfMetPuppi as _pfMetPuppi

hltPFMET = _pfMetPuppi.clone(
    calculateSignificance = cms.bool(False),
    globalThreshold = cms.double(0.0),
    src = cms.InputTag("hltParticleFlowTmp")
)
