import FWCore.ParameterSet.Config as cms

from RecoHGCal.TICL.TICLSeedingRegionProducer import TICLSeedingRegionProducer as _TICLSeedingRegionProducer

hltTiclSeedingGlobal = _TICLSeedingRegionProducer(
    mightGet = cms.optional.untracked.vstring,
    seedingPSet = cms.PSet(
        algo_verbosity = cms.int32(0),
        type = cms.string('SeedingRegionGlobal')
    )
)
