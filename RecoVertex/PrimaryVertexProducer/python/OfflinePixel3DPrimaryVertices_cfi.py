import FWCore.ParameterSet.Config as cms
from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import offlinePrimaryVertices

pixelVertices = offlinePrimaryVertices.clone(
    TrackLabel = "pixelTracks",

    TkFilterParameters = dict(
        maxNormalizedChi2 = 100.0,
        minPixelLayersWithHits=3,
        minSiliconLayersWithHits = 3,
        maxD0Significance = 100.0, 
        maxEta = 100.,
    ),

     TkClusParameters = cms.PSet(
        algorithm   = cms.string("DA_vect"),
        TkDAClusParameters = cms.PSet(
            dzCutOff = cms.double(4.),        # outlier rejection after freeze-out (T<Tmin)
            Tmin = cms.double(2.4),           # end of vertex splitting, (adjusted for Pixel vertices)
            vertexSize = cms.double(0.01),    # added in quadrature to track-z resolution (adjusted for Pixel vertices)
            uniquetrkweight = cms.double(0.9),# require at least two tracks with this weight at T=Tpurge
            coolingFactor = cms.double(0.6),  # moderate annealing speed
            zrange = cms.double(4.),          # consider only clusters within 4 sigma*sqrt(T) of a track
            delta_highT = cms.double(1.e-2),  # convergence requirement at high T
            delta_lowT = cms.double(1.e-3),   # convergence requirement at low T
            convergence_mode = cms.int32(0),  # 0 = two steps, 1 = dynamic with sqrt(T)
            Tpurge = cms.double(2.0),         # cleaning
            Tstop = cms.double(0.5),          # end of annealing
            d0CutOff = cms.double(3.),        # downweight high IP tracks (adjusted for Pixel vertices)
            zmerge = cms.double(1e-2),        # merge intermediat clusters separated by less than zmerge
            uniquetrkminp = cms.double(0.0),  # minimal a priori track weight for counting unique tracks
            runInBlocks = cms.bool(False),    # activate the DA running in blocks of z sorted tracks
            block_size = cms.uint32(10000),   # block size in tracks
            overlap_frac = cms.double(0.0)    # overlap between consecutive blocks (blocks_size*overlap_frac)
        )
     ),

    vertexCollections = cms.VPSet(
     [cms.PSet(label=cms.string(""),
               algorithm=cms.string("AdaptiveVertexFitter"),
               chi2cutoff = cms.double(3.0),
               minNdof=cms.double(2.0),
               useBeamConstraint = cms.bool(False),
               maxDistanceToBeam = cms.double(2.0)
               )
      ]
    )
)

from Configuration.Eras.Modifier_pp_on_XeXe_2017_cff import pp_on_XeXe_2017
from Configuration.ProcessModifiers.pp_on_AA_cff import pp_on_AA
(pp_on_XeXe_2017 | pp_on_AA).toModify(pixelVertices,
               TkFilterParameters = dict(
                   algorithm="filterWithThreshold",
                   maxD0Significance = 2.0,
                   maxD0Error = 10.0,
                   maxDzError = 10.0,
                   minPixelLayersWithHits = 3,
                   minPt = 0.7,
                   trackQuality = "highPurity",
                   numTracksThreshold = cms.int32(10),
                   maxNumTracksThreshold = cms.int32(1000),
                   minPtTight = cms.double(1.0)
               ),
               TkClusParameters = cms.PSet(
                 algorithm = cms.string("gap"),
                 TkGapClusParameters = cms.PSet(
                   zSeparation = cms.double(1.0)
                 )
               )
)
