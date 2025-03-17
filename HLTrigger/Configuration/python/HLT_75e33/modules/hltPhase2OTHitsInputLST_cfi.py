import FWCore.ParameterSet.Config as cms

from RecoTracker.LST.LSTPhase2OTHitsInputProducer import LSTPhase2OTHitsInputProducer as _LSTPhase2OTHitsInputProducer

hltPhase2OTHitsInputLST = _LSTPhase2OTHitsInputProducer(
    phase2OTRecHits = cms.InputTag('hltSiPhase2RecHits'),
    mightGet = cms.optional.untracked.vstring
)
