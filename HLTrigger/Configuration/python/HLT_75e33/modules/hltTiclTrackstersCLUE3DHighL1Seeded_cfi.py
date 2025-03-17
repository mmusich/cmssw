import FWCore.ParameterSet.Config as cms

from RecoHGCal.TICL.TrackstersProducer import TrackstersProducer as _TrackstersProducer

hltTiclTrackstersCLUE3DHighL1Seeded = _TrackstersProducer(
    detector = cms.string('HGCAL'),
    filtered_mask = ("hltFilteredLayerClustersCLUE3DHighL1Seeded","CLUE3DHigh"),
    itername = cms.string('CLUE3DHigh'),
    layer_clusters = ("hltHgcalMergeLayerClustersL1Seeded"),
    layer_clusters_hfnose_tiles = ("ticlLayerTileHFNose"),
    layer_clusters_tiles = ("hltTiclLayerTileProducerL1Seeded"),
    mightGet = cms.optional.untracked.vstring,
    original_mask = ("hltHgcalMergeLayerClustersL1Seeded","InitialLayerClustersMask"),
    patternRecognitionBy = cms.string('CLUE3D'),
    inferenceAlgo = cms.string('TracksterInferenceByCNNv4'),
    pluginPatternRecognitionByCA = dict(
        algo_verbosity = 0,
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
    criticalDensity = cms.vdouble(
      0.6,
      0.6,
      0.6
    ),
    criticalSelfDensity = cms.vdouble(
      0.15,
      0.15,
      0.15
    ),
    densitySiblingLayers = cms.vint32(
      3,
      3,
      3
    ),
    densityEtaPhiDistanceSqr = cms.vdouble(
      0.0008,
      0.0008,
      0.0008
    ),
    densityXYDistanceSqr = cms.vdouble(
      3.24,
      3.24,
      3.24
    ),
    kernelDensityFactor = cms.vdouble(
      0.2,
      0.2,
      0.2
    ),
    densityOnSameLayer = False,
    nearestHigherOnSameLayer = False,
    useAbsoluteProjectiveScale = True,
    useClusterDimensionXY = False,
    rescaleDensityByZ = False,
    criticalEtaPhiDistance = cms.vdouble(
      0.025,
      0.025,
      0.025
    ),
    criticalXYDistance = cms.vdouble(
      1.8,
      1.8,
      1.8
    ),
    criticalZDistanceLyr = cms.vint32(
      5,
      5,
      5
    ),
    outlierMultiplier = cms.vdouble(
      2,
      2,
      2
    ),
    minNumLayerCluster = cms.vint32(
      2,
      2,
      2
    ),
    computeLocalTime = False,
    doPidCut = True,
    cutHadProb = 999.,
    type = cms.string('CLUE3D')
    ),
    pluginPatternRecognitionByFastJet = dict(
        algo_verbosity = 0,
        antikt_radius = 0.09,
        minNumLayerCluster = 5,
        type = cms.string('FastJet')
    ),
    pluginInferenceAlgoTracksterInferenceByCNNv4 = dict(
        algo_verbosity = 0,
        onnxModelPath = cms.FileInPath('RecoHGCal/TICL/data/ticlv4/onnx_models/energy_id_v0.onnx'),
        inputNames  = ['input:0'],
        outputNames = ["output/regressed_energy:0", "output/id_probabilities:0"],
        eid_min_cluster_energy = 1,
        eid_n_layers = 50,
        eid_n_clusters = 10,
        doPID = 1,
        doRegression = 0,
        type = cms.string('TracksterInferenceByCNNv4')
    ),
    pluginInferenceAlgoTracksterInferenceByDNN = dict(
        algo_verbosity = 0,
	onnxPIDModelPath = cms.FileInPath('RecoHGCal/TICL/data/ticlv5/onnx_models/DNN/patternrecognition/id_v0.onnx'),
        onnxEnergyModelPath = cms.FileInPath('RecoHGCal/TICL/data/ticlv5/onnx_models/DNN/patternrecognition/energy_v0.onnx'),
        inputNames  = ['input'],
        output_en   = ['enreg_output'],
        output_id   = ['pid_output'],
        eid_n_layers = 50,
        eid_n_clusters = 10,
        doPID = 1,
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
        eid_n_layers = 50,
        eid_n_clusters = 10,
        doPID = 1,
        doRegression = 0,
        type = cms.string('TracksterInferenceByPFN')
    ),
    pluginInferenceAlgoTracksterInferenceByANN = dict(
      algo_verbosity = 0,
      type = cms.string('TracksterInferenceByANN')
    
    ),
    seeding_regions = ("hltTiclSeedingL1"),
    time_layerclusters = ("hltHgcalMergeLayerClustersL1Seeded","timeLayerCluster"),
)

from Configuration.ProcessModifiers.ticl_v5_cff import ticl_v5
ticl_v5.toModify(hltTiclTrackstersCLUE3DHighL1Seeded.pluginPatternRecognitionByCLUE3D, computeLocalTime = True)
ticl_v5.toModify(hltTiclTrackstersCLUE3DHighL1Seeded.inferenceAlgo, type = cms.string('TracksterInferenceByPFN'))

