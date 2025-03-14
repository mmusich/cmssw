import FWCore.ParameterSet.Config as cms

from FWCore.Modules.PathStatusFilter import PathStatusFilter as _PathStatusFilter

hltEGL1SeedsForDoubleEleNonIsolatedFilter = _PathStatusFilter(
    logicalExpression = cms.string('pDoubleEGEle37_24 or pDoubleTkEle25_12')
)
