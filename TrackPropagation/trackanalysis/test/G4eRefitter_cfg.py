import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process("G4eRefit",Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.MeasurementTrackerEvent.pixelClusterProducer = 'ALCARECOTkAlZMuMu'
process.MeasurementTrackerEvent.stripClusterProducer = 'ALCARECOTkAlZMuMu'
process.MeasurementTrackerEvent.inactivePixelDetectorLabels = cms.VInputTag()
process.MeasurementTrackerEvent.inactiveStripDetectorLabels = cms.VInputTag() 

from Configuration.AlCa.GlobalTag import GlobalTag
# process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2022_realistic', '')
process.GlobalTag.globaltag = "124X_dataRun3_Prompt_v4"
process.GlobalTag.toGet = cms.VPSet(
    cms.PSet(record = cms.string("GeometryFileRcd"),
             tag = cms.string("XMLFILE_Geometry_123DD4hepV1_Extended2021_mc"),
             label = cms.untracked.string('Extended'),
          )
)

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.default = cms.untracked.PSet(ERROR = cms.untracked.PSet(limit = cms.untracked.int32(5)))
process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(20) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                '/store/data/Run2022C/DoubleMuon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/355/913/00000/895a68d0-657a-4090-b923-ec00c884abcf.root',
                                '/store/data/Run2022C/Muon/ALCARECO/TkAlZMuMu-PromptReco-v1/000/356/580/00000/c711091b-8c2e-49a6-b511-0829239425b4.root'
                            ),
                            skipEvents=cms.untracked.uint32(3930))


import Alignment.CommonAlignmentProducer.AlignmentTrackSelector_cfi
process.MuSkimSelector = Alignment.CommonAlignmentProducer.AlignmentTrackSelector_cfi.AlignmentTrackSelector.clone(applyBasicCuts = True,
                                                                                                                   theCharge = cms.int32(-1), 
                                                                                                                   filter = True,
                                                                                                                   src = "ALCARECOTkAlZMuMu",
                                                                                                                   ptMin = 0.,
                                                                                                                   pMin = 0.,
                                                                                                                   etaMin = -3.5,
                                                                                                                   etaMax = 3.5,
                                                                                                                   d0Min = -9999.,
                                                                                                                   d0Max = 9999.,
                                                                                                                   dzMin = -9999.,
                                                                                                                   dzMax = 9999.,
                                                                                                                   nHitMin = 0,
                                                                                                                   nHitMin2D = 0)

process.pretrackanalysis = cms.EDAnalyzer("trackanalysis",
                                          tracks = cms.untracked.InputTag("MuSkimSelector"))

process.load("TrackPropagation.Geant4e.geantRefit_cff")
process.Geant4eTrackRefitter.src = cms.InputTag("MuSkimSelector")
process.Geant4eTrackRefitter.usePropagatorForPCA = cms.bool(True)

process.trackanalysis = cms.EDAnalyzer("trackanalysis",
                                       tracks = cms.untracked.InputTag("Geant4eTrackRefitter"))

process.g4RefitPath = cms.Path(process.offlineBeamSpot* 
                               process.MeasurementTrackerEvent * 
                               process.MuSkimSelector * 
                               process.pretrackanalysis * 
                               process.geant4eTrackRefit * 
                               process.trackanalysis)

process.out = cms.OutputModule( "PoolOutputModule",
  outputCommands = cms.untracked.vstring(
  'keep *'
  ),
  fileName = cms.untracked.string( 'test.root' )
)

process.e = cms.EndPath(process.out)
process.schedule = cms.Schedule( process.g4RefitPath, process.e )
