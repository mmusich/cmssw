import FWCore.ParameterSet.Config as cms

from RecoMET.METProducers.pfMetPuppi_cfi import pfMetPuppi as _pfMetPuppi

hltPFPuppiMET = _pfMetPuppi.clone(
    applyWeight = cms.bool(True),
    calculateSignificance = cms.bool(False),
    globalThreshold = cms.double(0.0),
    src = cms.InputTag("hltParticleFlowTmp"),
    srcWeights = cms.InputTag("hltPFPuppiNoLep")
)
