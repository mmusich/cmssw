import FWCore.ParameterSet.Config as cms
from ..psets.hltTiclTracksterLinksPSet_cfi import hltTiclTracksterLinksPSet 

from RecoHGCal.TICL.TracksterLinksProducer import TracksterLinksProducer as _TracksterLinksProducer

hltTiclTracksterLinks = _TracksterLinksProducer(
    detector = cms.string('HGCAL'),
    layer_clusters = ("hltHgcalMergeLayerClusters"),
    layer_clustersTime = ("hltHgcalMergeLayerClusters","timeLayerCluster"),
    inferenceAlgo = cms.string('TracksterInferenceByPFN'),
    linkingPSet = hltTiclTracksterLinksPSet,
    pluginInferenceAlgoTracksterInferenceByDNN = dict(
        algo_verbosity = 0,
        onnxPIDModelPath = cms.FileInPath('RecoHGCal/TICL/data/ticlv5/onnx_models/DNN/linking/id_v0.onnx'),
        onnxEnergyModelPath = cms.FileInPath('RecoHGCal/TICL/data/ticlv5/onnx_models/DNN/linking/energy_v0.onnx'),
        inputNames  = cms.vstring('input'),
        output_en   = cms.vstring('enreg_output'),
        output_id   = cms.vstring('pid_output'),
        eid_min_cluster_energy = 1,
        eid_n_layers = 50,
        eid_n_clusters = 10,
        doPID = 1,
        doRegression = 1,
        type = cms.string('TracksterInferenceByDNN')
    ),
    pluginInferenceAlgoTracksterInferenceByPFN = dict(
        algo_verbosity = 0,
        onnxPIDModelPath = cms.FileInPath('RecoHGCal/TICL/data/ticlv5/onnx_models/PFN/linking/id_v0.onnx'),
        onnxEnergyModelPath = cms.FileInPath('RecoHGCal/TICL/data/ticlv5/onnx_models/PFN/linking/energy_v0.onnx'),
        inputNames  = cms.vstring('input','input_tr_features'),
        output_en   = cms.vstring('enreg_output'),
        output_id   = cms.vstring('pid_output'),
        eid_min_cluster_energy = 1,
        eid_n_layers = 50,
        eid_n_clusters = 10,
        doPID = 1,
        doRegression = 1,
        type = cms.string('TracksterInferenceByPFN')
    ),
    mightGet = cms.optional.untracked.vstring,
    original_masks = cms.VInputTag("hltHgcalMergeLayerClusters:InitialLayerClustersMask"),
    propagator = cms.string('PropagatorWithMaterial'),
    regressionAndPid = True,
    tracksters_collections = cms.VInputTag("hltTiclTrackstersCLUE3DHigh", "hltTiclTrackstersRecovery")
)


