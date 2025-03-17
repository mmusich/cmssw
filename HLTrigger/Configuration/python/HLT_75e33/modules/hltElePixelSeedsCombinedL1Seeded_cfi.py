import FWCore.ParameterSet.Config as cms

from RecoTracker.TkSeedGenerator.SeedCombiner import SeedCombiner as _SeedCombiner

hltElePixelSeedsCombinedL1Seeded = _SeedCombiner(
    seedCollections = cms.VInputTag("hltElePixelSeedsDoubletsL1Seeded", "hltElePixelSeedsTripletsL1Seeded")
)
