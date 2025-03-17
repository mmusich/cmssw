import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Type1MET.CorrectedPFMETProducer import CorrectedPFMETProducer as _CorrectedPFMETProducer

hltPFPuppiMETTypeOne = _CorrectedPFMETProducer(
    src = cms.InputTag("hltPFPuppiMET"),
    srcCorrections = cms.VInputTag("hltPFPuppiMETTypeOneCorrector:type1")
)
