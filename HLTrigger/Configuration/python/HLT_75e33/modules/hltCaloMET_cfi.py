import FWCore.ParameterSet.Config as cms

from RecoMET.METProducers.CaloMETProducer import CaloMETProducer as _CaloMETProducer

hltCaloMET = _CaloMETProducer(
    alias = cms.string('RawCaloMET'),
    calculateSignificance = cms.bool(False),
    globalThreshold = cms.double(0.3),
    noHF = cms.bool(False),
    src = cms.InputTag("hltTowerMaker")
)
