import FWCore.ParameterSet.Config as cms

from RecoTracker.TkTrackingRegions.CandidateSeededTrackingRegionsEDProducer import CandidateSeededTrackingRegionsEDProducer as _CandidateSeededTrackingRegionsEDProducer

hltPhase2L3FromL1TkMuonPixelTracksTrackingRegions = _CandidateSeededTrackingRegionsEDProducer(
    RegionPSet = dict(
        beamSpot = ("hltOnlineBeamSpot"),
        deltaEta = 0.035,
        deltaPhi = 0.02,
        input = ("l1tTkMuonsGmt"),
        maxNRegions = 10000,
        maxNVertices = 1,
        measurementTrackerName = (""),
        mode = cms.string('BeamSpotSigma'),
        nSigmaZBeamSpot = 4.0,
        nSigmaZVertex = 3.0,
        originRadius = 0.2,
        precise = True,
        ptMin = 2.0,
        searchOpt = False,
        vertexCollection = ("notUsed"),
        whereToUseMeasurementTracker = cms.string('Never'),
        zErrorBeamSpot = 24.2,
        zErrorVetex = 0.2
    )
)

from Configuration.ProcessModifiers.phase2L2AndL3Muons_cff import phase2L2AndL3Muons
from Configuration.ProcessModifiers.phase2L3MuonsOIFirst_cff import phase2L3MuonsOIFirst
(phase2L2AndL3Muons & phase2L3MuonsOIFirst).toModify(
    hltPhase2L3FromL1TkMuonPixelTracksTrackingRegions.RegionPSet,
    input = "hltPhase2L3MuonFilter:L1TkMuToReuse"
)
