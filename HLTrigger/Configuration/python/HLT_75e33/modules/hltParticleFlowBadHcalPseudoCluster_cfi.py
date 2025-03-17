import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFClusterProducer.PFBadHcalPseudoClusterProducer import PFBadHcalPseudoClusterProducer as _PFBadHcalPseudoClusterProducer

hltParticleFlowBadHcalPseudoCluster = _PFBadHcalPseudoClusterProducer(
    debug = cms.untracked.bool(False),
    enable = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
)
