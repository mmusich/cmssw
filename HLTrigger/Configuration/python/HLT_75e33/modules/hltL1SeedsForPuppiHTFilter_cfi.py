import FWCore.ParameterSet.Config as cms

from FWCore.Modules.PathStatusFilter import PathStatusFilter as _PathStatusFilter

hltL1SeedsForPuppiHTFilter = _PathStatusFilter(
    logicalExpression = cms.string('pPuppiHT450')
)
