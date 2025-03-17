import FWCore.ParameterSet.Config as cms

from HLTrigger.Muon.HLTMuonTrackSelector import HLTMuonTrackSelector as _HLTMuonTrackSelector

hltPhase2L3MuonTracks = _HLTMuonTrackSelector(
    copyExtras = cms.untracked.bool(True),
    copyMVA = False,
    copyTrajectories = cms.untracked.bool(False),
    muon = ("hltPhase2L3Muons"),
    originalMVAVals = ("none"),
    track = ("hltPhase2L3MuonMerged")
)
