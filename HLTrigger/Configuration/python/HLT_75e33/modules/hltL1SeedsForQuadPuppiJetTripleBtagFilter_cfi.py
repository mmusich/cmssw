import FWCore.ParameterSet.Config as cms

from FWCore.Modules.PathStatusFilter import PathStatusFilter as _PathStatusFilter

hltL1SeedsForQuadPuppiJetTripleBtagFilter = _PathStatusFilter(
    logicalExpression = cms.string('pPuppiHT400 and pQuadJet70_55_40_40')
)
