import FWCore.ParameterSet.Config as cms

from RecoTracker.FinalTrackSelectors.TrackCutClassifier import TrackCutClassifier as _TrackCutClassifier

hltPhase2L3OIMuonTrackCutClassifier = _TrackCutClassifier(
    beamspot = ("hltOnlineBeamSpot"),
    ignoreVertices = True,
    mva = dict(
        dr_par = dict(
            d0err = [0.003, 0.003, 3.40282346639e+38],
            d0err_par = [0.001, 0.001, 3.40282346639e+38],
            dr_exp = [4, 4, 2147483647],
            dr_par1 = [0.4, 0.4, 3.40282346639e+38],
            dr_par2 = [0.3, 0.3, 3.40282346639e+38]
        ),
        dz_par = dict(
            dz_exp = [4, 4, 2147483647],
            dz_par1 = [0.4, 0.4, 3.40282346639e+38],
            dz_par2 = [0.35, 0.35, 3.40282346639e+38]
        ),
        maxChi2 = [3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38],
        maxChi2n = [10.0, 1.0, 0.4],
        maxDr = [0.5, 0.03, 3.40282346639e+38],
        maxDz = [0.5, 0.2, 3.40282346639e+38],
        maxDzWrtBS = [3.40282346639e+38, 24.0, 100.0],
        maxLostLayers = [4, 3, 2],
        min3DLayers = [1, 2, 1],
        minLayers = [3, 5, 5],
        minNVtxTrk = 3,
        minNdof = [1e-05, 1e-05, 1e-05],
        minPixelHits = [0, 0, 1]
    ),
    qualityCuts = [-0.7, 0.1, 0.7],
    src = ("hltPhase2L3OIMuCtfWithMaterialTracks"),
    vertices = ("Notused")
)
