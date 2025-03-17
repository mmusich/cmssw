import FWCore.ParameterSet.Config as cms

from RecoHGCal.TICL.TICLSeedingRegionProducer import TICLSeedingRegionProducer as _TICLSeedingRegionProducer

hltTiclSeedingGlobal = _TICLSeedingRegionProducer(
    mightGet = cms.optional.untracked.vstring,
    seedingPSet = dict(
        algo_verbosity = 0,
        type = cms.string('SeedingRegionGlobal')
    )
)
