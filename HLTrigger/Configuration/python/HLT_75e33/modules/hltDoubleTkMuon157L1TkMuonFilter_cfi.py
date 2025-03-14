import FWCore.ParameterSet.Config as cms

from FWCore.Modules.PathStatusFilter import PathStatusFilter as _PathStatusFilter

hltDoubleTkMuon157L1TkMuonFilter = _PathStatusFilter(
    logicalExpression = cms.string('pDoubleTkMuon15_7')
)
