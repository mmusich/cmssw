import FWCore.ParameterSet.Config as cms

from RecoMET.METProducers.PFClusterMETProducer import PFClusterMETProducer as _PFClusterMETProducer

hltPFClusterMET = _PFClusterMETProducer(
    alias = cms.string('pfClusterMet'),
    globalThreshold = cms.double(0.0),
    src = cms.InputTag("hltPfClusterRefsForJets")
)
