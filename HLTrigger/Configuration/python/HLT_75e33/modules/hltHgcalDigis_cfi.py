import FWCore.ParameterSet.Config as cms

from EventFilter.HGCalRawToDigi.HGCalRawToDigiFake import HGCalRawToDigiFake as _HGCalRawToDigiFake

hltHgcalDigis = _HGCalRawToDigiFake(
    bhDigis = ("simHGCalUnsuppressedDigis","HEback"),
    eeDigis = ("simHGCalUnsuppressedDigis","EE"),
    fhDigis = ("simHGCalUnsuppressedDigis","HEfront"),
    mightGet = cms.optional.untracked.vstring
)
