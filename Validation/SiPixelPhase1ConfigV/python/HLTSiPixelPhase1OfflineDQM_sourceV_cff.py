import FWCore.ParameterSet.Config as cms

# Hits
from Validation.SiPixelPhase1HitsV.SiPixelPhase1HitsV_cfi import SiPixelPhase1HitsAnalyzerV as _SiPixelPhase1HitsAnalyzerV
hltSiPixelPhase1HitsAnalyzerV = _SiPixelPhase1HitsAnalyzerV.clone(
    trackAssociatorByHitsTag = "hltTrackAssociatorByHits",
    tracksTag = "hltMergedTracks",
    histograms = [h.clone(topFolderName="HLT/PixelPhase1V/Hits") 
                  for h in _SiPixelPhase1HitsAnalyzerV.histograms]
)

# RecHit (clusters)
from Validation.SiPixelPhase1RecHitsV.SiPixelPhase1RecHitsV_cfi import SiPixelPhase1RecHitsAnalyzerV as _SiPixelPhase1RecHitsAnalyzerV
hltSiPixelPhase1RecHitsAnalyzerV = _SiPixelPhase1RecHitsAnalyzerV.clone(
    src = "hltSiPixelRecHits",
    histograms = [h.clone(topFolderName="HLT/PixelPhase1V/RecHits")
                  for h in _SiPixelPhase1RecHitsAnalyzerV.histograms]
)

# Clusters ontrack/offtrack (also hlt merged tracks)
from Validation.SiPixelPhase1TrackClustersV.SiPixelPhase1TrackClustersV_cfi import SiPixelPhase1TrackClustersAnalyzerV as _SiPixelPhase1TrackClustersAnalyzerV
hltSiPixelPhase1TrackClustersAnalyzerV = _SiPixelPhase1TrackClustersAnalyzerV.clone(
    clusters = cms.InputTag("hltSiPixelClusters"),
    tracks = cms.InputTag("hltMergedTracks"),
    histograms = [h.clone(topFolderName="HLT/PixelPhase1V/Clusters")
                  for h in _SiPixelPhase1TrackClustersAnalyzerV.histograms]
)

# the sequence
hltSiPixelPhase1OfflineDQM_sourceV = cms.Sequence(hltSiPixelPhase1HitsAnalyzerV +
                                                  hltSiPixelPhase1RecHitsAnalyzerV +
                                                  hltSiPixelPhase1TrackClustersAnalyzerV)

### Pixel Tracking-only configuration

# # Pixel clusters
# hltPixelOnlyTrackClustersAnalyzerV = hltSiPixelPhase1TrackClustersAnalyzerV.clone(
#     clusters = 'hltSiPixelClusters',
#     tracks = 'hltPixelTracks'
# )

# # Pixel rechit analyzer
# hltPixelOnlyRecHitsAnalyzerV = hltSiPixelPhase1RecHitsAnalyzerV.clone(
#     src = 'hltSiPixelRecHits',
#     pixelSimLinkSrc = 'simSiPixelDigis',
#     ROUList = ('TrackerHitsPixelBarrelLowTof',
#                'TrackerHitsPixelBarrelHighTof',
#                'TrackerHitsPixelEndcapLowTof',
#                'TrackerHitsPixelEndcapHighTof')
# )

# # Pixel hits
# hltPixelOnlyHitsAnalyzerV = hltSiPixelPhase1HitsAnalyzerV.clone(
#     tracksTag = 'hltPixelTracks'
# )

# hltSiPixelPhase1ValidationPixelTrackingOnly_sourceV = cms.Sequence(hltPixelOnlyTrackClustersAnalyzerV +
#                                                                    hltPixelOnlyHitsAnalyzerV +
#                                                                    hltPixelOnlyRecHitsAnalyzerV
# )
