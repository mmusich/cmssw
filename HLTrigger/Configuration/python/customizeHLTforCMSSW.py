import FWCore.ParameterSet.Config as cms

# helper functions
from HLTrigger.Configuration.common import *

# add one customisation function per PR
# - put the PR number into the name of the function
# - add a short comment
# for example:

# CCCTF tuning
# def customiseFor12718(process):
#     for pset in process._Process__psets.values():
#         if hasattr(pset,'ComponentType'):
#             if (pset.ComponentType == 'CkfBaseTrajectoryFilter'):
#                 if not hasattr(pset,'minGoodStripCharge'):
#                     pset.minGoodStripCharge = cms.PSet(refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone'))
#     return process



def customiseForOffline(process):
    # For running HLT offline and relieve the strain on Frontier so it will no longer inject a
    # transaction id which tells Frontier to add a unique "&freshkey" to many query URLs.
    # That was intended as a feature to only be used by the Online HLT, to guarantee that fresh conditions
    # from the database were loaded at each Lumi section
    # Seee CMSHLT-3123 for further details
    if hasattr(process, 'GlobalTag'):
        # Set ReconnectEachRun and RefreshEachRun to False
        process.GlobalTag.ReconnectEachRun = cms.untracked.bool(False)
        process.GlobalTag.RefreshEachRun = cms.untracked.bool(False)

        if hasattr(process.GlobalTag, 'toGet'):
            # Filter out PSet objects containing only 'record' and 'refreshTime'
            process.GlobalTag.toGet = [
                pset for pset in process.GlobalTag.toGet
                if set(pset.parameterNames_()) != {'record', 'refreshTime'}
            ]

    return process

def customiseFor2024L1TMenu(process):

    seed_replacements = {
        'L1_AXO_Medium' : 'L1_AXO_Nominal',
        #disable new L1 seeds by renaming to a disabled seed.
        'L1_SingleMu5_BMTF' : 'L1_SingleMuCosmics',
        'L1_SingleMu13_SQ14_BMTF' : 'L1_SingleMuCosmics',
        'L1_CICADA_VVVVTight' : 'L1_SingleMuCosmics',
        'L1_CICADA_VVVTight' : 'L1_SingleMuCosmics',
        'L1_CICADA_VVTight' : 'L1_SingleMuCosmics',
        'L1_AXO_VVVTight' : 'L1_SingleMuCosmics',
        'L1_AXO_VVTight' : 'L1_SingleMuCosmics'
    }

    for module in filters_by_type(process, 'HLTL1TSeed'):
        l1Seed = module.L1SeedsLogicalExpression.value()
        if any(old_seed in l1Seed for old_seed in seed_replacements):
            # Replace each old seed with the new seed
            for old_seed, new_seed in seed_replacements.items():
                l1Seed = l1Seed.replace(old_seed, new_seed)
            module.L1SeedsLogicalExpression = cms.string(l1Seed)

    return process

# CMSSW version specific customizations
def customizeHLTforCMSSW(process, menuType="GRun"):

    process = customiseForOffline(process)
    process = customiseFor2024L1TMenu(process)

    # add call to action function in proper order: newest last!
    # process = customiseFor12718(process)
    
    return process
