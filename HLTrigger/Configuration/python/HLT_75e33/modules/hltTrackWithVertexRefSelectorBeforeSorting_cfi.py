import FWCore.ParameterSet.Config as cms

from CommonTools.RecoAlgos.TrackWithVertexRefSelector import TrackWithVertexRefSelector as _TrackWithVertexRefSelector

hltTrackWithVertexRefSelectorBeforeSorting = _TrackWithVertexRefSelector(
    d0Max = 999.0,
    dzMax = 999.0,
    etaMax = 5.0,
    etaMin = 0.0,
    nSigmaDtVertex = 0,
    nVertices = 0,
    normalizedChi2 = 999999.0,
    numberOfLostHits = 999,
    numberOfValidHits = 0,
    numberOfValidPixelHits = 0,
    ptErrorCut = 9e+99,
    ptMax = 9e+99,
    ptMin = 0.9,
    quality = cms.string('highPurity'),
    rhoVtx = 0.2,
    src = ("hltGeneralTracks"),
    timeResosTag = (""),
    timesTag = (""),
    useVtx = True,
    vertexTag = ("hltUnsortedOfflinePrimaryVertices"),
    vtxFallback = True,
    zetaVtx = 1.0
)
