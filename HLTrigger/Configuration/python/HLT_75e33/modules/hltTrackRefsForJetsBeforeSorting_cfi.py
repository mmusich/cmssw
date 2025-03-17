import FWCore.ParameterSet.Config as cms

from CommonTools.RecoAlgos.ChargedRefCandidateProducer import ChargedRefCandidateProducer as _ChargedRefCandidateProducer

hltTrackRefsForJetsBeforeSorting = _ChargedRefCandidateProducer(
    particleType = cms.string('pi+'),
    src = cms.InputTag("hltTrackWithVertexRefSelectorBeforeSorting")
)
