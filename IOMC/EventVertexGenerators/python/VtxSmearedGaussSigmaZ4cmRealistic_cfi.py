import FWCore.ParameterSet.Config as cms

from IOMC.EventVertexGenerators.VtxSmearedParameters_cfi import GaussVtxSigmaZ4cmRealisticSmearingParameters,VtxSmearedCommon
VtxSmeared = cms.EDProducer("GaussEvtVtxGenerator",
    GaussVtxSigmaZ4cmRealisticSmearingParameters,
    VtxSmearedCommon
)
