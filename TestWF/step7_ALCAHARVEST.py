# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step7 --data --conditions auto:run1_data --scenario pp -s ALCAHARVEST:SiPixelAli --filein file:PromptCalibProdSiPixelAli.root -n 100
import FWCore.ParameterSet.Config as cms

process = cms.Process('ALCAHARVEST')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.AlCaHarvesting_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:PromptCalibProdSiPixelAli.root'),
    processingMode = cms.untracked.string('RunsAndLumis'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound'),
    fileMode = cms.untracked.string('FULLMERGE')
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step7 nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

# Additional output definition

# Other statements
process.PoolDBOutputService.toPut.append(process.ALCAHARVESTSiPixelAli_dbOutput)
process.pclMetadataWriter.recordsToMap.append(process.ALCAHARVESTSiPixelAli_metadata)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run1_data', '')
process.GlobalTag.toGet = cms.VPSet(
    cms.PSet(connect = cms.string("sqlite_file:mythresholds.db"),
             record = cms.string('AlignPCLThresholdsRcd'),
             tag = cms.string('PCLThresholds_express_v0') # choose tag you want
             )
    )

# Path and EndPath definitions
process.SiStripGains = cms.Path(process.ALCAHARVESTSiStripGains)
process.SiStripGainsAfterAbortGap = cms.Path(process.ALCAHARVESTSiStripGainsAfterAbortGap)
process.BeamSpotByRun = cms.Path(process.ALCAHARVESTBeamSpotByRun)
process.ALCAHARVESTDQMSaveAndMetadataWriter = cms.Path(process.dqmSaver+process.pclMetadataWriter)
process.SiPixelAli = cms.Path(process.ALCAHARVESTSiPixelAli)
process.BeamSpotByLumi = cms.Path(process.ALCAHARVESTBeamSpotByLumi)
process.SiStripQuality = cms.Path(process.ALCAHARVESTSiStripQuality)

# Schedule definition
process.schedule = cms.Schedule(process.SiPixelAli,process.ALCAHARVESTDQMSaveAndMetadataWriter)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
