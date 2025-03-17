import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTcore.TriggerSummaryProducerAOD import TriggerSummaryProducerAOD as _TriggerSummaryProducerAOD

hltTriggerSummaryAOD = _TriggerSummaryProducerAOD(
    moduleLabelPatternsToMatch = cms.vstring(
        'hlt*',
        'l1t*'
    ),
    moduleLabelPatternsToSkip = [],
    processName = cms.string('*'),
    throw = False
)
