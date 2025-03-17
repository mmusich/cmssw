import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTcore.TriggerSummaryProducerRAW import TriggerSummaryProducerRAW as _TriggerSummaryProducerRAW

hltTriggerSummaryRAW = _TriggerSummaryProducerRAW(
    processName = cms.string('@')
)
