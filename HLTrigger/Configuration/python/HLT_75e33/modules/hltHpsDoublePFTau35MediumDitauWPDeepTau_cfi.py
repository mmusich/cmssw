import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.HLT1PFTau import HLT1PFTau as _HLT1PFTau

hltHpsDoublePFTau35MediumDitauWPDeepTau = _HLT1PFTau(
    MaxEta = cms.double(2.1),
    MaxMass = cms.double(-1.0),
    MinE = cms.double(-1.0),
    MinEta = cms.double(-1.0),
    MinMass = cms.double(-1.0),
    MinN = cms.int32(2),
    MinPt = cms.double(35.0),
    inputTag = cms.InputTag("hltHpsSelectedPFTausMediumDitauWPDeepTau"),
    saveTags = cms.bool(True),
    triggerType = cms.int32(84)
)
