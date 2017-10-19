import FWCore.ParameterSet.Config as cms

anRes = cms.EDAnalyzer("SiStripHitResolution",    
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

hitres = cms.Sequence( anRes )
