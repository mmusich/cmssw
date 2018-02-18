import FWCore.ParameterSet.Config as cms

siPixelStatusHarvester = cms.EDAnalyzer("SiPixelStatusHarvester",

    SiPixelStatusHarvesterParameters = cms.PSet(
	outputBase = cms.untracked.string("nLumibased"), #runbased #dynamicLumibased
        ResetEveryNLumi = cms.untracked.int32(10),
	ModuleName  = cms.untracked.string("siPixelStatusProducer"),
	Label       = cms.untracked.string("siPixelStatus"),
	recordName  = cms.untracked.string("SiPixelQualityFromDbRcd"),
	dumpTxt     = cms.untracked.bool(False),
	txtFileName = cms.untracked.string("SiPixelBadComponent"),
    )
)

