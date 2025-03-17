import FWCore.ParameterSet.Config as cms

from RecoMuon.TrackerSeedGenerator.L3TrackCombiner import L3TrackCombiner as _L3TrackCombiner

hltPhase2L3OIL3Muons = _L3TrackCombiner(
    labels = cms.VInputTag("hltL3MuonsPhase2L3OI")
)
