import FWCore.ParameterSet.Config as cms

from RecoTracker.FinalTrackSelectors.TrackCutClassifier import TrackCutClassifier as _TrackCutClassifier

hltHighPtTripletStepTrackCutClassifier = _TrackCutClassifier(
    beamspot = ("hltOnlineBeamSpot"),
    ignoreVertices = False,
    mva = dict(
        dr_par = dict(
            d0err = [0.003, 0.003, 0.003],
            d0err_par = [0.002, 0.002, 0.001],
            dr_exp = [4, 4, 4],
            dr_par1 = [0.7, 0.6, 0.6],
            dr_par2 = [0.6, 0.5, 0.45]
        ),
        dz_par = dict(
            dz_exp = [4, 4, 4],
            dz_par1 = [0.8, 0.7, 0.7],
            dz_par2 = [0.6, 0.6, 0.55]
        ),
        maxChi2 = [9999.0, 9999.0, 9999.0],
        maxChi2n = [2.0, 1.0, 0.8],
        maxDr = [0.5, 0.03, 3.40282346639e+38],
        maxDz = [0.5, 0.2, 3.40282346639e+38],
        maxDzWrtBS = [3.40282346639e+38, 24.0, 15.0],
        maxLostLayers = [3, 3, 2],
        min3DLayers = [3, 3, 4],
        minLayers = [3, 3, 4],
        minNVtxTrk = 3,
        minNdof = [1e-05, 1e-05, 1e-05],
        minPixelHits = [0, 0, 3]
    ),
    qualityCuts = [-0.7, 0.1, 0.7],
    src = ("hltHighPtTripletStepTracks"),
    vertices = ("hltPhase2PixelVertices")
)
