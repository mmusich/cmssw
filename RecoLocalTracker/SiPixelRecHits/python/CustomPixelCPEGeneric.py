'''Customization functions for cmsDriver to change the phase-2 tracker local reconstruction for configuration different from regular planar rectangular pixels'''
import FWCore.ParameterSet.Config as cms

def _esproducers_by_type(process, *types):
    "Find all ESProducers in the Process that are instances of the given C++ type."
    return (module for module in process._Process__esproducers.values() if module._TypedParameterizable__type in types)

def customizeFor3DPixels(process):
    
    ''' Will remove any usage of template / genError payloads from the reconstruction
    '''
    
    for producer in _esproducers_by_type(process, "PixelCPEGenericESProducer"):
        producer.UseErrorsFromTemplates = False  # no GenErrors
        producer.LoadTemplatesFromDB = False     # do not load templates
            
    return process

def customizeForSquarePixels(process):
    
    ''' Do use Template errors for square pixels even in the first tracking step
        This is needed because hardcoded errors in https://github.com/cms-sw/cmssw/blob/master/RecoLocalTracker/SiPixelRecHits/src/PixelCPEGeneric.cc#L113
        have been optimized for rectangular 25x100 pixels, and in the current generic reco setup we use hardcoded errors for the first tracking pass
    '''
    
    for producer in _esproducers_by_type(process, "PixelCPEGenericESProducer"):
        producer.NoTemplateErrorsWhenNoTrkAngles = cms.bool(False) # use genErrors in the seeding step (when no track angles are available)

    return process
