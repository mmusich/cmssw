import FWCore.ParameterSet.Config as cms

from Alignment.CommonAlignmentProducer.alignmentTrackFromVertexSelectorModule_cfi import alignmentTrackFromVertexSelectorModule
AlignmentTracksFromVertexSelector = alignmentTrackFromVertexSelectorModule.clone(src = cms.InputTag("generalTracks"),
                                                                                 vertices = cms.InputTag("offlinePrimaryVertices"),
                                                                                 leptonTracks = cms.InputTag("ALCARECOTkAlDiMuon"),
                                                                                 useClosestVertexToDilepton = cms.bool(False),
                                                                                 vertexIndex = cms.uint32(0),
                                                                                 filter = cms.bool(False))
