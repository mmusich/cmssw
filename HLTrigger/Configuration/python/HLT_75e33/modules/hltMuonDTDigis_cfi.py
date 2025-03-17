import FWCore.ParameterSet.Config as cms

from EventFilter.DTRawToDigi.DTuROSRawToDigi import DTuROSRawToDigi as _DTuROSRawToDigi

hltMuonDTDigis = _DTuROSRawToDigi(
    debug = cms.untracked.bool(False),
    inputLabel = ("rawDataCollector")
)
