import FWCore.ParameterSet.Config as cms

# Hits
from Validation.SiPixelPhase1HitsV.SiPixelPhase1HitsV_cfi  import SiPixelPhase1HitsHarvesterV as _SiPixelPhase1HitsHarvesterV
hltSiPixelPhase1HitsHarvesterV = _SiPixelPhase1HitsHarvesterV.clone(
    histograms = [h.clone(topFolderName="HLT/PixelPhase1V/Hits")
                  for h in _SiPixelPhase1HitsHarvesterV.histograms]
)

# RecHit (clusters)
from Validation.SiPixelPhase1RecHitsV.SiPixelPhase1RecHitsV_cfi import SiPixelPhase1RecHitsHarvesterV as _SiPixelPhase1RecHitsHarvesterV
hltSiPixelPhase1RecHitsHarvesterV = _SiPixelPhase1RecHitsHarvesterV.clone(
    histograms = [h.clone(topFolderName="HLT/PixelPhase1V/RecHits")
                  for h in  _SiPixelPhase1RecHitsHarvesterV.histograms]
)

# Clusters ontrack/offtrack (also hlt merged tracks)
from Validation.SiPixelPhase1TrackClustersV.SiPixelPhase1TrackClustersV_cfi import SiPixelPhase1TrackClustersHarvesterV as _SiPixelPhase1TrackClustersHarvesterV
hltSiPixelPhase1TrackClustersHarvesterV = _SiPixelPhase1TrackClustersHarvesterV.clone(
    histograms = [h.clone(topFolderName="HLT/PixelPhase1V/Clusters")
                  for h in _SiPixelPhase1TrackClustersHarvesterV.histograms]
)

# the sequence
hltSiPixelPhase1OfflineDQM_harvestingV = cms.Sequence(hltSiPixelPhase1RecHitsHarvesterV +
                                                   hltSiPixelPhase1HitsHarvesterV +
                                                   hltSiPixelPhase1TrackClustersHarvesterV)
