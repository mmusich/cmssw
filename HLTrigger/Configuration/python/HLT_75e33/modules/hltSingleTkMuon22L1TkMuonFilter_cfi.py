import FWCore.ParameterSet.Config as cms

from FWCore.Modules.PathStatusFilter import PathStatusFilter as _PathStatusFilter

hltSingleTkMuon22L1TkMuonFilter = _PathStatusFilter(
    logicalExpression = cms.string('pSingleTkMuon22')
)
