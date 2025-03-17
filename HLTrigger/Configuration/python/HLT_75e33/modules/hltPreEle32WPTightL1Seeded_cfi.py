import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTcore.HLTPrescaler import HLTPrescaler as _HLTPrescaler

hltPreEle32WPTightL1Seeded = _HLTPrescaler(
    L1GtReadoutRecordTag = ("hltGtStage2Digis"),
    offset = 0
)
