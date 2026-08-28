import FWCore.ParameterSet.Config as cms

hltSiPixelRecHits = cms.EDProducer('SiPixelRecHitFromSoAAlpaka',
    pixelRecHitSrc = cms.InputTag('hltPhase2SiPixelRecHitsSoA'),
    src = cms.InputTag('hltSiPixelClusters'),
)

_hltSiPixelRecHits = cms.EDProducer("SiPixelRecHitConverter",
    CPE = cms.string('PixelCPEGeneric'),
    src = cms.InputTag("hltSiPixelClusters")
)

from Configuration.ProcessModifiers.hltPhase2LegacyTracking_cff import hltPhase2LegacyTracking
hltPhase2LegacyTracking.toReplaceWith(hltSiPixelRecHits, _hltSiPixelRecHits)
