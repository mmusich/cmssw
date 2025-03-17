import FWCore.ParameterSet.Config as cms

from CommonTools.ParticleFlow.TPPFCandidatesOnPFCandidates import TPPFCandidatesOnPFCandidates as _TPPFCandidatesOnPFCandidates

hltPfNoPileUpJME = _TPPFCandidatesOnPFCandidates(
    bottomCollection = ("hltParticleFlowPtrs"),
    enable = True,
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = ("hltPfPileUpJME")
)
