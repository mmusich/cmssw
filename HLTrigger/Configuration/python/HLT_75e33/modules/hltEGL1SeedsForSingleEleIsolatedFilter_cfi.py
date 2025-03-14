import FWCore.ParameterSet.Config as cms

from FWCore.Modules.PathStatusFilter import PathStatusFilter as _PathStatusFilter

hltEGL1SeedsForSingleEleIsolatedFilter = _PathStatusFilter(
    logicalExpression = cms.string('pSingleEGEle51 or pSingleTkEle36 or pSingleIsoTkEle28')
)
