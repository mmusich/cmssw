import FWCore.ParameterSet.Config as cms

#
# MM. Apr 3rd 2019: temporary customize function to avoid running Cluster Repair on Prompt-like workflows
#
def doNotRunClusterRepair(process):

    if hasattr(process,'TTRHBuilderAngleAndTemplate') and hasattr(process.TTRHBuilderAngleAndTemplate,'PixelCPE'):
        print("Warning: disactivating cluster repair for Prompt-Like workflows")
        process.TTRHBuilderAngleAndTemplate.PixelCPE = cms.string('PixelCPETemplateReco')

    return process
