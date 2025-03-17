import FWCore.ParameterSet.Config as cms

from CommonTools.RecoAlgos.PFClusterRefCandidateProducer import PFClusterRefCandidateProducer as _PFClusterRefCandidateProducer

hltPfClusterRefsForJetsHGCAL = _PFClusterRefCandidateProducer(
    particleType = cms.string('pi+'),
    src = ("hltParticleFlowClusterHGCal")
)
