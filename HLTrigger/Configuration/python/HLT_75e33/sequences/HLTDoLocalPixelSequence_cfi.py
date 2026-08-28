import FWCore.ParameterSet.Config as cms

from ..modules.hltSiPixelClusters_cfi import *
from ..modules.hltSiPixelRecHits_cfi import *
from ..modules.hltPhase2SiPixelClustersSoA_cfi import hltPhase2SiPixelClustersSoA
from ..modules.hltPhase2SiPixelRecHitsSoA_cfi  import hltPhase2SiPixelRecHitsSoA
from ..modules.hltSiPixelClusterShapeCache_cfi import hltSiPixelClusterShapeCache

HLTDoLocalPixelSequence = cms.Sequence(
     hltPhase2SiPixelClustersSoA
    +hltSiPixelClusters
    +hltSiPixelClusterShapeCache  # Currently needed by tracker muons
    +hltPhase2SiPixelRecHitsSoA
    +hltSiPixelRecHits
)

_HLTDoLocalPixelSequence = cms.Sequence(hltSiPixelClusters+
                                        hltSiPixelClusterShapeCache+
                                        hltSiPixelRecHits)

from Configuration.ProcessModifiers.hltPhase2LegacyTracking_cff import hltPhase2LegacyTracking
hltPhase2LegacyTracking.toReplaceWith(HLTDoLocalPixelSequence,_HLTDoLocalPixelSequence)
