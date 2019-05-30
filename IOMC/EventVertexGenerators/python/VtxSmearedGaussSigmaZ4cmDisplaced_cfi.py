import FWCore.ParameterSet.Config as cms

from IOMC.EventVertexGenerators.VtxSmearedParameters_cfi import GaussVtxSigmaZ4cmDisplacedSmearingParameters,VtxSmearedCommon
VtxSmeared = cms.EDProducer("GaussEvtVtxGenerator",
    GaussVtxSigmaZ4cmDisplacedSmearingParameters,
    VtxSmearedCommon
)
