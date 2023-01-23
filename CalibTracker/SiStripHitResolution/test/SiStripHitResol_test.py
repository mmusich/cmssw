import FWCore.ParameterSet.Config as cms

process = cms.Process("HitResol")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_data', '')  

InputTagName = "ALCARECOSiStripCalMinBias"
OutputRootFile = "hitresol_ALCARECO_2022F.root"
fileNames=cms.untracked.vstring("/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/ef6009e4-6857-40a1-9a55-0c702021caad.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/ef6cdbda-400c-4813-b4c7-9dfacd070e08.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f1a88b5f-8573-403e-aa35-0ad6b57125c0.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f1c537d0-2265-403b-84f9-dacb5a63c03f.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f30d1b57-eda6-4836-9ed6-cd683945a1e0.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f3c7f61d-7f6b-4021-b6c2-a15b66e3f375.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f3e11a67-7a78-4f6e-9b9b-b7687ce16c68.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f4250ffa-e73e-4e42-baa7-aebd8b169105.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f4c4cb8e-5c92-49b4-9fd3-40e09c4cf48a.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f4f5e6bd-0a16-4937-a3eb-5b76333d9c4d.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f5a5bd8e-b0be-4fb0-967b-4695ea851b9b.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f621fe39-c841-41da-82e9-d4478d70212e.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f623103e-0bf0-45e2-9eae-5ffb22fdeadc.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f6427525-18b5-4d7f-be0e-91ab1d577986.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f672d472-e7d5-4599-952e-d8d50945073e.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f67c28df-f403-4a83-a591-f4bdb165dd84.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f698e5d8-5b41-4777-ae43-460d54d3976a.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f6b3f1c4-86ec-4898-88fd-1bca7f62b790.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f6cd657e-92c4-442b-b23a-051324bf5d39.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f6e20b10-6dde-4541-8bdb-1cfe87af38e9.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f6e5cc1a-6d92-40a3-8458-e106da32802a.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f7aeb47e-f7a1-4396-a58c-54739b48369a.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f7bbb077-9a8e-4ac9-a679-f406308bab8f.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f7d67cd3-41b4-4c26-9071-dca7323be6b2.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f7df74df-3218-46f0-be25-d6fead5bfcd6.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/f9b7b869-979b-41cd-9337-648f66e216f5.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/fa243534-8e22-4dc2-abba-03bc4d34ecfe.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/fa7661c4-c194-40c6-ab1a-4883df9f1175.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/fa80d407-f32a-4e64-9a62-2666bc2cce64.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/faabd565-eafe-460b-b2de-ed6e66326e60.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/fb4eefef-0b9b-45f4-b861-8a11d95c57c7.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/fb83158d-1e46-419f-8cbb-9f7c3bd1c432.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/fbae4d0d-ce75-4b71-abdd-702bb734ef73.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/fbe069b5-99f1-494a-b916-314535f50430.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/fbf73d0c-e58c-4cbb-851e-09e2a67a09d4.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/fc0a765c-93f9-4a64-a867-7c3dd479d3fe.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/fc71ffea-9e40-44f5-9586-351bee0bd3e7.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/fd369a1a-f0d1-4f0e-9342-b0a45382e230.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/fdf15a26-fa7b-4302-9492-4fa35625724c.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/fe313c3f-dac2-4886-9a1e-3d9d458af9b3.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/fe9e79c9-f19b-4ea8-9241-6780a30bbb97.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/fec236d5-0ba5-4ac1-b040-2bf0fe7ee642.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/ff44f336-0add-40fa-b585-b4ab239933a5.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/ffec3b5f-83f6-4cec-9c2d-bf2d0f9c530f.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/167/00000/fff21490-1866-4ad5-9c84-33e403aabfda.root",
                                "/store/express/Run2022F/StreamExpress/ALCARECO/SiStripCalMinBias-Express-v1/000/362/180/00000/218a0cf6-4a5d-4375-8d43-6e94e8f6b052.root")

process.source = cms.Source("PoolSource", fileNames=fileNames)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000))

process.load("RecoVertex.BeamSpotProducer.BeamSpot_cfi")
#process.load("RecoLocalTracker.SiStripRecHitConverter.StripCPEfromTrackAngle_cfi")
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
process.refitTracks = process.TrackRefitterP5.clone(src=cms.InputTag(InputTagName))
process.load("CalibTracker.SiStripHitResolution.SiStripHitResol_cff")
process.anResol.combinatorialTracks = cms.InputTag("refitTracks")
process.anResol.trajectories = cms.InputTag("refitTracks")

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string(OutputRootFile)  
                                   )

process.allPath = cms.Path(process.MeasurementTrackerEvent*process.offlineBeamSpot*process.refitTracks*process.hitresol)
