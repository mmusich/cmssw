import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.HLT1PFTau import HLT1PFTau as _HLT1PFTau

hltHpsPFTau30LooseTauWPDeepTau = _HLT1PFTau(
    MaxEta = cms.double(2.1),
    MaxMass = cms.double(-1.0),
    MinE = cms.double(-1.0),
    MinEta = cms.double(-1.0),
    MinMass = cms.double(-1.0),
    MinN = cms.int32(1),
    MinPt = cms.double(30.0),
    inputTag = cms.InputTag("hltHpsSelectedPFTauLooseTauWPDeepTau"),
    saveTags = cms.bool(True),
    triggerType = cms.int32(84)
)
