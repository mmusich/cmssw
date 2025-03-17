import FWCore.ParameterSet.Config as cms

from RecoLocalMuon.GEMRecHit.GEMRecHitProducer import GEMRecHitProducer as _GEMRecHitProducer

hltGemRecHits = _GEMRecHitProducer(
    applyMasking = False,
    deadFile = cms.optional.FileInPath,
    gemDigiLabel = ("simMuonGEMDigis"),
    maskFile = cms.optional.FileInPath,
    mightGet = cms.optional.untracked.vstring,
    recAlgo = cms.string('GEMRecHitStandardAlgo'),
    recAlgoConfig = dict(

    )
)
