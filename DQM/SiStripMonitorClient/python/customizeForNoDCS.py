import FWCore.ParameterSet.Config as cms
'''
The following customization will remove all checks on SiStrip DCS bits 
for SiStrip and Tracking Monitors
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
                    
    #(24, 25, 26, 27, 28, 29) # 24-27: strip, 28-29: pixel
    # see https://github.com/cms-sw/cmssw/blob/master/DataFormats/Scalers/interface/DcsStatus.h#L51
    for producer in producers_by_type(process, 'SiStripMonitorCluster'):
        producer.StripDCSfilter.dcsPartitions = cms.vint32(28, 29)

    #(24, 25, 26, 27, 28, 29) # 24-27: strip, 28-29: pixel
    # see https://github.com/cms-sw/cmssw/blob/master/DataFormats/Scalers/interface/DcsStatus.h#L51
    for producer in producers_by_type(process, 'TrackingMonitor'):
        producer.genericTriggerEventPSet.dcsPartitions = cms.vint32(28, 29)

    return process
