import FWCore.ParameterSet.Config as cms

from RecoTracker.TkSeedingLayers.SeedingLayersEDProducer import SeedingLayersEDProducer as _SeedingLayersEDProducer

hltPixelLayerPairsUnseeded = _SeedingLayersEDProducer(
    BPix = dict(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
        skipClusters = cms.InputTag("hltElePixelHitTripletsClusterRemoverUnseeded")
    ),
    FPix = dict(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
        skipClusters = cms.InputTag("hltElePixelHitTripletsClusterRemoverUnseeded")
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
        'BPix1+BPix2',
        'BPix1+BPix3',
        'BPix1+BPix4',
        'BPix2+BPix3',
        'BPix2+BPix4',
        'BPix3+BPix4',
        'FPix1_pos+FPix2_pos',
        'FPix1_pos+FPix3_pos',
        'FPix2_pos+FPix3_pos',
        'BPix1+FPix1_pos',
        'BPix1+FPix2_pos',
        'BPix1+FPix3_pos',
        'BPix2+FPix1_pos',
        'BPix2+FPix2_pos',
        'BPix2+FPix3_pos',
        'BPix3+FPix1_pos',
        'BPix3+FPix2_pos',
        'BPix3+FPix3_pos',
        'BPix4+FPix1_pos',
        'BPix4+FPix2_pos',
        'BPix4+FPix3_pos',
        'FPix1_neg+FPix2_neg',
        'FPix1_neg+FPix3_neg',
        'FPix2_neg+FPix3_neg',
        'BPix1+FPix1_neg',
        'BPix1+FPix2_neg',
        'BPix1+FPix3_neg',
        'BPix2+FPix1_neg',
        'BPix2+FPix2_neg',
        'BPix2+FPix3_neg',
        'BPix3+FPix1_neg',
        'BPix3+FPix2_neg',
        'BPix3+FPix3_neg',
        'BPix4+FPix1_neg',
        'BPix4+FPix2_neg',
        'BPix4+FPix3_neg'
    ]
)
