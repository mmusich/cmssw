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
    src = "hltSiPixelRecHits"
)

# Clusters ontrack/offtrack (also hlt merged tracks)
from Validation.SiPixelPhase1TrackClustersV.SiPixelPhase1TrackClustersV_cfi import SiPixelPhase1TrackClustersAnalyzerV as _SiPixelPhase1TrackClustersAnalyzerV
hltSiPixelPhase1TrackClustersAnalyzerV = _SiPixelPhase1TrackClustersAnalyzerV.clone(
    clusters = cms.InputTag("hltSiPixelClusters"),
    tracks = cms.InputTag("hltMergedTracks"),    
)

hltSiPixelPhase1OfflineDQM_sourceV = cms.Sequence(hltSiPixelPhase1HitsAnalyzerV + hltSiPixelPhase1RecHitsAnalyzerV + hltSiPixelPhase1TrackClustersAnalyzerV)

### Pixel Tracking-only configurations for the GPU workflow

# # Pixel clusters
# pixelOnlyTrackClustersAnalyzerV = SiPixelPhase1TrackClustersAnalyzerV.clone(
#     clusters = 'siPixelClustersPreSplitting',
#     tracks = 'pixelTracks'
# )

# # Pixel rechit analyzer
# pixelOnlyRecHitsAnalyzerV = SiPixelPhase1RecHitsAnalyzerV.clone(
#     src = 'siPixelRecHitsPreSplitting',
#     pixelSimLinkSrc = 'simSiPixelDigis',
#     ROUList = ('TrackerHitsPixelBarrelLowTof',
#                'TrackerHitsPixelBarrelHighTof',
#                'TrackerHitsPixelEndcapLowTof',
#                'TrackerHitsPixelEndcapHighTof')
# )

# # Pixel hits
# pixelOnlyHitsAnalyzerV = SiPixelPhase1HitsAnalyzerV.clone(
#     tracksTag = 'pixelTracks'
# )

# # Tracking particles
# pixelOnlyTrackingParticleAnalyzerV = SiPixelPhase1TrackingParticleAnalyzerV.clone()

# siPixelPhase1ValidationPixelTrackingOnly_sourceV = cms.Sequence(pixelOnlyDigisAnalyzerV 
#                                                                 + pixelOnlyTrackClustersAnalyzerV 
#                                                                 + pixelOnlyHitsAnalyzerV
#                                                                 + pixelOnlyRecHitsAnalyzerV
#                                                                 + pixelOnlyTrackingParticleAnalyzerV
# )
