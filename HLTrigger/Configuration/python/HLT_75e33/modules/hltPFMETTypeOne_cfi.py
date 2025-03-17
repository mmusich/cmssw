import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Type1MET.CorrectedPFMETProducer import CorrectedPFMETProducer as _CorrectedPFMETProducer

hltPFMETTypeOne = _CorrectedPFMETProducer(
    src = ("hltPFMET"),
    srcCorrections = cms.VInputTag("hltPFMETTypeOneCorrector:type1")
)
