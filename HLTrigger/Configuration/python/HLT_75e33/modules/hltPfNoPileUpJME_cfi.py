import FWCore.ParameterSet.Config as cms

from CommonTools.ParticleFlow.TPPFCandidatesOnPFCandidates import TPPFCandidatesOnPFCandidates as _TPPFCandidatesOnPFCandidates

hltPfNoPileUpJME = _TPPFCandidatesOnPFCandidates(
    bottomCollection = cms.InputTag("hltParticleFlowPtrs"),
    enable = cms.bool(True),
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("hltPfPileUpJME")
)
