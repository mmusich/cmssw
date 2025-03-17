import FWCore.ParameterSet.Config as cms

from EventFilter.HGCalRawToDigi.HGCalRawToDigiFake import HGCalRawToDigiFake as _HGCalRawToDigiFake

hltHgcalDigis = _HGCalRawToDigiFake(
    bhDigis = cms.InputTag("simHGCalUnsuppressedDigis","HEback"),
    eeDigis = cms.InputTag("simHGCalUnsuppressedDigis","EE"),
    fhDigis = cms.InputTag("simHGCalUnsuppressedDigis","HEfront"),
    mightGet = cms.optional.untracked.vstring
)
