import FWCore.ParameterSet.Config as cms

# AlCaReco for track based alignment using ZMuMu events (including the tracks from the PV)
OutALCARECOTkAlZMuMuAndVertex_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlZMuMuAndVertex')
    ),
    outputCommands = cms.untracked.vstring(
        'keep *_ALCARECOTkAlZMuMuAndVertex_*_*', 
        'keep *_ALCARECOTkAlZMuMuVertexTracks_*_*',
        'keep *_muons__*', 
        'keep L1AcceptBunchCrossings_*_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_TriggerResults_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
	'keep *_offlinePrimaryVertices_*_*')
)
OutALCARECOTkAlZMuMuAndVertex = OutALCARECOTkAlZMuMuAndVertex_noDrop.clone()
OutALCARECOTkAlZMuMuAndVertex.outputCommands.insert(0, "drop *")
