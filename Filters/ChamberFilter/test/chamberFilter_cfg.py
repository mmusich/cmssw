import FWCore.ParameterSet.Config as cms

import os
#inputfiles = os.environ["ALIGNMENT_INPUTFILES"].split(" ")
#jobnumber = int(os.environ["ALIGNMENT_JOBNUMBER"])

process = cms.Process("CHAMBERFILTER")

process.source = cms.Source("PoolSource",
     fileNames = cms.untracked.vstring(
        '/store/data/Run2012A/SingleMu/ALCARECO/MuAlCalIsolatedMu-13Jul2012-v1/00000/AE61973D-F3D0-E111-8112-0017A4770434.root'
    )
)


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

process.MessageLogger = cms.Service("MessageLogger",
                                    destinations = cms.untracked.vstring("cout"),
                                    cout = cms.untracked.PSet(threshold = cms.untracked.string("INFO")))

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = "GR_R_53_V16A::All"

process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")

process.ChamberFilter = cms.EDFilter("ChamberFilter",
  tracksTag      = cms.InputTag("ALCARECOMuAlCalIsolatedMu:GlobalMuon"),
  minTrackPt     = cms.double(30.),
  minTrackEta    = cms.double(-2.4),
  maxTrackEta    = cms.double(2.4),
  minTrackerHits = cms.int32(10),
  minDTHits      = cms.int32(1),
  minCSCHits     = cms.int32(1)
)

process.Path = cms.Path(process.ChamberFilter)

process.output = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string("SingleMu_Run2012A_MuAlCalIsolatedMu-13Jul2012-v1_MEp_1_3_1.root"),
  SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("Path"))
)

process.EndPath = cms.EndPath(process.output)

