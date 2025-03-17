import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFTracking.HGCalTrackCollectionProducer import HGCalTrackCollectionProducer as _HGCalTrackCollectionProducer

hltHgcalTrackCollection = _HGCalTrackCollectionProducer(
    DPtOverPtCuts_byTrackAlgo = cms.vdouble(
        10.0, 10.0, 10.0, 10.0, 10.0,
        5.0
    ),
    NHitCuts_byTrackAlgo = cms.vuint32(
        3, 3, 3, 3, 3,
        32700
    ),
    hgcalGeometryNames = dict(
        HGC_ECAL = cms.string('HGCalEESensitive')
    ),
    src = ("hltPfTrack"),
    trackQuality = cms.string('highPurity'),
    useIterativeTracking = True
)
