import FWCore.ParameterSet.Config as cms

demo = cms.EDAnalyzer('SiStripNoiseVisualizer'
     ,tracks = cms.untracked.InputTag('ctfWithMaterialTracks')
)
