import FWCore.ParameterSet.Config as cms

from CommonTools.RecoAlgos.PFClusterRefCandidateMerger import PFClusterRefCandidateMerger as _PFClusterRefCandidateMerger

hltPfClusterRefsForJets = _PFClusterRefCandidateMerger(
    src = cms.VInputTag("hltPfClusterRefsForJetsHCAL", "hltPfClusterRefsForJetsECAL", "hltPfClusterRefsForJetsHF", "hltPfClusterRefsForJetsHO", "hltPfClusterRefsForJetsHGCAL")
)
