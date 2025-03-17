import FWCore.ParameterSet.Config as cms

from FWCore.Modules.PathStatusFilter import PathStatusFilter as _PathStatusFilter

hltEGL1SeedsForSingleEleNonIsolatedFilter = _PathStatusFilter(
    logicalExpression = cms.string('pSingleEGEle51 or pSingleTkEle36')
)
