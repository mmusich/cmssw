import FWCore.ParameterSet.Config as cms

from RecoMuon.L3TrackFinder.Phase2HLTMuonSelectorForL3 import Phase2HLTMuonSelectorForL3 as _Phase2HLTMuonSelectorForL3

hltPhase2L3MuonFilter = _Phase2HLTMuonSelectorForL3(
    l1TkMuons = ("l1tTkMuonsGmt"),
    l2MuonsUpdVtx = ("hltL2MuonsFromL1TkMuon:UpdatedAtVtx"),
    l3Tracks = ("hltIter2Phase2L3FromL1TkMuonMerged"),
    IOFirst = True,
    matchingDr = 0.02,
    applyL3Filters = True,
    MinNhits = 1,
    MaxNormalizedChi2 = 5.0,
    MinNhitsMuons = 0,
    MinNhitsPixel = 1,
    MinNhitsTracker = 6,
    MaxPtDifference = 999.0,
)

from Configuration.ProcessModifiers.phase2L2AndL3Muons_cff import phase2L2AndL3Muons
from Configuration.ProcessModifiers.phase2L3MuonsOIFirst_cff import phase2L3MuonsOIFirst
(phase2L2AndL3Muons & phase2L3MuonsOIFirst).toModify(
    hltPhase2L3MuonFilter,
    l3Tracks = "hltPhase2L3OIMuonTrackSelectionHighPurity",
    IOFirst = False,
)
