import FWCore.ParameterSet.Config as cms

from RecoTracker.TkSeedGenerator.SeedCombiner import SeedCombiner as _SeedCombiner

hltElePixelSeedsCombinedUnseeded = _SeedCombiner(
    seedCollections = cms.VInputTag("hltElePixelSeedsDoubletsUnseeded", "hltElePixelSeedsTripletsUnseeded")
)
