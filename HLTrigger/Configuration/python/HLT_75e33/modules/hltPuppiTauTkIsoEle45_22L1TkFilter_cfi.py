import FWCore.ParameterSet.Config as cms

from FWCore.Modules.PathStatusFilter import PathStatusFilter as _PathStatusFilter

hltPuppiTauTkIsoEle45_22L1TkFilter = _PathStatusFilter(
    logicalExpression = cms.string('pPuppiTauTkIsoEle45_22')
)
