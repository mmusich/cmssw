import FWCore.ParameterSet.Config as cms

from RecoTracker.TkTrackingRegions.CandidateSeededTrackingRegionsEDProducer import CandidateSeededTrackingRegionsEDProducer as _CandidateSeededTrackingRegionsEDProducer

hltPhase2L3MuonPixelTracksAndHighPtTripletTrackingRegions = _CandidateSeededTrackingRegionsEDProducer(
    RegionPSet = dict(
        beamSpot = ("hltOnlineBeamSpot"),
        deltaEta = 0.4,
        deltaPhi = 0.4,
        input = ("hltPhase2L3MuonCandidates"),
        maxNRegions = 10000,
        maxNVertices = 1,
        measurementTrackerName = (""),
        mode = cms.string('BeamSpotSigma'),
        nSigmaZBeamSpot = 4.0,
        nSigmaZVertex = 3.0,
        originRadius = 0.2,
        precise = True,
        ptMin = 0.9,
        searchOpt = False,
        vertexCollection = ("notUsed"),
        whereToUseMeasurementTracker = cms.string('Never'),
        zErrorBeamSpot = 24.2,
        zErrorVetex = 0.2
    )
)
