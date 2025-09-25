import FWCore.ParameterSet.Config as cms
from PhysicsTools.NanoAOD.common_cff import *

hltVertexTable = cms.EDProducer("HLTVertexTableProducer",
                                skipNonExistingSrc = cms.bool(True),
                                pvSrc = cms.InputTag("hltOfflinePrimaryVertices"),
                                goodPvCut = cms.string("!isFake && ndof >= 4.0 && abs(z) <= 24.0 && abs(position.Rho) <= 2.0"), 
                                pfSrc = cms.InputTag("hltParticleFlowTmp"),
                                dlenMin = cms.double(0),
                                dlenSigMin = cms.double(3),
                                pvName = cms.string("hltPrimaryVertex"))

hltPixelVertexTable = cms.EDProducer("HLTVertexTableProducer",
                                     skipNonExistingSrc = cms.bool(True),
                                     pvSrc = cms.InputTag("hltPhase2PixelVertices"),
                                     goodPvCut = cms.string(""),
                                     usePF = cms.bool(False), # use directly the tracks from PV fit 
                                     pfSrc = cms.InputTag(""),
                                     dlenMin = cms.double(0),
                                     dlenSigMin = cms.double(3),
                                     pvName = cms.string("hltPixelVertex"))

hltSimVertexTable = cms.EDProducer("SimpleTrackingVertexFlatTableProducer",
                                   skipNonExistingSrc = cms.bool(True),
                                   src = cms.InputTag("mix","MergedTrackTruth"),
                                   name = cms.string("hltSimVertices"),
                                   cut = cms.string("eventId().bunchCrossing() == 0 && eventId().event() == 0 && nDaughterTracks()!=2"),
                                   doc = cms.string("Sim Vertices information"),
                                   singleton = cms.bool(False),
                                   extension = cms.bool(False),
                                   variables = cms.PSet(
                                       x = Var("position().x()", "float", doc="x coordinate of the vertex"),
                                       y = Var("position().y()", "float", doc="y coordinate of the vertex"),
                                       z = Var("position().z()", "float", doc="z coordinate of the vertex"),
                                       bx = Var("eventId().bunchCrossing()","int", doc="bunch crossing of the sim vertex"),
                                       eid = Var("eventId().event()","int", doc="event id of the sim vertex"),
                                       tracksSize = Var("nDaughterTracks()", "uint", doc="number of tracks associated to the vertex"),
                                       inputTracks = Var("nSourceTracks()","uint", doc="number of input tracks")
                                   ))
