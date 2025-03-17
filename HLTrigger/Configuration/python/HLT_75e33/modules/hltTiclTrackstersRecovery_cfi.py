import FWCore.ParameterSet.Config as cms

from RecoHGCal.TICL.TrackstersProducer import TrackstersProducer as _TrackstersProducer

hltTiclTrackstersRecovery = _TrackstersProducer(
    detector = cms.string('HGCAL'),
    filtered_mask = ("hltFilteredLayerClustersRecovery","Recovery"),
    itername = cms.string('Recovery'),
    layer_clusters = ("hltHgcalMergeLayerClusters"),
    layer_clusters_hfnose_tiles = ("ticlLayerTileHFNose"),
    layer_clusters_tiles = ("hltTiclLayerTileProducer"),
    mightGet = cms.optional.untracked.vstring,
    original_mask = ("hltTiclTrackstersCLUE3DHigh"),
    patternRecognitionBy = cms.string('Recovery'),
    inferenceAlgo = cms.string('TracksterInferenceByPFN'),
    pluginPatternRecognitionByCA = dict(
        algo_verbosity = 0,
        computeLocalTime = True,
        energy_em_over_total_threshold = -1,
        etaLimitIncreaseWindow = 2.1,
        filter_on_categories = [0],
        max_delta_time = 3,
        max_longitudinal_sigmaPCA = 9999,
        max_missing_layers_in_trackster = 9999,
        max_out_in_hops = 10,
        min_cos_pointing = -1,
        min_cos_theta = 0.915,
        min_layers_per_trackster = 10,
        oneTracksterPerTrackSeed = False,
        out_in_dfs = True,
        pid_threshold = 0,
        promoteEmptyRegionToTrackster = False,
        root_doublet_max_distance_from_seed_squared = 9999,
        shower_start_max_layer = 9999,
        siblings_maxRSquared = [0.0006, 0.0006, 0.0006],
        skip_layers = 0,
        type = cms.string('CA')
    ),
    pluginPatternRecognitionByCLUE3D = dict(
        algo_verbosity = 0,
        computeLocalTime = True,
        criticalDensity = [4, 4, 4],
        criticalEtaPhiDistance = [0.025, 0.025, 0.025],
        criticalSelfDensity = [0.15, 0.15, 0.15],
        criticalXYDistance = [1.8, 1.8, 1.8],
        criticalZDistanceLyr = [5, 5, 5],
        cutHadProb = 0.5,
        densityEtaPhiDistanceSqr = [0.0008, 0.0008, 0.0008],
        densityOnSameLayer = False,
        densitySiblingLayers = [3, 3, 3],
        densityXYDistanceSqr = [3.24, 3.24, 3.24],
        doPidCut = False,
        kernelDensityFactor = [0.2, 0.2, 0.2],
        minNumLayerCluster = [2, 2, 2],
        nearestHigherOnSameLayer = False,
        outlierMultiplier = [2, 2, 2],
        rescaleDensityByZ = False,
        type = cms.string('CLUE3D'),
        useAbsoluteProjectiveScale = True,
        useClusterDimensionXY = False
    ),
    pluginPatternRecognitionByFastJet = dict(
        algo_verbosity = 0,
        antikt_radius = 0.09,
        computeLocalTime = True,
        minNumLayerCluster = 5,
        type = cms.string('FastJet')
    ),
    pluginPatternRecognitionByRecovery = dict(
        algo_verbosity = 0,
        type = cms.string('Recovery')
    ),

    pluginInferenceAlgoTracksterInferenceByDNN = dict(
        algo_verbosity = 0,
	onnxPIDModelPath = cms.FileInPath('RecoHGCal/TICL/data/ticlv5/onnx_models/DNN/patternrecognition/id_v0.onnx'),
        onnxEnergyModelPath = cms.FileInPath('RecoHGCal/TICL/data/ticlv5/onnx_models/DNN/patternrecognition/energy_v0.onnx'),
        inputNames  = ['input'],
        output_en   = ['enreg_output'],
        output_id   = ['pid_output'],
        eid_min_cluster_energy = 1,
        eid_n_layers = 50,
        eid_n_clusters = 10,
        doPID = 0,
        doRegression = 0,
        type = cms.string('TracksterInferenceByDNN')
    ),
    pluginInferenceAlgoTracksterInferenceByPFN = dict(
        algo_verbosity = 0,
        onnxPIDModelPath = cms.FileInPath('RecoHGCal/TICL/data/ticlv5/onnx_models/PFN/patternrecognition/id_v0.onnx'),
        onnxEnergyModelPath = cms.FileInPath('RecoHGCal/TICL/data/ticlv5/onnx_models/PFN/patternrecognition/energy_v0.onnx'),
        inputNames  = ['input','input_tr_features'],
        output_en   = ['enreg_output'],
        output_id   = ['pid_output'],
        eid_min_cluster_energy = 1,
        eid_n_layers = 50,
        eid_n_clusters = 10,
        doPID = 0,
        doRegression = 0,
        type = cms.string('TracksterInferenceByPFN')
    ),
    pluginInferenceAlgoTracksterInferenceByANN = dict(
      algo_verbosity = 0,
      type = cms.string('TracksterInferenceByANN')
    
    ),
    seeding_regions = ("hltTiclSeedingGlobal"),
    time_layerclusters = ("hltHgcalMergeLayerClusters","timeLayerCluster")
)
