import FWCore.ParameterSet.Config as cms

from FWCore.Modules.PathStatusFilter import PathStatusFilter as _PathStatusFilter

hltEGL1SeedsForSinglePhotonIsolatedFilter = _PathStatusFilter(
    logicalExpression = cms.string('pSingleEGEle51 or pSingleIsoTkPho36')
)
