import FWCore.ParameterSet.Config as cms

from RecoMuon.TrackerSeedGenerator.L3TrackLinksCombiner import L3TrackLinksCombiner as _L3TrackLinksCombiner

hltPhase2L3OIL3MuonsLinksCombination = _L3TrackLinksCombiner(
    labels = cms.VInputTag("hltL3MuonsPhase2L3OI")
)
