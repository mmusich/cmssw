import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.HLT1PFMET import HLT1PFMET as _HLT1PFMET

hltPFPuppiMETTypeOne140 = _HLT1PFMET(
    MaxEta = -1.0,
    MaxMass = -1.0,
    MinE = -1.0,
    MinEta = -1.0,
    MinMass = -1.0,
    MinN = 1,
    MinPt = 140.0,
    inputTag = ("hltPFPuppiMETTypeOne"),
    saveTags = True,
    triggerType = 87
)
