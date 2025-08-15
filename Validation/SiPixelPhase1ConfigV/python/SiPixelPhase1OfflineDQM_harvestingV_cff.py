import FWCore.ParameterSet.Config as cms

from Validation.SiPixelPhase1ConfigV.SiPixelPhase1OfflineDQM_sourceV_cff import *

# the sequence
siPixelPhase1OfflineDQM_harvestingV = cms.Sequence(SiPixelPhase1DigisHarvesterV
                                                   + SiPixelPhase1RecHitsHarvesterV
                                                   + SiPixelPhase1HitsHarvesterV
                                                   + SiPixelPhase1TrackClustersHarvesterV
                                                   + SiPixelPhase1TrackingParticleHarvesterV)

