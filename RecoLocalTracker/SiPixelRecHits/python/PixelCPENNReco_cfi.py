import FWCore.ParameterSet.Config as cms

from RecoLocalTracker.SiPixelRecHits._templates_default_cfi import _templates_default
templates = _templates_default.clone()

from RecoTracker.FinalTrackSelectors.tfGraphDefProducer_cfi import tfGraphDefProducer as _tfGraphDefProducer
tracksterSelectionTf = _tfGraphDefProducer.clone(
    ComponentName = "tracksterSelectionTf",
    FileName = "/uscms_data/d3/ssekhar/CMSSW_11_1_2/src/TrackerStuff/PixelHitsCNN/data/graph_x_1dcnn_p1_2024_by25k_irrad_BPIXL1_022122.pb"
)