import FWCore.ParameterSet.Config as cms

from RecoMuon.L3MuonIsolationProducer.L3MuonCombinedRelativeIsolationProducer import L3MuonCombinedRelativeIsolationProducer as _L3MuonCombinedRelativeIsolationProducer

hltPhase2L3MuonsTrkIsoRegionalNewdR0p3dRVeto0p005dz0p25dr0p20ChisqInfPtMin0p0Cut0p07 = _L3MuonCombinedRelativeIsolationProducer(
    CaloDepositsLabel = ("notUsed"),
    CaloExtractorPSet = dict(
        CaloTowerCollectionLabel = ("hltPhase2TowerMakerForAll"),
        ComponentName = cms.string('CaloExtractor'),
        DR_Max = 0.3,
        DR_Veto_E = 0.07,
        DR_Veto_H = 0.1,
        DepositLabel = cms.untracked.string('EcalPlusHcal'),
        Threshold_E = 0.2,
        Threshold_H = 0.5,
        Vertex_Constraint_XY = False,
        Vertex_Constraint_Z = False,
        Weight_E = 1.0,
        Weight_H = 1.0
    ),
    CutsPSet = dict(
        ComponentName = cms.string('SimpleCuts'),
        ConeSizes = [0.3],
        EtaBounds = [2.411],
        Thresholds = [0.07],
        applyCutsORmaxNTracks = False,
        maxNTracks = -1
    ),
    OutputMuIsoDeposits = True,
    TrackPt_Min = -1.0,
    TrkExtractorPSet = dict(
        BeamSpotLabel = ("hltOnlineBeamSpot"),
        BeamlineOption = cms.string('BeamSpotFromEvent'),
        Chi2Ndof_Max = 1e+64,
        Chi2Prob_Min = -1.0,
        ComponentName = cms.string('PixelTrackExtractor'),
        DR_Max = 0.3,
        DR_Veto = 0.005,
        DR_VetoPt = 0.025,
        DepositLabel = cms.untracked.string('PXLS'),
        Diff_r = 0.2,
        Diff_z = 0.25,
        NHits_Min = 0,
        PropagateTracksToRadius = True,
        PtVeto_Min = 2.0,
        Pt_Min = -1.0,
        ReferenceRadius = 6.0,
        VetoLeadingTrack = True,
        inputTrackCollection = ("hltPhase2L3MuonGeneralTracks")
    ),
    UseCaloIso = False,
    UseRhoCorrectedCaloDeposits = False,
    inputMuonCollection = ("hltPhase2L3MuonCandidates"),
    printDebug = False
)
