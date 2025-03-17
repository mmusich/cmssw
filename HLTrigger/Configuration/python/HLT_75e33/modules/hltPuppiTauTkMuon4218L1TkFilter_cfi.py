import FWCore.ParameterSet.Config as cms

from FWCore.Modules.PathStatusFilter import PathStatusFilter as _PathStatusFilter

hltPuppiTauTkMuon4218L1TkFilter = _PathStatusFilter(
    logicalExpression = cms.string('pPuppiTauTkMuon42_18')
)
