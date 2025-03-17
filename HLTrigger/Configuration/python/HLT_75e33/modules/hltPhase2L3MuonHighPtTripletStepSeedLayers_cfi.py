import FWCore.ParameterSet.Config as cms

from RecoTracker.TkSeedingLayers.SeedingLayersEDProducer import SeedingLayersEDProducer as _SeedingLayersEDProducer

hltPhase2L3MuonHighPtTripletStepSeedLayers = _SeedingLayersEDProducer(
    BPix = dict(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("hltPhase2L3MuonHighPtTripletStepClusters")
    ),
    FPix = dict(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("hltPhase2L3MuonHighPtTripletStepClusters")
    ),
    MTEC = dict(

    ),
    MTIB = dict(

    ),
    MTID = dict(

    ),
    MTOB = dict(

    ),
    TEC = dict(

    ),
    TIB = dict(

    ),
    TID = dict(

    ),
    TOB = dict(

    ),
    layerList = [
        'BPix1+BPix2+BPix3',
        'BPix2+BPix3+BPix4',
        'BPix1+BPix3+BPix4',
        'BPix1+BPix2+BPix4',
        'BPix2+BPix3+FPix1_pos',
        'BPix2+BPix3+FPix1_neg',
        'BPix1+BPix2+FPix1_pos',
        'BPix1+BPix2+FPix1_neg',
        'BPix2+FPix1_pos+FPix2_pos',
        'BPix2+FPix1_neg+FPix2_neg',
        'BPix1+FPix1_pos+FPix2_pos',
        'BPix1+FPix1_neg+FPix2_neg',
        'FPix1_pos+FPix2_pos+FPix3_pos',
        'FPix1_neg+FPix2_neg+FPix3_neg',
        'BPix1+FPix2_pos+FPix3_pos',
        'BPix1+FPix2_neg+FPix3_neg',
        'FPix2_pos+FPix3_pos+FPix4_pos',
        'FPix2_neg+FPix3_neg+FPix4_neg',
        'FPix3_pos+FPix4_pos+FPix5_pos',
        'FPix3_neg+FPix4_neg+FPix5_neg',
        'FPix4_pos+FPix5_pos+FPix6_pos',
        'FPix4_neg+FPix5_neg+FPix6_neg',
        'FPix5_pos+FPix6_pos+FPix7_pos',
        'FPix5_neg+FPix6_neg+FPix7_neg',
        'FPix6_pos+FPix7_pos+FPix8_pos',
        'FPix6_neg+FPix7_neg+FPix8_neg'
    ],
    mightGet = cms.optional.untracked.vstring
)
