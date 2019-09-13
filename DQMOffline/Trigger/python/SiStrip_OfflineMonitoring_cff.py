import FWCore.ParameterSet.Config as cms

## SiStripCluster converter
#import EventFilter.SiStripRawToDigi.SiStripRawToClustersHLTdsvbuilder_cff
#HLTsiStripClusters = EventFilter.SiStripRawToDigi.SiStripRawToClustersHLTdsvbuilder_cff.siStripClusters.clone()
#HLTsiStripClusters.SiStripLazyGetter = cms.InputTag("hltSiStripRawToClustersFacility")
#HLTsiStripClusters.SiStripRefGetter  = cms.InputTag("hltSiStripClusters")

# SiStripCluster monitoring
import DQM.SiStripMonitorCluster.SiStripMonitorCluster_cfi
HLTSiStripMonitorCluster = DQM.SiStripMonitorCluster.SiStripMonitorCluster_cfi.SiStripMonitorCluster.clone()
HLTSiStripMonitorCluster.ClusterProducerStrip = cms.InputTag("hltSiStripRawToClustersFacility")
HLTSiStripMonitorCluster.ClusterProducerPix   = cms.InputTag("hltSiPixelClusters")
HLTSiStripMonitorCluster.TopFolderName        = cms.string("HLT/SiStrip")
HLTSiStripMonitorCluster.TH1TotalNumberOfClusters.subdetswitchon   = cms.bool(True)
HLTSiStripMonitorCluster.TProfClustersApvCycle.subdetswitchon      = cms.bool(False)
HLTSiStripMonitorCluster.TProfTotalNumberOfClusters.subdetswitchon = cms.bool(True)
HLTSiStripMonitorCluster.TH2CStripVsCpixel.globalswitchon       = cms.bool(True)
HLTSiStripMonitorCluster.TH1MultiplicityRegions.globalswitchon  = cms.bool(True)
HLTSiStripMonitorCluster.TH1MainDiagonalPosition.globalswitchon = cms.bool(True)
HLTSiStripMonitorCluster.TH1StripNoise2ApvCycle.globalswitchon  = cms.bool(False)
HLTSiStripMonitorCluster.TH1StripNoise3ApvCycle.globalswitchon  = cms.bool(False)
HLTSiStripMonitorCluster.ClusterHisto = cms.bool(True)
HLTSiStripMonitorCluster.Mod_On            = cms.bool(False)
HLTSiStripMonitorCluster.BPTXfilter = cms.PSet(
        andOr         = cms.bool( False ),
            dbLabel       = cms.string("SiStripDQMTrigger"),
            l1Algorithms = cms.vstring( 'L1Tech_BPTX_plus_AND_minus.v0', 'L1_ZeroBias' ),
            andOrL1       = cms.bool( True ),
            errorReplyL1  = cms.bool( True ),
            l1BeforeMask  = cms.bool( True ) # specifies, if the L1 algorithm decision should be read as before (true) or after (false) masking is applied.
        )
HLTSiStripMonitorCluster.PixelDCSfilter = cms.PSet(
        andOr         = cms.bool( False ),
            dcsInputTag   = cms.InputTag( "scalersRawToDigi" ),
            dcsPartitions = cms.vint32 ( 28, 29),
            andOrDcs      = cms.bool( False ),
            errorReplyDcs = cms.bool( True ),
        )
HLTSiStripMonitorCluster.StripDCSfilter = cms.PSet(
        andOr         = cms.bool( False ),
            dcsInputTag   = cms.InputTag( "scalersRawToDigi" ),
            dcsPartitions = cms.vint32 ( 24, 25, 26, 27 ),
            andOrDcs      = cms.bool( False ),
            errorReplyDcs = cms.bool( True ),
        )
HLTSiStripMonitorCluster.TH2CStripVsCpixel = cms.PSet(
        Nbinsx = cms.int32(200),
        xmin   = cms.double(-0.5),
        xmax   = cms.double(99999.5),
        Nbinsy = cms.int32(170),
        ymin   = cms.double(-0.5),
        ymax   = cms.double(50999.5),
        globalswitchon = cms.bool(True)
        )
HLTSiStripMonitorCluster.TH1NClusPx = cms.PSet(
        Nbinsx = cms.int32(170),
        xmax = cms.double(50999.5),
        xmin = cms.double(-0.5)
        )
