import FWCore.ParameterSet.Config as cms

from CommonTools.RecoAlgos.PFClusterRefCandidateProducer import PFClusterRefCandidateProducer as _PFClusterRefCandidateProducer

hltPfClusterRefsForJetsHO = _PFClusterRefCandidateProducer(
    particleType = cms.string('pi+'),
    src = cms.InputTag("hltParticleFlowClusterHO")
)
