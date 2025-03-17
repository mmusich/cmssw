import FWCore.ParameterSet.Config as cms

from FWCore.Modules.PathStatusFilter import PathStatusFilter as _PathStatusFilter

hltL1SeedsForPuppiJetFilter = _PathStatusFilter(
    logicalExpression = cms.string('pSinglePuppiJet230')
)
