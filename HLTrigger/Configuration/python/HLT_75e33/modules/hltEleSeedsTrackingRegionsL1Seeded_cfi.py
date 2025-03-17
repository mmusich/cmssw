import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaElectronProducers.TrackingRegionsFromSuperClustersEDProducer import TrackingRegionsFromSuperClustersEDProducer as _TrackingRegionsFromSuperClustersEDProducer

hltEleSeedsTrackingRegionsL1Seeded = _TrackingRegionsFromSuperClustersEDProducer(
    RegionPSet = dict(
        beamSpot = ("hltOnlineBeamSpot"),
        defaultZ = 0.0,
        deltaEtaRegion = 0.1,
        deltaPhiRegion = 0.4,
        measurementTrackerEvent = (""),
        minBSDeltaZ = 0.0,
        nrSigmaForBSDeltaZ = 4.0,
        originHalfLength = 12.5,
        originRadius = 0.2,
        precise = True,
        ptMin = 1.5,
        superClusters = cms.VInputTag("hltEgammaSuperClustersToPixelMatchL1Seeded"),
        useZInBeamspot = False,
        useZInVertex = False,
        vertices = (""),
        whereToUseMeasTracker = cms.string('kNever')
    )
)
