import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

###################################################################
# Messages
###################################################################
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000

process.source = cms.Source("EmptySource",
                            firstRun = cms.untracked.uint32(362658),
                            numberEventsInRun = cms.untracked.uint32(1),
)

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '130X_dataRun3_HLT_v2', '')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

process.demo = cms.EDAnalyzer('MyAnalyzer')

process.p = cms.Path(process.demo)
