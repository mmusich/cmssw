import FWCore.ParameterSet.Config as cms

from RecoMuon.TrackerSeedGenerator.TSGForOIFromL2 import TSGForOIFromL2 as _TSGForOIFromL2

hltPhase2L3OISeedsFromL2Muons = _TSGForOIFromL2(
    MeasurementTrackerEvent = ("hltMeasurementTrackerEvent"),
    SF1 = 3.0,
    SF2 = 4.0,
    SF3 = 5.0,
    SF4 = 7.0,
    SF5 = 10.0,
    SF6 = 2.0,
    UseHitLessSeeds = True,
    adjustErrorsDynamicallyForHitless = True,
    adjustErrorsDynamicallyForHits = False,
    debug = cms.untracked.bool(False),
    estimator = cms.string('hltESPChi2MeasurementEstimator100'),
    eta1 = 0.2,
    eta2 = 0.3,
    eta3 = 1.0,
    eta4 = 1.2,
    eta5 = 1.6,
    eta6 = 1.4,
    eta7 = 2.1,
    fixedErrorRescaleFactorForHitless = 2.0,
    fixedErrorRescaleFactorForHits = 1.0,
    hitsToTry = 1,
    layersToTry = 2,
    maxEtaForTOB = 1.8,
    maxHitSeeds = 1,
    maxHitlessSeeds = 5,
    maxSeeds = 20,
    minEtaForTEC = 0.7,
    numL2ValidHitsCutAllEndcap = 30,
    numL2ValidHitsCutAllEta = 20,
    pT1 = 13.0,
    pT2 = 30.0,
    pT3 = 70.0,
    propagatorName = cms.string('PropagatorWithMaterialParabolicMf'),
    src = ("hltL2MuonsFromL1TkMuon","UpdatedAtVtx"),
    tsosDiff1 = 0.2,
    tsosDiff2 = 0.02
)

from Configuration.ProcessModifiers.phase2L2AndL3Muons_cff import phase2L2AndL3Muons
phase2L2AndL3Muons.toModify(
    hltPhase2L3OISeedsFromL2Muons,
    src = "hltPhase2L3MuonFilter:L2MuToReuse"
)

from Configuration.ProcessModifiers.phase2L3MuonsOIFirst_cff import phase2L3MuonsOIFirst
(phase2L2AndL3Muons & phase2L3MuonsOIFirst).toModify(
    hltPhase2L3OISeedsFromL2Muons,
    src ="hltL2MuonsFromL1TkMuon:UpdatedAtVtx"
)
