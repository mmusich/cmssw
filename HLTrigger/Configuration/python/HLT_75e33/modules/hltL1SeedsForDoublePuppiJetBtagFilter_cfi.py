import FWCore.ParameterSet.Config as cms

from FWCore.Modules.PathStatusFilter import PathStatusFilter as _PathStatusFilter

hltL1SeedsForDoublePuppiJetBtagFilter = _PathStatusFilter(
    logicalExpression = cms.string('pDoublePuppiJet112_112')
)
