import FWCore.ParameterSet.Config as cms

from EventFilter.GEMRawToDigi.GEMRawToDigiModule import GEMRawToDigiModule as _GEMRawToDigiModule

hltMuonGEMDigis = _GEMRawToDigiModule(
    InputLabel = cms.InputTag("rawDataCollector"),
    mightGet = cms.optional.untracked.vstring,
    useDBEMap = cms.bool(False)
)
