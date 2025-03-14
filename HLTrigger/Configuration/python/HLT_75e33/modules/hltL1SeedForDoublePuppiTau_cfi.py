import FWCore.ParameterSet.Config as cms

from FWCore.Modules.PathStatusFilter import PathStatusFilter as _PathStatusFilter

hltL1SeedForDoublePuppiTau = _PathStatusFilter(
    logicalExpression = cms.string('pDoublePuppiTau52_52')
)
