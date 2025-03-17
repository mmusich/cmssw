import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.HLTBool import HLTBool as _HLTBool

hltBoolFalse = _HLTBool(
    result = cms.bool(False)
)
