# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --conditions auto:run1_data -s RAW2DIGI,L1Reco,RECO,EI,ALCAPRODUCER:@allForExpress,DQM:@express,ENDJOB --process RECO --data --eventcontent ALCARECO,DQM --runUnscheduled --scenario pp --datatier ALCARECO,DQMIO --customise Configuration/DataProcessing/RecoTLR.customiseExpress -n 100 --filein filelist:step1_dasquery.log --lumiToProcess step1_lumiRanges.log --fileout file:step2.root
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('CommonTools.ParticleFlow.EITopPAG_cff')
process.load('Configuration.StandardSequences.AlCaRecoStreams_cff')
process.load('DQMOffline.Configuration.DQMOffline_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/0699429A-B37F-E011-A57A-0019B9F72D71.root', 
        '/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/18E0AF9F-BA7F-E011-AC1C-001D09F24259.root', 
        '/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/1E9D751C-CE7F-E011-A67E-0030487CD6E6.root', 
        '/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/2C1B50CC-C17F-E011-9FE6-003048F1C836.root', 
        '/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/2E2E1830-D17F-E011-BCEA-003048F118AA.root', 
        '/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/36C9058E-BF7F-E011-8AA5-003048F024DC.root', 
        '/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/4C4014A6-D47F-E011-B1FE-003048F1110E.root', 
        '/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/70880A66-C67F-E011-A3C4-003048D2BC42.root', 
        '/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/72315DA9-AD7F-E011-87DF-001D09F28F25.root', 
        '/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/728CF6FF-BC7F-E011-9065-000423D9997E.root', 
        '/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/741732C7-BE7F-E011-A571-0030487A18A4.root', 
        '/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/78ECBE39-B97F-E011-AFA6-003048F110BE.root', 
        '/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/94A66560-B17F-E011-9AE3-001617DBD556.root', 
        '/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/A2E399AE-C57F-E011-84EE-001617E30CC8.root', 
        '/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/A4BFB684-BD7F-E011-A2D9-0019B9F72CE5.root', 
        '/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/B6758760-B77F-E011-BD34-0030486733D8.root', 
        '/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/BAE5AFA1-CA7F-E011-8A31-003048CFB40C.root', 
        '/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/C05A4890-C37F-E011-B3B2-001617E30CC8.root', 
        '/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/C2365AF8-C07F-E011-B9C2-0030487C6062.root', 
        '/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/CC54CF95-AE7F-E011-87DF-003048F1BF66.root', 
        '/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/CCF770BD-B57F-E011-8C09-001D09F29597.root', 
        '/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/FC16AD5B-B47F-E011-83B2-001D09F26C5C.root'),
    lumisToProcess = cms.untracked.VLuminosityBlockRange("165121:1-165121:268435455"),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.ALCARECOoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('StreamALCACombined')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:step2.root'),
    outputCommands = process.ALCARECOEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step2_inDQM.root'),
    outputCommands = process.DQMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOHotline_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOSiStripPCLHistos_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOLumiPixelsMinBias_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOSiStripCalMinBiasAfterAbortGap_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOTkAlMinBias_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOSiStripCalMinBias_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECODtCalib_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOSiStripCalZeroBias_noDrop.outputCommands)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run1_data', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.eventinterpretaion_step = cms.Path(process.EIsequence)
process.dqmoffline_step = cms.EndPath(process.DQMOfflineCommonSiStripZeroBias)
process.dqmoffline_1_step = cms.EndPath(process.DQMOfflineMuon)
process.dqmoffline_2_step = cms.EndPath(process.DQMOfflineHcal)
process.dqmoffline_3_step = cms.EndPath(process.DQMOfflineJetMET)
process.dqmoffline_4_step = cms.EndPath(process.DQMOfflineEcal)
process.dqmofflineOnPAT_step = cms.EndPath(process.PostDQMOffline)
process.ALCARECOoutput_step = cms.EndPath(process.ALCARECOoutput)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.eventinterpretaion_step,process.pathHotlineSkimSingleMuon,process.pathHotlineSkimDoubleMuon,process.pathHotlineSkimTripleMuon,process.pathHotlineSkimSingleElectron,process.pathHotlineSkimDoubleElectron,process.pathHotlineSkimTripleElectron,process.pathHotlineSkimSinglePhoton,process.pathHotlineSkimDoublePhoton,process.pathHotlineSkimTriplePhoton,process.pathHotlineSkimSingleJet,process.pathHotlineSkimDoubleJet,process.pathHotlineSkimMultiJet,process.pathHotlineSkimHT,process.pathHotlineSkimMassiveDimuon,process.pathHotlineSkimMassiveDielectron,process.pathHotlineSkimMassiveEMu,process.pathHotlineSkimPFMET,process.pathHotlineSkimCaloMET,process.pathHotlineSkimCondMET,process.pathALCARECOSiStripPCLHistos,process.pathALCARECOLumiPixelsMinBias,process.pathALCARECOSiStripCalMinBiasAfterAbortGap,process.pathALCARECOTkAlMinBias,process.pathALCARECOSiStripCalMinBias,process.pathALCARECODtCalib,process.pathALCARECOSiStripCalZeroBias,process.dqmoffline_step,process.dqmoffline_1_step,process.dqmoffline_2_step,process.dqmoffline_3_step,process.dqmoffline_4_step,process.dqmofflineOnPAT_step,process.ALCARECOoutput_step,process.DQMoutput_step)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.RecoTLR
from Configuration.DataProcessing.RecoTLR import customiseExpress 

#call to customisation function customiseExpress imported from Configuration.DataProcessing.RecoTLR
process = customiseExpress(process)

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)
from FWCore.ParameterSet.Utilities import cleanUnscheduled
process=cleanUnscheduled(process)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
