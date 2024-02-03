# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step5 -s ALCA:TkAlMuonIsolated --conditions auto:phase2_realistic_T25 --datatier ALCARECO -n -1 --eventcontent ALCARECO --geometry Extended2026D98 --era Phase2C17I13M9 -n -1 --fileout file:step5.root --nThreads 4 --dasquery=file dataset=/RelValSingleMuFlatPt2To100/CMSSW_14_0_0_pre2-133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/GEN-SIM-RECO
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C17I13M9_cff import Phase2C17I13M9

process = cms.Process('ALCA',Phase2C17I13M9)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D98Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.AlCaRecoStreamsMC_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/0f73e103-273c-416c-8fdd-e322aa8de063.root',
        '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/1abd3dd2-bc65-4028-995e-9ad505672d08.root',
        '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/1ffbad78-d003-4a61-869d-46ac2087e80c.root',
        '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/4085c749-1d0b-4264-9a46-6ed926475a6b.root',
        '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/560602b8-bd74-4228-bd95-a49099cc031e.root',
        '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/59292bf8-70e0-4982-a4af-6f27370dfba8.root',
        '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/70b39b48-f2b8-4584-b268-e464aaba3531.root',
        '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/734e7003-ac98-462c-87c8-66dedc28fe8a.root',
        '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/a807ed3e-e844-41b3-b6e1-ea16e6ae9632.root',
        '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/af7f0f95-05f8-42cf-9792-0f8653c651eb.root',
        '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/b0a8ead8-0fcd-48d5-822f-a323925b101a.root',
        '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/b579e360-bb6a-4707-a4c9-9b01f2ce4e7d.root',
        '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/b996f92a-73fd-4e45-9e37-20c7e86c2061.root',
        '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/b9a33790-ba83-4715-b28f-b6c95e19c7ca.root',
        '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/bc8feccd-4e0b-402d-8741-edcb0e7e571b.root',
        '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/bc90c644-bb51-4488-b1d0-b42b2ec7a991.root',
        '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/d3fecec7-889d-442a-9249-fdf2eadbd24b.root',
        '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/d99c2acd-545b-4095-80a8-8f57e77b4551.root',
        '/store/relval/CMSSW_14_0_0_pre2/RelValSingleMuFlatPt2To100/GEN-SIM-RECO/133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/2580000/db45efef-81c1-4da8-99d8-6e491edf0237.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    TryToContinue = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToCallForTryToContinue = cms.untracked.vstring(),
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(8),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step5 nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition


# Additional output definition
process.ALCARECOStreamTkAlMuonIsolated = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlMuonIsolated')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('TkAlMuonIsolated')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('TkAlMuonIsolated.root'),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep recoTracks_ALCARECOTkAlMuonIsolated_*_*',
        'keep recoTrackExtras_ALCARECOTkAlMuonIsolated_*_*',
        'keep TrackingRecHitsOwned_ALCARECOTkAlMuonIsolated_*_*',
        'keep SiPixelClusteredmNewDetSetVector_ALCARECOTkAlMuonIsolated_*_*',
        'keep L1AcceptBunchCrossings_*_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_TriggerResults_*_*',
        'keep *_offlinePrimaryVertices_*_*',
        'keep DCSRecord_onlineMetaDataDigis_*_*',
        'keep Phase2TrackerCluster1DedmNewDetSetVector_ALCARECOTkAlMuonIsolated_*_*'
    )
)

# Other statements
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOTkAlMuonIsolated_noDrop.outputCommands)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T25', '')

# Path and EndPath definitions
process.endjob_step = cms.EndPath(process.endOfProcess)
process.ALCARECOStreamTkAlMuonIsolatedOutPath = cms.EndPath(process.ALCARECOStreamTkAlMuonIsolated)

# Schedule definition
process.schedule = cms.Schedule(process.pathALCARECOTkAlMuonIsolated,process.endjob_step,process.ALCARECOStreamTkAlMuonIsolatedOutPath)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads = 4
process.options.numberOfStreams = 0



# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
