import FWCore.ParameterSet.Config as cms

from CommonTools.RecoAlgos.PFCandidatePrimaryVertexSorter import PFCandidatePrimaryVertexSorter as _PFCandidatePrimaryVertexSorter

hltPrimaryVertexAssociation = _PFCandidatePrimaryVertexSorter(
    assignment = dict(
        DzCutForChargedFromPUVtxs = 0.2,
        EtaMinUseDz = -1,
        NumOfPUVtxsForCharged = 0,
        OnlyUseFirstDz = False,
        PtMaxCharged = -1,
        maxDistanceToJetAxis = 0.07,
        maxDtSigForPrimaryAssignment = 3.0,
        maxDxyForJetAxisAssigment = 0.1,
        maxDxyForNotReconstructedPrimary = 0.01,
        maxDxySigForNotReconstructedPrimary = 2,
        maxDzErrorForPrimaryAssignment = 0.05,
        maxDzForJetAxisAssigment = 0.1,
        maxDzForPrimaryAssignment = 0.1,
        maxDzSigForPrimaryAssignment = 5.0,
        maxJetDeltaR = 0.5,
        minJetPt = 25,
        preferHighRanked = False,
        useTiming = False,
        useVertexFit = True
    ),
    jets = ("hltAK4PFPuppiJets"),
    particles = ("hltParticleFlowTmp"),
    produceAssociationToOriginalVertices = True,
    produceNoPileUpCollection = False,
    producePileUpCollection = False,
    produceSortedVertices = False,
    qualityForPrimary = 2,
    sorting = dict(

    ),
    usePVMET = True,
    vertices = ("hltOfflinePrimaryVertices")
)
