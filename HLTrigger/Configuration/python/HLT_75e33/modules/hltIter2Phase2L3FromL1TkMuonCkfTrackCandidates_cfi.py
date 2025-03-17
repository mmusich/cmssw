import FWCore.ParameterSet.Config as cms

from RecoTracker.CkfPattern.CkfTrackCandidateMaker import CkfTrackCandidateMaker as _CkfTrackCandidateMaker

hltIter2Phase2L3FromL1TkMuonCkfTrackCandidates = _CkfTrackCandidateMaker(
    MeasurementTrackerEvent = ("hltIter2Phase2L3FromL1TkMuonMaskedMeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    TrajectoryBuilderPSet = dict(
        refToPSet_ = cms.string('HLTIter2Phase2L3FromL1TkMuonPSetGroupedCkfTrajectoryBuilderIT')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = dict(
        numberMeasurementsForFit = 4,
        propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite')
    ),
    cleanTrajectoryAfterInOut = False,
    doSeedingRegionRebuilding = False,
    maxNSeeds = 100000,
    maxSeedsBeforeCleaning = 1000,
    src = ("hltIter2Phase2L3FromL1TkMuonPixelSeedsFiltered"),
    useHitsSplitting = False
)
