import FWCore.ParameterSet.Config as cms

from RecoMuon.MuonIdentification.MuonIDFilterProducerForHLT import MuonIDFilterProducerForHLT as _MuonIDFilterProducerForHLT

hltPhase2L3Muons = _MuonIDFilterProducerForHLT(
    allowedTypeMask = 0,
    applyTriggerIdLoose = True,
    inputMuonCollection = ("hltPhase2L3MuonsNoID"),
    maxNormalizedChi2 = 9999.0,
    minNMuonHits = 0,
    minNMuonStations = 0,
    minNTrkLayers = 0,
    minPixHits = 0,
    minPixLayer = 0,
    minPt = 0.0,
    minTrkHits = 0,
    requiredTypeMask = 0,
    typeMuon = 0
)
