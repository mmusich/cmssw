import FWCore.ParameterSet.Config as cms

process = cms.Process('test')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

# Input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('/store/express/Run2017F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/305/045/00000/087CFA02-8FB0-E711-80B3-02163E0145EE.root'),
                            secondaryFileNames = cms.untracked.vstring()
                            )

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '92X_dataRun2_Express_v7', '')

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('HitRes_data_alcareco.root')
                                   )

process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
process.load("RecoTracker.MeasurementDet.MeasurementTrackerEventProducer_cfi")
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
process.load("RecoTracker.TrackProducer.TrackRefitter_cfi")
process.TrackRefitter.src = cms.InputTag("ALCARECOSiStripCalMinBias")

process.analysis = cms.EDAnalyzer("SiStripHitResolution",    
                                  tracks = cms.InputTag("TrackRefitter"),
                                  trajectories = cms.InputTag("TrackRefitter"),                
                                  associatePixel = cms.bool(False),
                                  associateStrip = cms.bool(False),
                                  associateRecoTracks = cms.bool(False),    
                                  pairsOnly = cms.bool(False),
                                  minMomentum = cms.double(3.),
                                  genTruth = cms.bool(False),
                                  ROUList = cms.vstring('g4SimHitsTrackerHitsTIBLowTof', 
                                                        'g4SimHitsTrackerHitsTIBHighTof', 
                                                        'g4SimHitsTrackerHitsTIDLowTof', 
                                                        'g4SimHitsTrackerHitsTIDHighTof', 
                                                        'g4SimHitsTrackerHitsTOBLowTof', 
                                                        'g4SimHitsTrackerHitsTOBHighTof', 
                                                        'g4SimHitsTrackerHitsTECLowTof', 
                                                        'g4SimHitsTrackerHitsTECHighTof'
                                                        'TrackerHitsTIBLowTof', 
                                                        'TrackerHitsTIBHighTof', 
                                                        'TrackerHitsTIDLowTof', 
                                                        'TrackerHitsTIDHighTof', 
                                                        'TrackerHitsTOBLowTof', 
                                                        'TrackerHitsTOBHighTof', 
                                                        'TrackerHitsTECLowTof', 
                                                        'TrackerHitsTECHighTof'
                                                        ),                                                                 
                                  stripSimLinkSrc = cms.InputTag("simSiStripDigis")
                                  )

process.aPath = cms.Path(process.offlineBeamSpot+process.MeasurementTrackerEvent+process.TrackRefitter+process.analysis)
process.schedule = cms.Schedule(process.aPath)


