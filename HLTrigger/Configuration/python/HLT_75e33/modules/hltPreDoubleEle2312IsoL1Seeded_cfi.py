import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTcore.HLTPrescaler import HLTPrescaler as _HLTPrescaler

hltPreDoubleEle2312IsoL1Seeded = _HLTPrescaler(
    L1GtReadoutRecordTag = ("hltGtStage2Digis"),
    offset = 0
)
