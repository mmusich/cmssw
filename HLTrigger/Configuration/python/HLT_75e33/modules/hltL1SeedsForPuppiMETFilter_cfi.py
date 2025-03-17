import FWCore.ParameterSet.Config as cms

from FWCore.Modules.PathStatusFilter import PathStatusFilter as _PathStatusFilter

hltL1SeedsForPuppiMETFilter = _PathStatusFilter(
    logicalExpression = cms.string('pPuppiMET200')
)
