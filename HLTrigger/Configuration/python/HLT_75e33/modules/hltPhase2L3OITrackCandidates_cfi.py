import FWCore.ParameterSet.Config as cms

from RecoTracker.CkfPattern.CkfTrackCandidateMaker import CkfTrackCandidateMaker as _CkfTrackCandidateMaker

hltPhase2L3OITrackCandidates = _CkfTrackCandidateMaker(
    MeasurementTrackerEvent = ("hltMeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    TrajectoryBuilderPSet = dict(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('muonSeededTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = dict(
        numberMeasurementsForFit = 4,
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = False,
    doSeedingRegionRebuilding = False,
    maxNSeeds = 500000,
    maxSeedsBeforeCleaning = 5000,
    src = ("hltPhase2L3OISeedsFromL2Muons"),
    useHitsSplitting = False
)
