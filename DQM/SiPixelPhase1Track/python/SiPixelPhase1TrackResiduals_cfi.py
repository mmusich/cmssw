import FWCore.ParameterSet.Config as cms
from DQMServices.Core.DQMEDHarvester import DQMEDHarvester
from DQM.SiPixelPhase1Common.HistogramManager_cfi import *
import DQM.SiPixelPhase1Common.TriggerEventFlag_cfi as trigger

SiPixelPhase1TrackResidualsResidualsX = DefaultHistoTrack.clone(
  name = "residual_x",
  title = "Track Residuals X",
  range_min = -0.1, range_max = 0.1, range_nbins = 100,
  xlabel = "(x_rec - x_pred) [cm]",
  dimensions = 1,
  specs = VPSet(
    StandardSpecification2DProfile,
    Specification().groupBy("PXBarrel/PXLayer").saveAll(),
    Specification().groupBy("PXForward/PXDisk").saveAll(),
    
    Specification().groupBy("PXBarrel/PXLayer/LumiBlock")
                   .reduce("MEAN")
                   .groupBy("PXBarrel/PXLayer", "EXTEND_X")
                   .save(),

    Specification().groupBy("PXForward/PXDisk/LumiBlock")
                   .reduce("MEAN")
                   .groupBy("PXForward/PXDisk", "EXTEND_X")
                   .save(),

    Specification(PerLayer1D).groupBy("PXBarrel/Shell/PXLayer").save(),
    Specification(PerLayer1D).groupBy("PXForward/HalfCylinder/PXRing/PXDisk").save()
  )
)

SiPixelPhase1TrackResidualsResidualsY = SiPixelPhase1TrackResidualsResidualsX.clone(
  name = "residual_y",
  title = "Track Residuals Y",
  xlabel = "(y_rec - y_pred) [cm]",
)

SiPixelPhase1TrackResidualsResidualsEdgeX = SiPixelPhase1TrackResidualsResidualsX.clone(
    title = "Track Residuals X (edge pixel clusters)",
    name = "resondedge_x",
)

SiPixelPhase1TrackResidualsResidualsEdgeY = SiPixelPhase1TrackResidualsResidualsY.clone(
    title = "Track Residuals Y (edge pixel clusters)",
    name = "resondedge_y",
)

SiPixelPhase1TrackResidualsResidualsOtherBadX = SiPixelPhase1TrackResidualsResidualsX.clone(
    title = "Track Residuals X (other bad pixel clusters)",
    name = "resotherbad_x",
)

SiPixelPhase1TrackResidualsResidualsOtherBadY = SiPixelPhase1TrackResidualsResidualsY.clone(
    title = "Track Residuals Y (other bad pixel clusters)",
    name = "resotherbad_y",
)

SiPixelPhase1TrackResidualsConf = cms.VPSet(
    SiPixelPhase1TrackResidualsResidualsX,
    SiPixelPhase1TrackResidualsResidualsY,
    SiPixelPhase1TrackResidualsResidualsEdgeX,
    SiPixelPhase1TrackResidualsResidualsEdgeY,
    SiPixelPhase1TrackResidualsResidualsOtherBadX,
    SiPixelPhase1TrackResidualsResidualsOtherBadY
)

from DQMServices.Core.DQMEDAnalyzer import DQMEDAnalyzer
SiPixelPhase1TrackResidualsAnalyzer = DQMEDAnalyzer('SiPixelPhase1TrackResiduals',
        trajectoryInput = cms.string("generalTracks"),
        Tracks        = cms.InputTag("generalTracks"),
        vertices = cms.InputTag("offlinePrimaryVertices"),
        histograms = SiPixelPhase1TrackResidualsConf,
        geometry = SiPixelPhase1Geometry,
        triggerflags = trigger.SiPixelPhase1Triggers
)

SiPixelPhase1TrackResidualsHarvester = DQMEDHarvester("SiPixelPhase1Harvester",
        histograms = SiPixelPhase1TrackResidualsConf,
        geometry = SiPixelPhase1Geometry
)
