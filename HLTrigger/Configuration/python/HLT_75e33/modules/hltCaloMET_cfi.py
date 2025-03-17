import FWCore.ParameterSet.Config as cms

from RecoMET.METProducers.CaloMETProducer import CaloMETProducer as _CaloMETProducer

hltCaloMET = _CaloMETProducer(
    alias = cms.string('RawCaloMET'),
    calculateSignificance = False,
    globalThreshold = 0.3,
    noHF = False,
    src = ("hltTowerMaker")
)
