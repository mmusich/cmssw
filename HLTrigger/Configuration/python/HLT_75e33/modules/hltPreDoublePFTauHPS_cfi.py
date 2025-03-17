import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTcore.HLTPrescaler import HLTPrescaler as _HLTPrescaler

hltPreDoublePFTauHPS = _HLTPrescaler(
    L1GtReadoutRecordTag = ("hltGtStage2Digis"),
    offset = 0
)
