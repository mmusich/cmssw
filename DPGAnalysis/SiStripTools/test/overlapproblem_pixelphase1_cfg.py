import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("OverlapProblemALCAZmumu")

#prepare options

options = VarParsing.VarParsing("analysis")

options.register('globalTag',
                 "DONOTEXIST",
                 VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                 VarParsing.VarParsing.varType.string,          # string, int, or float
                 "GlobalTag")
#options.globalTag = "DONOTEXIST::All"

options.parseArguments()

#
process.load("DPGAnalysis.SiStripTools.processOptions_cff")
process.load("DPGAnalysis.SiStripTools.MessageLogger_cff")

process.MessageLogger.cout.threshold = cms.untracked.string("WARNING")
#process.MessageLogger.debugModules = cms.untracked.vstring("overlapproblemanalyzer")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(options.inputFiles),
                            #                    skipBadFiles = cms.untracked.bool(True),
                            inputCommands = cms.untracked.vstring("keep *", "drop *_MEtoEDMConverter_*_*")
                            )

process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
#process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.Geometry.GeometryExtended2017Reco_cff")
#process.load("Configuration.Geometry.GeometryExtendedPhaseIPixelReco_cff")
#process.load("Configuration.Geometry.GeometryExtendedPhaseIPixel_cff")
process.load("SimTracker.TrackAssociatorProducers.trackAssociatorByHits_cfi")


process.load("DPGAnalysis.SiStripTools.tkAlTrackRefitSequence_cff")
process.refittedTracks.src = cms.InputTag("generalTracks")
process.refittedTracks.TTRHBuilder = cms.string('WithTrackAngle')

process.load('SLHCUpgradeSimulations.Geometry.fakeConditions_Phase1_R30F12_cff')

#process.KFFittingSmootherWithOutliersRejectionAndRK.LogPixelProbabilityCut = cms.double(-16.0)


process.load("RecoLocalTracker.SiPixelRecHits.PixelCPEGeneric_cfi")

#process.siPixelRecHits.CPE = cms.string('PixelCPEGeneric')

process.load("DPGAnalysis.SiStripTools.overlapproblemtsosanalyzer_cfi")
process.overlapproblemtsoshitfiltered = process.overlapproblemtsosanalyzer.clone(trajTrackAssoCollection = cms.InputTag("HitFilteredTracks"))
process.overlapproblemtsosats = process.overlapproblemtsosanalyzer.clone(trajTrackAssoCollection = cms.InputTag("refittedATSTracks"))

process.overlapproblemtsosall = process.overlapproblemtsosanalyzer.clone(onlyValidRecHit = cms.bool(False))
process.overlapproblemtsoshitfilteredall = process.overlapproblemtsoshitfiltered.clone(onlyValidRecHit = cms.bool(False))
process.overlapproblemtsosatsall = process.overlapproblemtsosats.clone(onlyValidRecHit = cms.bool(False))

process.load("DPGAnalysis.SiStripTools.overlapproblemtpanalyzer_cfi")
#process.load("DebugTools.RecHits.tpanalyzer_cfi")



process.p0 = cms.Path( process.seqTrackRefitting
                       + process.trackAssociatorByHits
                       + process.overlapproblemtsosanalyzer # + process.overlapproblemtsoshitfiltered + process.overlapproblemtsosats
                       + process.overlapproblemtsosall # + process.overlapproblemtsoshitfilteredall + process.overlapproblemtsosatsall 
                       + process.overlapproblemtpanalyzer
#                       + process.tpanalyzer
                       )

#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, options.globalTag, '')


process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('OverlapProblem_tpanalyzer.root')
                                   )

#print process.dumpPython()
