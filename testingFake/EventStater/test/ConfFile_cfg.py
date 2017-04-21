import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.source = cms.Source("EmptySource",
                            firstRun = cms.untracked.uint32(291659),
                            numberEventsInRun = cms.untracked.uint32(1),
                            numberEventsInLuminosityBlock = cms.untracked.uint32(1),
                            firstTime = cms.untracked.uint64(6408036110198526976),
                            timeBetweenEvents = cms.untracked.uint64(1)
                            )

# process.source = cms.Source("EmptyIOVSource",
#                            timetype = cms.string('timestamp'),
#                            firstValue = cms.uint64(6408036110198526976),
#                            lastValue = cms.uint64(6408036110198526976),
#                            interval = cms.uint64(1)
#                            )

# process.source = cms.Source("EmptyIOVSource",
#                             firstValue = cms.uint64(291659),
#                             lastValue  = cms.uint64(291659),
#                             timetype  = cms.string('runnumber'),
#                             interval = cms.uint64(1)
#                             )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)


process.demo = cms.EDAnalyzer('EventStater')

process.p = cms.Path(process.demo)

#print process.dumpPython()
