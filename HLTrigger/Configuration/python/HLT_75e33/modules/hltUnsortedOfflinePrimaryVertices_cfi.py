import FWCore.ParameterSet.Config as cms

from RecoVertex.PrimaryVertexProducer.PrimaryVertexProducer import PrimaryVertexProducer as _PrimaryVertexProducer

hltUnsortedOfflinePrimaryVertices = _PrimaryVertexProducer(
    TkClusParameters = dict(
        TkDAClusParameters = dict(
            Tmin = 2.0,
            Tpurge = 2.0,
            Tstop = 0.5,
            coolingFactor = 0.6,
            d0CutOff = 3.0,
            dzCutOff = 3.0,
            uniquetrkweight = 0.8,
            vertexSize = 0.006,
            zmerge = 0.01
        ),
        algorithm = 'DA_vect'
    ),
    TkFilterParameters = dict(
        algorithm = 'filter',
        maxD0Significance = 4.0,
        maxEta = 4.0,
        maxNormalizedChi2 = 10.0,
        minPixelLayersWithHits = 2,
        minPt = 0.9,
        minSiliconLayersWithHits = 5,
        trackQuality = 'any'
    ),
    TrackLabel = ("hltGeneralTracks"),
    beamSpotLabel = ("hltOnlineBeamSpot"),
    verbose = cms.untracked.bool(False),
    vertexCollections = [
        dict(
            algorithm = 'AdaptiveVertexFitter',
            chi2cutoff = 2.5,
            label = '',
            maxDistanceToBeam = 1.0,
            minNdof = 0.0,
            useBeamConstraint = False
        ),
        dict(
            algorithm = 'AdaptiveVertexFitter',
            chi2cutoff = 2.5,
            label = 'WithBS',
            maxDistanceToBeam = 1.0,
            minNdof = 2.0,
            useBeamConstraint = True
        )
    ]
)
