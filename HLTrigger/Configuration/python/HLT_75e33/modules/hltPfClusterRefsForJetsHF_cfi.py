import FWCore.ParameterSet.Config as cms

from CommonTools.RecoAlgos.PFClusterRefCandidateProducer import PFClusterRefCandidateProducer as _PFClusterRefCandidateProducer

hltPfClusterRefsForJetsHF = _PFClusterRefCandidateProducer(
    particleType = cms.string('pi+'),
    src = cms.InputTag("hltParticleFlowClusterHF")
)
