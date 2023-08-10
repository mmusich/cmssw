import FWCore.ParameterSet.Config as cms
'''
The following customization will remove all checks on SiStrip DCS bits 
for SiStrip and Tracking MonitorClients
'''

def producers_by_type(process, *types):
    return (module for module in process._Process__producers.values() if module._TypedParameterizable__type in types)

def removeSiStripDCSChecks(process):

    print('WARNING: removing SiStrip DCS Checks in Strip and Tracking Monitors')

    for producerType in [
            'SiStripMonitorTrack',
            'SiStripMonitorCluster']:
        for producer in producers_by_type(process, producerType):
            producer.UseDCSFiltering = cms.bool(False)
                    
    for producer in producers_by_type(process, 'SiStripMonitorCluster'):
        producer.StripDCSfilter.dcsPartitions = cms.vint32()

    for producer in producers_by_type(process, 'TrackingMonitor'):
        producer.genericTriggerEventPSet.dcsPartitions = cms.vint32()

    return process
