import FWCore.ParameterSet.Config as cms

from RecoTracker.TkSeedingLayers.SeedingLayersEDProducer import SeedingLayersEDProducer as _SeedingLayersEDProducer

hltPhase2L3FromL1TkMuonPixelLayerQuadruplets = _SeedingLayersEDProducer(
    BPix = dict(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    FPix = dict(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle')
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
    layerList = cms.vstring(
        'BPix1+BPix2+BPix3+BPix4',
        'BPix1+BPix2+BPix3+FPix1_pos',
        'BPix1+BPix2+BPix3+FPix1_neg',
        'BPix1+BPix2+FPix1_pos+FPix2_pos',
        'BPix1+BPix2+FPix1_neg+FPix2_neg',
        'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
        'BPix1+FPix1_neg+FPix2_neg+FPix3_neg'
    )
)
