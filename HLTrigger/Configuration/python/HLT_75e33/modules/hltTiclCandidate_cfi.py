import FWCore.ParameterSet.Config as cms

from RecoHGCal.TICL.TICLCandidateProducer import TICLCandidateProducer as _TICLCandidateProducer

hltTiclCandidate = _TICLCandidateProducer(
    cutTk = cms.string('1.48 < abs(eta) < 3.0 && pt > 1. && quality("highPurity") && hitPattern().numberOfLostHits("MISSING_OUTER_HITS") < 5'),
    detector = cms.string('HGCAL'),
    egamma_tracksterlinks_collections = cms.VInputTag("hltTiclTracksterLinks"),
    egamma_tracksters_collections = cms.VInputTag("hltTiclTracksterLinks"),
    general_tracksterlinks_collections = cms.VInputTag("hltTiclTracksterLinks"),
    general_tracksters_collections = cms.VInputTag("hltTiclTracksterLinks"),
    interpretationDescPSet = dict(
        algo_verbosity = 0,
        cutTk = cms.string('1.48 < abs(eta) < 3.0 && pt > 1. && quality("highPurity") && hitPattern().numberOfLostHits("MISSING_OUTER_HITS") < 5'),
        delta_tk_ts_interface = 0.03,
        delta_tk_ts_layer1 = 0.02,
        timing_quality_threshold = 0.5,
        type = cms.string('General')
    ),
    layer_clusters = ("hltHgcalMergeLayerClusters"),
    layer_clustersTime = ("hltHgcalMergeLayerClusters","timeLayerCluster"),
    mightGet = cms.optional.untracked.vstring,
    muons = ("hltPhase2L3Muons"),
    original_masks = cms.VInputTag("hltHgcalMergeLayerClusters:InitialLayerClustersMask"),
    propagator = cms.string('PropagatorWithMaterial'),
    timingQualityThreshold = 0.5,
    timingSoA = ("mtdSoA"),
    tracks = ("hltGeneralTracks"),
    useMTDTiming = False,
    useTimingAverage = False
)

