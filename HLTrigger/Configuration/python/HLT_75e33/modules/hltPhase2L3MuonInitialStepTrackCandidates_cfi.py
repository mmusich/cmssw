import FWCore.ParameterSet.Config as cms

from RecoTracker.CkfPattern.CkfTrackCandidateMaker import CkfTrackCandidateMaker as _CkfTrackCandidateMaker

hltPhase2L3MuonInitialStepTrackCandidates = _CkfTrackCandidateMaker(
    MeasurementTrackerEvent = ("hltMeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    TrajectoryBuilderPSet = dict(
        refToPSet_ = cms.string('hltPhase2L3MuonInitialStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = dict(
        numberMeasurementsForFit = 4,
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = True,
    doSeedingRegionRebuilding = True,
    maxNSeeds = 100000,
    maxSeedsBeforeCleaning = 1000,
    numHitsForSeedCleaner = 50,
    onlyPixelHitsForSeedCleaner = True,
    reverseTrajectories = False,
    src = ("hltPhase2L3MuonInitialStepSeeds"),
    useHitsSplitting = False
)
