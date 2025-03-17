import FWCore.ParameterSet.Config as cms

from HLTrigger.special.HLTTriggerTypeFilter import HLTTriggerTypeFilter as _HLTTriggerTypeFilter

hltTriggerType = _HLTTriggerTypeFilter(
    SelectedTriggerType = 1
)
