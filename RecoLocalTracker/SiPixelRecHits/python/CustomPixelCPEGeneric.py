'''Customization functions for cmsDriver to change the phase-2 tracker local reconstruction for configuration different from regular planar rectangular pixels'''
import FWCore.ParameterSet.Config as cms
def customizeFor3DPixels(process):
    
    ''' Will remove any usage of template / genError payloads from the reconstruction
    '''
    
    if hasattr(process,'PixelCPEGenericESProducer'):
        try:
            process.PixelCPEGenericESProducer.UseErrorsFromTemplates = False    # no GenErrors
            process.PixelCPEGenericESProducer.LoadTemplatesFromDB = False       # do not load templates
        except ValueError:
            raise SystemExit("\n\n ERROR! Could not customize for 3D pixels \n\n")
            
    return process

def customizeForSquarePixels(process):
    
    ''' Do use Template errors for square pixels even in the first tracking step
    '''
    
    if hasattr(process,'PixelCPEGenericESProducer'):
        try:
            process.PixelCPEGenericESProducer.NoTemplateErrorsWhenNoTrkAngles = False # use genErrors in the seeding step
        except ValueError:
            raise SystemExit("\n\n ERROR! Could not customize for square pixels \n\n")

    return process
