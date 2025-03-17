import FWCore.ParameterSet.Config as cms

from RecoTracker.CkfPattern.CkfTrackCandidateMaker import CkfTrackCandidateMaker as _CkfTrackCandidateMaker

hltHighPtTripletStepTrackCandidates = _CkfTrackCandidateMaker(
    MeasurementTrackerEvent = ("hltMeasurementTrackerEvent"), 
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    TrajectoryBuilderPSet = dict(
        refToPSet_ = cms.string('highPtTripletStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('highPtTripletStepTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = dict(
        numberMeasurementsForFit = 4,
        propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite')
    ),
    cleanTrajectoryAfterInOut = True,
    doSeedingRegionRebuilding = True,
    maxNSeeds = 100000,
    maxSeedsBeforeCleaning = 1000,
    numHitsForSeedCleaner = 50,
    onlyPixelHitsForSeedCleaner = True,
    phase2clustersToSkip = ("hltHighPtTripletStepClusters"),
    reverseTrajectories = False,
    src = ("hltHighPtTripletStepSeeds"),
    useHitsSplitting = False
)
