import FWCore.ParameterSet.Config as cms

from RecoTracker.CkfPattern.CkfTrackCandidateMaker import CkfTrackCandidateMaker as _CkfTrackCandidateMaker

hltIter0Phase2L3FromL1TkMuonCkfTrackCandidates = _CkfTrackCandidateMaker(
    MeasurementTrackerEvent = ("hltMeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('none'),
    TrajectoryBuilderPSet = dict(
        refToPSet_ = cms.string('HLTIter0Phase2L3FromL1TkMuonPSetGroupedCkfTrajectoryBuilderIT')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = dict(
        numberMeasurementsForFit = 4,
        propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite')
    ),
    cleanTrajectoryAfterInOut = False,
    doSeedingRegionRebuilding = True,
    maxNSeeds = 100000,
    maxSeedsBeforeCleaning = 1000,
    src = ("hltIter0Phase2L3FromL1TkMuonPixelSeedsFromPixelTracks"),
    useHitsSplitting = True
)
