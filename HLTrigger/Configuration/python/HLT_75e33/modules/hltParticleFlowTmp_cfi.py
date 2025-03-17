import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFProducer.PFCandidateListMerger import PFCandidateListMerger as _PFCandidateListMerger

hltParticleFlowTmp = _PFCandidateListMerger(
    src = cms.VInputTag("hltParticleFlowTmpBarrel", "hltPfTICL")
)