HLTSiStripMonitorCluster.TH1NClusStrip = cms.PSet(
        Nbinsx = cms.int32(200),
        xmax = cms.double(99999.5),
        xmin = cms.double(-0.5)
    )

from RecoLocalTracker.SiPixelRecHits.PixelCPETemplateReco_cfi import templates
hltESPPixelCPETemplateReco = templates.clone(
    ComponentName = cms.string( "hltESPPixelCPETemplateReco" )
)

from RecoLocalTracker.SiPixelRecHits.PixelCPEGeneric_cfi import PixelCPEGenericESProducer
hltESPPixelCPEGeneric = PixelCPEGenericESProducer.clone(
    ComponentName = cms.string( "hltESPPixelCPEGeneric" )
)

hltESPTTRHBuilderAngleAndTemplate = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPETemplateReco" ),
  ComponentName = cms.string( "hltESPTTRHBuilderAngleAndTemplate" )
)

hltESPTTRHBWithTrackAngle = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBWithTrackAngle" )
)

hltESPStripCPEfromTrackAngle = cms.ESProducer( "StripCPEESProducer",
  ComponentType = cms.string( "StripCPEfromTrackAngle" ),
  ComponentName = cms.string( "hltESPStripCPEfromTrackAngle" ),
  parameters = cms.PSet( 
    mLC_P2 = cms.double( 0.3 ),
    mLC_P1 = cms.double( 0.618 ),
    mLC_P0 = cms.double( -0.326 ),
    useLegacyError = cms.bool( True ),
    mTEC_P1 = cms.double( 0.471 ),
    mTEC_P0 = cms.double( -1.885 ),
    mTOB_P0 = cms.double( -1.026 ),
    mTOB_P1 = cms.double( 0.253 ),
    mTIB_P0 = cms.double( -0.742 ),
    mTIB_P1 = cms.double( 0.202 ),
    mTID_P0 = cms.double( -1.427 ),
    mTID_P1 = cms.double( 0.433 )
  )
)

from RecoTracker.TrackProducer.TrackRefitter_cfi import *
hltTrackRefitterForSiStripMonitorTrack = TrackRefitter.clone()
hltTrackRefitterForSiStripMonitorTrack.beamSpot                = cms.InputTag("hltOnlineBeamSpot")
hltTrackRefitterForSiStripMonitorTrack.MeasurementTrackerEvent = cms.InputTag('MeasurementTrackerEvent')
hltTrackRefitterForSiStripMonitorTrack.TrajectoryInEvent       = cms.bool(True)
hltTrackRefitterForSiStripMonitorTrack.useHitsSplitting        = cms.bool(False)
#hltTrackRefitterForSiStripMonitorTrack.src                     = cms.InputTag("hltIter4Merged") # scenario 0
hltTrackRefitterForSiStripMonitorTrack.src                     = cms.InputTag("hltMergedTracks") # hltIter2Merged # scenario 1
#hltTrackRefitterForSiStripMonitorTrack.TTRHBuilder             = cms.string('hltESPTTRHBuilderAngleAndTemplate')
hltTrackRefitterForSiStripMonitorTrack.TTRHBuilder             = cms.string('hltESPTTRHBWithTrackAngle')

import DQM.SiStripMonitorTrack.SiStripMonitorTrack_cfi
HLTSiStripMonitorTrack = DQM.SiStripMonitorTrack.SiStripMonitorTrack_cfi.SiStripMonitorTrack.clone()
HLTSiStripMonitorTrack.TrackProducer     = 'hltTrackRefitterForSiStripMonitorTrack' 
HLTSiStripMonitorTrack.TrackLabel        = ''
HLTSiStripMonitorTrack.AlgoName          = cms.string("HLT")
HLTSiStripMonitorTrack.Cluster_src       = cms.InputTag('hltSiStripRawToClustersFacility')
HLTSiStripMonitorTrack.Trend_On          = cms.bool(True)
HLTSiStripMonitorTrack.TopFolderName     = cms.string('HLT/SiStrip')
HLTSiStripMonitorTrack.Mod_On            = cms.bool(False)
sistripMonitorHLTsequence = cms.Sequence(
    HLTSiStripMonitorCluster
    * hltTrackRefitterForSiStripMonitorTrack
    * HLTSiStripMonitorTrack
)    

