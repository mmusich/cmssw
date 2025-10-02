import FWCore.ParameterSet.Config as cms

process = cms.Process("FEDMove")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/data/Run2025D/EphemeralHLTPhysics0/RAW/v1/000/394/959/00000/02ab3d20-66ba-4372-8f06-5d09e0848408.root'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)  # process all events
)

process.rawDataCollector = cms.EDProducer('CopyAndMoveFED1024',
                                          src = cms.InputTag('rawDataCollector')
                                          )

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string("modifiedFEDs.root"),
    outputCommands = cms.untracked.vstring('drop FEDRawDataCollection_rawDataCollector_*_LHC',                                           
                                           "keep *")
)

process.p = cms.Path(process.rawDataCollector)
process.e = cms.EndPath(process.out)
